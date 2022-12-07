input_file = open('day_06_input.txt', 'r')
input_data = input_file.read()


def find_marker(packet_len):
    # packet_len = packet_len
    start = 0
    fin = packet_len
    for char in input_data:
        if len(set(input_data[start:fin])) == packet_len:
            return fin

        start += 1
        fin += 1


# print(input_data[0:4])

print(find_marker(4))
print(find_marker(14))