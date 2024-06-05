import os 
import numpy as np 
class ConveyorBelt:
    def __init__(self):
        self.state = None

class BarrierArm:
    def __init__(self):
        self.state = None

class SortingArm1:
    def __init__(self):
        self.state = None

class SortingArm2:
    def __init__(self):
        self.state = None

class Chute1:
    def __init__(self):
        self.state = None

class Chute2:
    def __init__(self):
        self.state = None

class Chute3:
    def __init__(self):
        self.state = None

class Workpiece:
    def __init__(self):
        self.color = None
        self.state = None

class System:
    def __init__(self,input):
        self.conveyorbelt = ConveyorBelt()
        self.conveyorbelt.state = 'stopped'
        self.barrierarm = BarrierArm()
        self.barrierarm.state = 'extended'
        self.sortingarm1 = SortingArm1()
        self.sortingarm1.state = 'retracted'
        self.sortingarm2 = SortingArm2()
        self.sortingarm2.state = 'retracted'
        self.chute1 = Chute1()
        self.chute1.state = 'not_full'
        self.chute2 = Chute2()
        self.chute2.state = 'not_full'
        self.chute3 = Chute3()
        self.chute3.state = 'not_full'
        self.workpiece = Workpiece()
        self.workpiece.state = 'located_at_the_front_of_the_conveyor_belt'
        self.workpiece.color = input
    def step_1(self):
        self.conveyorbelt.state = 'running'


        self.workpiece.state = 'moving_to_barrier_arm'


    def step_2(self):
        self.barrierarm.state = 'detects_workpiece'


    def step_3(self):
       if self.workpiece.color == 'black':
               self.barrierarm.state = 'retracted' 
               self.workpiece.state = 'stored in Chute 3' 
       if self.workpiece.color == 'metallic':
               self.barrierarm.state = 'retracted' 
               self.sortingarm2.state = 'extended' 
               self.workpiece.state = 'stored in Chute 2' 
               self.sortingarm2.state = 'retracted' 
       if self.workpiece.color == 'red':
               self.barrierarm.state = 'retracted' 
               self.sortingarm1.state = 'extended' 
               self.workpiece.state = 'stored in Chute 1' 
               self.sortingarm1.state = 'retracted' 
    def step_4(self):
        self.conveyorbelt.state = 'stopped'


    def step_5(self):
        self.barrierarm.state = 'extended'


if __name__ == '__main__': 
   #Please input the color of workpiece 
   user_input=input('Please input the color') 
   simulation_system=System(user_input) 
