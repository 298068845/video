import socket
import main_panel
from bean import *
from LoadingMask import *
import subprocess
from pycocotools.coco import COCO
from pycocotools.cocoeval import COCOeval
import json
class pingUtils(QThread):
    mysignal = pyqtSignal(int,main_panel.Ui_MainWindow,int) 
    def __init__(self,ui):
        super(pingUtils,self).__init__()
        self.ui = ui

        
    def run(self):
        for x in range(len(self.ui.ip)):
            #ui.loading_mask = LoadingMask(MainWindow,None,"正在检索%s……"%x,500)
            #ui.loading_mask.show()
            #ret = os.system('ping -w 1 %s'%self.ui.ip[x]) # 实现pingIP地址的功能，-c1指发送报文一次，-w1指等待1秒
            ret = subprocess.call("ping -w 1 %s"%self.ui.ip[x],shell=True)
            self.mysignal.emit(ret,self.ui,x)

class helloUtils(QThread):
     mysignal = pyqtSignal(main_panel.Ui_MainWindow,int) 
     def __init__(self,mainUi):
        super(helloUtils,self).__init__()
        self.mainUi = mainUi
    
     def run(self):
        try:
            client = socket.socket()
            #client.connect(('192.168.2.109', 5000))
            client.connect((self.mainUi.selectIp, 5000))
            client.send(to1b(Ruquest.HELLO))
            data = client.recv(512)
            if(data[0]==Response.HELLO):
                msg = getHello(data)
                print(msg.type)
                print(msg.signName)
                print(msg.deviceName)
                self.mainUi.deviceName = msg.deviceName
                self.mainUi.signName = msg.signName
                self.mysignal.emit(self.mainUi,Response.HELLO)
        except TimeoutError:
            self.mysignal.emit(self.mainUi,Response.TIMEOUT)
            print('超时！')
        except ConnectionResetError:
            self.mysignal.emit(self.mainUi,Response.CLOSE)
            print('连接中断！')
        except ConnectionRefusedError:
            self.mysignal.emit(self.mainUi,Response.REJECT)
            print('连接被拒绝')
        else:
            client.close()  
            
        
class testUtils(QThread):
     mysignal = pyqtSignal(main_panel.Ui_MainWindow,int) 
     def __init__(self,testUi):
        super(testUtils,self).__init__()
        self.testUi = testUi
        
     def run(self):
        try:
            print("starttest")
            client = socket.socket()
            #client.connect(('192.168.2.109', 5000))
            client.connect((self.testUi.selectIp, 5000))
            client.send(setTestInfo(Ruquest.TEST,self.testUi.curId,self.testUi.type,self.testUi.currentModelPath,self.testUi.currentImagePath))
            data = client.recv(512)
            print(data)
            if(data[0]==Response.TEST):
                msg = getTestCallBackInfo(data)
                print(msg.type)
                print(msg.id)
                print(msg.state)
                if(msg.state==0):
                    print("开始推断任务")
                    self.mysignal.emit(self.testUi,Response.TEST)
                else:
                    print("推断失败")
        except ConnectionResetError:
            self.mysignal.emit(self.testUi,Response.CLOSE)
            print('连接中断！')
        except ConnectionRefusedError:
            self.mysignal.emit(self.testUi,Response.REJECT)
            print('连接被拒绝')
        else:
            client.close()  
            
class CheckUtils(QThread):
     mysignal = pyqtSignal(main_panel.Ui_MainWindow,int) 
     def __init__(self,testUi):
        super(CheckUtils,self).__init__()
        self.testUi = testUi

     def run(self):
        try:
            print("check")
            client = socket.socket()
            client.connect((self.testUi.selectIp, 5000))
            client.send(to1b(Ruquest.STATE))
            data = client.recv(512)
            if(data[0]==Response.STATE):
                msg = getStateInfo(data)
                self.testUi.state = msg.state
                if(msg.state==0):
                    # print("finish")
                    self.mysignal.emit(self.testUi,Response.STATE)
                else:
                    # print("sumit")
                    self.mysignal.emit(self.testUi,Ruquest.STATE)
        except ConnectionResetError:
            self.mysignal.emit(self.testUi,Response.CLOSE)
            print('连接中断！')
        except ConnectionRefusedError:
            self.mysignal.emit(self.testUi,Response.REJECT)
            print('连接被拒绝')
        else:
            client.close()  
            
class getDetectUtils(QThread):
     mysignal = pyqtSignal(main_panel.Ui_MainWindow,int) 
     def __init__(self,testUi):
        super(getDetectUtils,self).__init__()
        self.testUi = testUi
        
     def run(self):
        try:
            client = socket.socket()
            client.connect((self.testUi.selectIp, 5000))
            client.send(setAskResultInfo(Ruquest.RESULT, self.testUi.curId))
            data = client.recv(10)
            print(data)
            detectList=[]
            imagesize = 0
            if (data[0] == Response.RESULT):
                head = getResultInfo(data)
                print("imageNum",head.imageSize)
                imagesize = str(head.imageSize)
                content = b''
                for i in range(head.imageSize):
                    item = client.recv(8)
                    item = getDetectInfo(item)
                    #print(item.num,item.no)
                    for j in range(item.num):
                        newcontent = client.recv(24)
                        #print(newcontent)
                        content = content + newcontent
                        d = getDetectContentInfo(newcontent)
                        #print(d.width, d.height, d.x, d.y, d.score, d.index)
                        data = {
                               "category_id":d.index+int(self.testUi.convert[d.index]),
                               "image_id":int(self.testUi.idlist[item.no-1]),
                               "bbox" :[d.x, d.y,d.width, d.height],
                               "score":d.score
                                }
                        detectList.append(data)
                t = getTimeInfo(client.recv(12))
                with open('yolo3.json', 'w') as json_data:
                    json.dump(detectList, json_data, ensure_ascii=False)
                cocoGt = COCO("instances_val2017.json")
                cocoDt = cocoGt.loadRes(detectList)
                imagids = sorted(cocoGt.getImgIds())
                imagids = imagids[0: head.imageSize]
                cocoEval = COCOeval(cocoGt, cocoDt, 'bbox')
                cocoEval.params.imgIds = imagids
                cocoEval.evaluate()
                cocoEval.accumulate()
                cocoEval.summarize()
                self.testUi.map = cocoEval.stats
                self.testUi.fps = str(round(head.imageSize*1000/t.inferenceTime,3))+"fps"
                self.testUi.inferenceTime = t.inferenceTime
                self.testUi.imageTime = t.imageTime
                self.testUi.modelTime = t.modelTime
                #self.testUi.ui.CostTime.setText(str(round(head.imageSize*1000/t.inferenceTime,3))+"fps")
                self.testUi.totalCost = t.inferenceTime + t.imageTime + t.modelTime
                print("inferenceTime", "imageTime", "modelTime")
                print(t.inferenceTime, t.imageTime, t.modelTime)
                print("totalCost",self.testUi.totalCost)
                print("获取推断结果成功")
                self.testUi.imagesize = imagesize
                self.mysignal.emit(self.testUi,Response.RESULT)
        except ConnectionResetError:
            self.mysignal.emit(self.testUi,Response.CLOSE)
            print('连接中断！')
        except ConnectionRefusedError:
            self.mysignal.emit(self.testUi,Response.REJECT)
            print('连接被拒绝')
        else:
            client.close()  
    
class getClassfyUtils(QThread):
     mysignal = pyqtSignal(main_panel.Ui_MainWindow,int) 
     def __init__(self,testUi):
        super(getClassfyUtils,self).__init__()
        self.testUi = testUi
        
     def run(self):
        try:
            self.testUi.top1 = 0
            self.testUi.top5 = 0
            client = socket.socket()
            client.connect((self.testUi.selectIp, 5000))
            client.send(setAskResultInfo(Ruquest.RESULT, self.testUi.curId))
            data = client.recv(10)
            imagesize = 0
            if(data[0]==Response.RESULT):
                head = getResultInfo(data)
                print("imageNum",head.imageSize)
                imagesize = str(head.imageSize)
                Batch_size = 44 * head.imageSize+12
                content = b''
                while(len(content)<Batch_size):
                    # print(content)
                    # print(len(content))
                    content = content+client.recv(1320)
 
                #print(len(content))
                for i in range(head.imageSize):
                    c = getClassifyContentInfo(content[i*44:(i+1)*44])
                    trueIndex = int(self.testUi.truelabel[i])
                    top1core = c.score1
                    top1index = c.index1
                    if(c.score2>top1core):
                        top1core = c.score2
                        top1index = c.index2
                    if(c.score3>top1core):
                        top1core = c.score3
                        top1index = c.index3
                    if(c.score4>top1core):
                        top1core = c.score4
                        top1index = c.index4
                    if(c.score5>top1core):
                        top1core = c.score5
                        top1index = c.index5
                    if(top1index==trueIndex):
                        self.testUi.top1 = self.testUi.top1 +1

                    if c.index1 == trueIndex:
                        self.testUi.top5 = self.testUi.top5 +1
                    elif c.index2 == trueIndex:
                        self.testUi.top5 = self.testUi.top5 +1
                    elif c.index3 == trueIndex:
                        self.testUi.top5 = self.testUi.top5 +1
                    elif c.index4 == trueIndex:
                        self.testUi.top5 = self.testUi.top5 +1
                    elif c.index5 == trueIndex:
                        self.testUi.top5 = self.testUi.top5 +1
                     
                print(self.testUi.top1,self.testUi.top5)
                self.testUi.top1 = self.testUi.top1*100/head.imageSize
                self.testUi.top5 = self.testUi.top5*100/head.imageSize
                t = getTimeInfo(content[Batch_size-12:Batch_size])
                self.testUi.inferenceTime = t.inferenceTime
                self.testUi.imageTime = t.imageTime
                self.testUi.modelTime = t.modelTime
                self.testUi.totalCost = t.inferenceTime + t.imageTime + t.modelTime
                print("inferenceTime", "imageTime", "modelTime")
                print(t.inferenceTime, t.imageTime, t.modelTime)
                print("totalCost",self.testUi.totalCost)
                self.testUi.fps = str(round(head.imageSize*1000/t.inferenceTime,3))+"fps"
                self.testUi.imagesize = imagesize
                print("获取推断结果成功")
                self.mysignal.emit(self.testUi,Response.RESULT)
        except ConnectionResetError:
            self.mysignal.emit(self.testUi,Response.CLOSE)
            print('连接中断！')
        except ConnectionRefusedError:
            self.mysignal.emit(self.testUi,Response.REJECT)
            print('连接被拒绝')
        else:
            client.close()  
    