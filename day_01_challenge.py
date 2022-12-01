input_file = open('day_01_input.txt', 'r')
input_data = input_file.read()


def get_input_list_as_int_totals_per_elf():
    elf_list = input_data.split('\n\n')
    elf_list = [elf_hoard.split('\n') for elf_hoard in elf_list]

    int_elf_list = []

    for elf_hoard in elf_list:
        int_elf_list.append(sum([int(cal_val) for cal_val in elf_hoard]))
    
    return int_elf_list


def max_total_calories_carried_by_elf():
    return max(get_input_list_as_int_totals_per_elf())


def total_of_top_three_elves():
    input_list = get_input_list_as_int_totals_per_elf()
    return_total = 0
    for i in range(3):
        return_total += max(input_list)
        input_list.remove(max(input_list))

    return return_total


print(max_total_calories_carried_by_elf())
print(total_of_top_three_elves())
