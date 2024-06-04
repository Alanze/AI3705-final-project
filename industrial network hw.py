import numpy as np
#以下是各个组件的类定义
class workpiece:
    def __init__(self,color,pos) :
        self.color=color #记录工件颜色,0代表black，1代表metallic，2代表red
        self.pos=pos #记录工件位置，0代表在传送带前端位置，1代表在阻隔臂上，2代表被分类到chute1，3代表被分类到chute2，4代表被分类到chute3

class conveyor:
    front_pos=0
    def __init__(self,state=0) :
        self.state=state#记录正在运动与否，0表示静止，1表示运动
class detector:
    detect_pos=1
    def __init__(self):
        pass
    def detect(workpiece):
        if(workpiece.pos==1):
            return workpiece.color

class barrier_arm:
    def __init__(self,state=1):
        self.state=state#检测是否伸缩，0为收缩状态，1为伸展状态

class chute:
    def __init__(self,state=0) :
        self.state=state#检测是否装满，0为未装满，1为装满         
class sorting_arm:
    def __init__(self,state=0):
        self.state=state#检测是否伸缩，0为收缩状态，1为伸展状态
#以下是各个检测函数
def check_at_front(workpiece,conveyor):
    if(workpiece.pos == conveyor.front_pos):
        return True
    else:
        return False
    
def check_at_detector(workpiece,detector):
    if(workpiece.pos == detector.detect_pos):
        return True
    else:
        return False
def check_chute_isfull(chute):
    if chute.state==0:#检测滑槽是否装满，未满为False，装满为True
        return False
    else:
        return True
#以下为辅助表示函数
def print_color(color):
    real_color=" "
    if color == 0:
        real_color = "black"
    elif color == 1:
        real_color = "metallic"
    elif color == 2:
            real_color = "red"
    else:
        return "error!"
    return real_color
#以下为主程序
if __name__ == "__main__":
    workpiece1=workpiece(0,0)
    conveyor_belt=conveyor(0)
    check_converyor = check_at_front(workpiece1,conveyor_belt)
    if check_converyor:
        conveyor_belt.state=1#开始运动
        workpiece1.pos=1#运送至阻隔臂
    
    detector1=detector
    check_detector = check_at_detector(workpiece1,detector1)
    if check_at_detector:
        color=detector1.detect(workpiece1)#检测工件颜色
    barrier_arm1=barrier_arm(1)#初始为伸展状态
    chute1=chute(0)
    chute2=chute(0)
    chute3=chute(0)
    sorting_arm1=sorting_arm(0)#初始为收缩状态
    sorting_arm2=sorting_arm(0)
    # print(barrier_arm1.state)
    
    if color == 0:
        barrier_arm1.state=0#阻隔臂收缩
        chute3_flag = check_chute_isfull(chute3)
        if not chute3_flag:
            workpiece1.pos=4
    elif color == 1:
        sorting_arm2.state=1#分类臂2伸展
        barrier_arm1.state=0#阻隔臂收缩
        chute2_flag = check_chute_isfull(chute2)
        if not chute2_flag:
            workpiece1.pos=3
        sorting_arm2.state=0#分类臂2收缩
    elif color == 2:
        sorting_arm1.state=1#分类臂1伸展
        barrier_arm1.state=0#阻隔臂收缩
        chute3_flag = check_chute_isfull(chute3)
        if not chute3_flag:
            workpiece1.pos=2
        sorting_arm1.state=0#分类臂2收缩 
        conveyor_belt.state=0#传送带停止
        barrier_arm1.state=1#阻隔臂伸展


    