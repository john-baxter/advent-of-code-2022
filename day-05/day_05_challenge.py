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


    def complete_one_line_of_instruction_v9000(self, times, origin, target):
        for i in range(times):
            self.move_one_crate(
                origin, target
            )


    def complete_one_line_of_instruction_v9001(self, crates, origin, target):
        crates *= -1
        self.crate_stacks[target] += self.crate_stacks[origin][crates:]
        self.crate_stacks[origin] = self.crate_stacks[origin][:crates]


    
    def do_all_the_lines_of_instructions_v9000(self):
        for single_line in self.instruction_list:
            times = single_line[0]
            origin = single_line[1] - 1
            target = single_line[2] - 1
            self.complete_one_line_of_instruction_v9000(
                times, origin, target
            )


    def do_all_the_lines_of_instructions_v9001(self):
        for single_line in self.instruction_list:
            crates = single_line[0]
            origin = single_line[1] - 1
            target = single_line[2] - 1
            self.complete_one_line_of_instruction_v9001(
                crates, origin, target
            )


    def read_tops_of_stacks(self):
        for stack in self.crate_stacks:
            self.elf_message.append(stack[-1])


supply_stacks_part_1 = SupplyStacks()
supply_stacks_part_1.do_all_the_lines_of_instructions_v9000()
supply_stacks_part_1.read_tops_of_stacks()
print("".join(supply_stacks_part_1.elf_message))

supply_stacks_part_2 = SupplyStacks()
supply_stacks_part_2.do_all_the_lines_of_instructions_v9001()
supply_stacks_part_2.read_tops_of_stacks()
print("".join(supply_stacks_part_2.elf_message))
