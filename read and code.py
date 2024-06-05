import re

def parse_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()

    sections = re.split(r'\*\*([A-Za-z ]+):\*\*', content)[1:]
    data = {sections[i].strip(): sections[i+1].strip() for i in range(0, len(sections), 2)}

    objects = data.get('Objects', '').split('\n')
    initial_conditions = data.get('Initial Conditions', '').split('\n')
    steps = data.get('Steps', '').split('\n')

    parsed_data = {
        'objects': [obj.strip() for obj in objects if obj.strip()],
        'initial_conditions': [cond.strip() for cond in initial_conditions if cond.strip()],
        'steps': [step.strip() for step in steps if step.strip()]
    }
    parsed_data = {
        'objects': [obj.strip('*') for obj in objects if obj.strip('*')],
        'initial_conditions': [cond.strip('*') for cond in initial_conditions if cond.strip('*')],
        'steps': [step.strip() for step in steps if step.strip()]
    }
    return parsed_data

def generate_class_code(parsed_data):
    code = ""
    code +=f"import os \n"
    code +=f"import numpy as np \n"
    # Generate classes for objects
    for obj in parsed_data['objects']:
        obj_name, attrs = obj.split('(', 1)
        obj_name = obj_name.strip().replace(' ', '')
        
        # print(obj_name)
        attrs = [attr.strip() for attr in attrs.split(',') if attr.strip()]
        
        code += f"class {obj_name}:\n"
        code += "    def __init__(self):\n"
        if 'color'  in attrs[0]:
            code += "        self.color = None\n"
        
        if 'states' in attrs[0]:
            code += "        self.state = None\n"
        
        else:
            for attr in attrs:
                code += f"        self.{attr.strip().replace(' ', '_').lower()} = None\n"
        code += "\n"

    # Generate System class and initial conditions
    code += "class System:\n"
    code += "    def __init__(self,input):\n"
    for cond in parsed_data['initial_conditions']:
        obj_name, state = cond.split(':')
        obj_name = obj_name.strip().replace(' ', '')
        state = state.strip().replace(' ', '_').lower()
        code += f"        self.{obj_name.lower()} = {obj_name}()\n"
        code += f"        self.{obj_name.lower()}.state = '{state}'\n"
    code += f"        self.workpiece.color = input"
    code += "\n"

    # Generate methods for steps
    step_counter = 1
    chute_1_num=0
    chute_2_num=0
    chute_3_num=0
    # print(len(parsed_data['steps']))
    for i in range(len(parsed_data['steps'])):
        str_number = str(step_counter)
        now_step=parsed_data['steps'][i]
        if now_step.startswith(str_number):
            code += f"    def step_{step_counter}(self):\n"
            step_counter+=1
            
        if now_step.startswith('* Case'):
            now_step=now_step.split(':')[1]
            now_step=now_step.strip()
            # print(now_step)
            if 'color =' in now_step:
                objective,feature = now_step.split('color =')
                objective=objective.strip()
                feature=feature.strip()
                code +=f"       if self.{objective.lower()}.color == '{feature}':\n"
                # print(feature)
        if now_step.startswith('+ Chute'):
            now_step=now_step.strip('+ ')
            if 'workpiece' in now_step:
                chute_corresponding=now_step.split(':')[0]
                
                # print(chute_corresponding)
                chute_num=chute_corresponding.split('Chute')[1].strip()
                objective='workpiece'
                # if(chute_num=='1'):
                #     chute_1_num+=1
                #     report_num=chute_1_num
                # elif(chute_num=='2'):
                #     chute_2_num+=1
                #     report_num=chute_2_num
                # elif(chute_num=='3'):
                #     chute_3_num+=1
                #     report_num=chute_3_num
                # code +=f"               #{chute_corresponding.lower()} store the workpiece and the num of workpiece in {chute_corresponding} is {report_num} \n"
                code +=f"               self.{objective.lower()}.state = 'stored in {chute_corresponding}' \n"
        if now_step.startswith('+ '):

            now_step=now_step.strip('+ ')
            now_step = now_step.replace(' ', '')
            # now_step=now_step.strip()
            objective,state=now_step.split(':')
            objective=objective.strip()
            # objective_no_space = objective.replace(' ', '')
            # print(type(objective_no_space))
            state=state.strip()
            print(objective)
            code +=f"               self.{objective.lower()}.state = '{state}' \n"        
        elif now_step.startswith('* '):
            case_steps = now_step.strip('* ')
            # print(case_steps)
            # print("yes")
            objective,change=case_steps.split(':')
            objective=objective.strip().replace(' ', '')
            change=change.strip().replace(' ', '_').lower()
            code += f"        self.{objective.lower()}.state = '{change}'\n"
            code += f"\n\n"
    # code +=f"    def simulation(self,input): \n"
    # code +=f"        self.workpiece.color = input\n"    
            # code += f"        # {case_steps.strip()}\n"
    # for step in parsed_data['steps']:
    #     str_number = str(step_counter)
    #     if step.startswith(str_number):
            
    #         code += f"    def step_{step_counter}(self):\n"
    #         step_counter+=1
    #         continue
    #     if step.startswith('* '):
    #         case_steps = step.strip('* ')
    #         print(case_steps)
    #         for case_step in case_steps:
    #             if case_step.strip():
    #                 code += f"        # {case_step.strip()}\n"
    #                 code += "        pass\n\n"
    #     if step.startswith('* Case'):
    #         continue
        
    #                 # code += f"    def step_{step_counter}(self):\n"
    #                 # code += f"        # {case_step.strip()}\n"
    #                 # code += "        pass\n\n"
    #                 # step_counter += 1
    #     else:
    #         code += f"    def step_{step_counter}(self):\n"
    #         code += f"        # {step}\n"
    #         code += "        pass\n\n"
    #         step_counter += 1
    code +=f"if __name__ == '__main__': \n"
    code +=f"   #Please input the color of workpiece \n"
    code +=f"   user_input=input('Please input the color') \n"
    code +=f"   simulation_system=System(user_input) \n"
    return code

def main(input_file, output_file):
    parsed_data = parse_file(input_file)
    code = generate_class_code(parsed_data)

    with open(output_file, 'w') as file:
        file.write(code)

if __name__ == "__main__":
    input_file = 'my_input_test.txt'  # 输入文件路径
    output_file = 'generated_classes_test.py'  # 输出文件路径
    test_data=parse_file(input_file)
    print(test_data['steps'])
    main(input_file, output_file)
