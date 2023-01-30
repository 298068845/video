import csv
default = ["192.168.2","211","",
           "/mnt/classify_detect/classify_detect/model/mobilenet_v2_magik.pb.bin",
           "/mnt/classify_detect/classify_detect/classify_images.txt",
           "/mnt/classify_detect/classify_detect/model/yolov3_magik.pb.bin",
           "/mnt/classify_detect/classify_detect/yolov3_images.txt",
           "/mnt/classify_detect/classify_detect/model/resnet50_v2_magik.bin"]

def getConfig():
    try:
        f =  open("config.txt")
        txt = f.read().splitlines()
        print(txt)
        if len(txt)==0 or str(txt[0])=="":
            return default
        else:
            return txt
    except FileNotFoundError:
        with open("config.txt") as ff:
            print("文件创建成功！")
            return []

def saveConfig(ip1,ip2,ip3,path1,path2):
    f = open('config.txt', mode='w')  # 打开文件，若文件不存在系统自动创建。
    f.write(ip1+','+ip2+','+ip3+','+path1+','+path2)  # write 写入


def getClassifyLabel():
    txt_path= 'classifyLabel.txt'
    f = open(txt_path)
    data_lists = f.read().splitlines()
    f.close()
    return data_lists

def getConvert():
    txt_path= 'convert.txt'
    f = open(txt_path)
    data_lists = f.read().splitlines()
    f.close()
    return data_lists

def getDetectId():
    txt_path= 'yolov3_id.txt'
    f = open(txt_path)
    data_lists = f.read().splitlines()
    f.close()
    return data_lists

def writeHistory(self):
    path = 'history.csv'
    person = [self.signName,self.deviceName,self.modelname,self.data,self.imagesize,
              self.modelTime,self.imageTime,self.inferenceTime,
              self.fps,self.totalCost,self.result,self.trueTime]
    header = ['厂家名称', '芯片名称', '模型名称','推断日期','图片数目',
              '模型加载时间','图片加载时间','推断耗时',
              '推断速度','设备端总耗时','推断结果','平台侧总耗时']

    try:
        person_str = ",".join(str(i) for i in person)
        person_str = person_str.replace('\\x00', '')
        person_str = person_str.replace('\0', '')
        print(person_str)
        person = person_str.split(',')
        with open(path, 'a', newline='') as f:
            writer = csv.writer(f, dialect="excel")
            with open(path, 'r', encoding='gbk', newline="") as f2:
                reader = csv.reader(f2)
                if not [row for row in reader]:
                    writer.writerow(header)
                writer.writerow(person)
    except Exception as e:
        print("write history error:%s"%e)

def readHistory():
    list = []
    try:
        with open('history.csv', 'r', encoding='gbk') as file_obj:
            read = csv.reader((line.replace('\0','') for line in file_obj))
            i=0
            for r in read:
                if(i!=0):
                    # print(r)
                    list.append(r)
                i=i+1
            #print(list)
            return list
    except Exception as e:
        print("read history error:%s"%e)
        return list