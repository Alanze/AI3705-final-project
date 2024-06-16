import os 
import numpy as np 

import webbrowser
from flask import Flask, render_template, request, jsonify

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

app = Flask(__name__)
@app.route('/show')
def show():
    # Pass the state to HTML file
    return render_template('show.html')

@app.route('/process_case', methods=['POST'])
def process_case():
    case = request.form['animationCase']
    color_map = {'case1': 'black', 'case2': 'metallic', 'case3': 'red'}
    color = color_map.get(case, 'black')  # Default to 'black' if case is not found
    print(f"The color is: {color}")
    system = System(color)
    print(f"Initial workpiece state: {system.workpiece.state}")
    system.step_1()
    system.step_2()
    system.step_3()
    system.step_4()
    system.step_5()
    print(f"Final workpiece state: {system.workpiece.state}")
    return jsonify({'result': f'Workpiece stored in {system.workpiece.state}'})

if __name__ == '__main__':
    
    webbrowser.open('http://127.0.0.1:8080/show')
    app.run(debug=True, port=8080)
