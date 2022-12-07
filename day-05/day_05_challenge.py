import re
from day_05_input_1 import start_position as start_position


input_file = open('day_05_input_2.txt', 'r')
input_data = input_file.read()
input_data = [re.findall(r'\d+', input_line) for input_line in input_data.split('\n')]
input_ints = [(int(a), int(b), int(c),) for [a, b, c] in input_data]


class SupplyStacks():
    def __init__(self):
        self.crate_stacks = start_position
        self.instruction_list = input_ints
        self.elf_message = []


    def move_one_crate(self, origin, target):
        self.crate_stacks[target].append(
            self.crate_stacks[origin].pop()
        )


    def complete_one_line_of_instruction(self, times, origin, target):
        for i in range(times):
            self.move_one_crate(
                origin, target
            )

    
    def do_all_the_lines_of_instructions(self):
        for single_line in self.instruction_list:
            times = single_line[0]
            origin = single_line[1] - 1
            target = single_line[2] - 1
            self.complete_one_line_of_instruction(
                times, origin, target
            )


    def read_tops_of_stacks(self):
        for stack in self.crate_stacks:
            self.elf_message.append(stack[-1])


supply_stacks = SupplyStacks()
supply_stacks.do_all_the_lines_of_instructions()
supply_stacks.read_tops_of_stacks()
print("".join(supply_stacks.elf_message))
