input_file = open('day_04_input.txt', 'r')
input_data = input_file.read()
input_list_pairs = input_data.split('\n')
input_list_pairs = [pair.split(',') for pair in input_list_pairs]

input_list_pairs = [
    [
        [
            int(number) for number in minmax.split('-')
        ] for minmax in elf_pair
    ] for elf_pair in input_list_pairs
]


def fully_contained_ranges():
    total = 0
    for range_pair in input_list_pairs:
        if range_pair[0][0] <= range_pair[1][0] and range_pair[0][1] >= range_pair[1][1] \
        or range_pair[1][0] <= range_pair[0][0] and range_pair[1][1] >= range_pair[0][1]:
            total += 1
    return total


def is_a_between_b_and_c(a, b, c):
    return a >= b and a <= c


def overlapping_ranges():
    total = 0
    for range_pair in input_list_pairs:
        if is_a_between_b_and_c(range_pair[0][0], range_pair[1][0], range_pair[1][1]):
            total += 1
            continue
        if is_a_between_b_and_c(range_pair[0][1], range_pair[1][0], range_pair[1][1]):
            total += 1
            continue
        if is_a_between_b_and_c(range_pair[1][0], range_pair[0][0], range_pair[0][1]):
            total += 1
            continue
        if is_a_between_b_and_c(range_pair[1][1], range_pair[0][0], range_pair[0][1]):
            total += 1
            continue
    return total

print(overlapping_ranges())
# print(fully_contained_ranges())
# is_a_between_b_and_c()