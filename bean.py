class Ruquest():
    HELLO = 0x01
    TEST = 0x10
    STATE = 0x03
    RESULT = 0x11
class Response():
    HELLO = 0x02
    TEST = 0x80
    STATE = 0x04
    RESULT = 0x20
    REJECT = 99
    CLOSE = 98
    TIMEOUT = 97

import struct
def toB(data):
    if isinstance(data, int):
        return  struct.pack('>i', data)
    elif isinstance(data, float):
        return  struct.pack('>f', data)
    elif isinstance(data, str):
        return data.encode('utf-8')

def to1b(data):
    return struct.pack('>b', data)

#报文类型、厂家名称长度、厂家名称、设备名称长度。设备名称
class helloInfo:
    def __init__(self):
        self.type = b''
        self.signNameSize = 0
        self.signName = ""
        self.deviceNameSize = 0
        self.deviceName = ""

def getHello(data):
    h = helloInfo()
    h.type = data[0]
    h.signNameSize = int(data[1])
    h.signName = data[2:2+h.signNameSize].decode()
    h.deviceNameSize = int(data[2+h.signNameSize])
    h.deviceName = data[2+h.signNameSize+1:2+h.signNameSize+1+h.deviceNameSize].decode()
    return h

def setHello(type,sname,dname):
    helloInfoByte = to1b(type)+ to1b(len(sname)) + toB(sname) + to1b(len(dname)) + toB(dname)
    return helloInfoByte

#报文类型、请求编号、任务类型、模型路径长度、模型路径、数据集路径长度、数据集路径
class testInfo:
    def __init__(self):
        self.type = b''
        self.id = 1000
        self.missionType = b''
        self.modelPathSize = 0
        self.modelPath = ""
        self.dataPathSize = 0
        self.dataPath = ""

def getTestInfo(data):
    t = testInfo()
    t.type = data[0]
    t.id =  struct.unpack('>i', data[1:5])[0]
    t.missionType = data[5]
    t.modelPathSize = int(data[6])
    t.modelPath = data[7:7+t.modelPathSize].decode()
    t.dataPathSize = int(data[7+t.modelPathSize])
    t.dataPath = data[7+t.modelPathSize+1:7+t.modelPathSize+1+t.dataPathSize].decode()
    return t

def setTestInfo(type,id,missionType,modelPath,dataPath):
    testInfoByte = to1b(type) + toB(id)+to1b(missionType)+to1b(len(modelPath)) + toB(modelPath) + to1b(len(dataPath)) + toB(dataPath)
    return testInfoByte

#报文类型、请求编号、指令状态
class testCallBackInfo:
    def __init__(self):
        self.type = b''
        self.id = 1000
        self.state = 0

def getTestCallBackInfo(data):
    tc = testCallBackInfo()
    tc.type = data[0]
    tc.id = struct.unpack('>i', data[1:5])[0]
    tc.state = data[5]
    return tc

def setTestCallBackInfo(type,id,state):
    testCallBackInfoByte = bytes([type]) + toB(id) + toB(state)
    print(testCallBackInfoByte)
    return testCallBackInfoByte

#报文类型、设备状态
class StateInfo:
    def __init__(self):
        self.type = b''
        self.state = 0

def setStateInfo(type,state):
    stataInfoByte = to1b(type)  + toB(state)
    return stataInfoByte

def getStateInfo(data):
    s = testCallBackInfo()
    s.type = data[0]
    s.state = data[1]
    return s

def setAskResultInfo(type,id):
    askResultByte = to1b(type)  + toB(id)
    return askResultByte

#报文类型、请求编号、任务类型、推断图片数
class ResultInfo:
    def __init__(self):
        self.type = b''
        self.id = 1000
        self.missionType = b''
        self.imageSize = 0



def getResultInfo(data):
    r = ResultInfo()
    r.type = data[0]
    r.id = struct.unpack('>i', data[1:5])[0]
    r.missionType = data[5]
    r.imageSize =  struct.unpack('>i', data[6:10])[0]
    return r

#图片编号、置信度、分类号
class ClassifyContentInfo:
    def __init__(self):
        self.no = 0
        self.score1 = 0.99
        self.index1 = 1
        self.score2 = 0.99
        self.index2 = 1
        self.score3 = 0.99
        self.index3 = 1
        self.score4 = 0.99
        self.index4 = 1
        self.score5 = 0.99
        self.index5 = 1


def setClassifyResultInfo(type,id,missionType,imageSize,modelTime,imageTime,inferenceTime):
    stataInfoByte =  to1b(type) + toB(id) + to1b(missionType)+ toB(imageSize)
    for i in range(1000):
        contentByte = toB(i)
        for x in range(5):
            contentByte = contentByte  + toB(x) + toB(0.99)
        stataInfoByte = stataInfoByte + contentByte
    stataInfoByte = stataInfoByte + toB(modelTime)+ toB(imageTime)+ toB(inferenceTime)
    return stataInfoByte

def getClassifyContentInfo(data):
    c = ClassifyContentInfo()
    c.no = struct.unpack('>i', data[0:4])[0]
    c.index1 = struct.unpack('>i', data[4:8])[0]
    c.score1 = struct.unpack('>f', data[8:12])[0]
    c.index2 = struct.unpack('>i', data[12:16])[0]
    c.score2 = struct.unpack('>f', data[16:20])[0]
    c.index3 = struct.unpack('>i', data[20:24])[0]
    c.score3 = struct.unpack('>f', data[24:28])[0]
    c.index4 = struct.unpack('>i', data[28:32])[0]
    c.score4 = struct.unpack('>f', data[32:36])[0]
    c.index5 = struct.unpack('>i', data[36:40])[0]
    c.score5 = struct.unpack('>f', data[40:44])[0]
    return c

#模型加载时间、图片加载时间、推断耗时
class timeInfo:
    def __init__(self):
        self.modelTime = 1.99
        self.imageTime = 2.99
        self.inferenceTime = 3.99

def setTimeInfo(modelTime,imageTime,inferenceTime):
    timeInfoByte = toB(modelTime)  + toB(imageTime)+ toB(inferenceTime)
    return timeInfoByte

def getTimeInfo(data):
    print(data)
    t = timeInfo()
    t.modelTime = struct.unpack('>f', data[0:4])[0]
    t.imageTime = struct.unpack('>f', data[4:8])[0]
    t.inferenceTime = struct.unpack('>f', data[8:12])[0]
    return t

#图片编号、box数目
class DetectInfo:
    def __init__(self):
        self.no = 0
        self.num = 100

#分类号、置信度、坐标x、坐标y、宽、高
class DetectContentInfo:
    def __init__(self):
        self.index = 1
        self.score = 0.99
        self.x = 0.1
        self.y = 0.2
        self.width = 1.1
        self.height = 1.1



def setDetectResultInfo(type,id,missionType,imageSize,num,modelTime,imageTime,inferenceTime):
    stataInfoByte =  to1b(type) + toB(id) + to1b(missionType)+ toB(imageSize)
    for i in range(1000):
        contentByte = toB(i) +toB(num)
        for x in range(num):
            contentByte = contentByte  + toB(x) + toB(0.99) +toB(0.1) + toB(0.2) +toB(1.1) + toB(1.1)
        stataInfoByte = stataInfoByte + contentByte
    stataInfoByte = stataInfoByte + toB(modelTime)+ toB(imageTime)+ toB(inferenceTime)
    return stataInfoByte

def getDetectInfo(data):
    d = DetectInfo()
    d.no = struct.unpack('>i', data[0:4])[0]
    d.num = struct.unpack('>i', data[4:8])[0]
    return d

def getDetectContentInfo(data):
    dc = DetectContentInfo()
    dc.index = struct.unpack('>i', data[0:4])[0]
    dc.score = struct.unpack('>f', data[4:8])[0]
    dc.x = struct.unpack('>f', data[8:12])[0]
    dc.y = struct.unpack('>f', data[12:16])[0]
    dc.width = struct.unpack('>f', data[16:20])[0]
    dc.height = struct.unpack('>f', data[20:24])[0]
    return dc