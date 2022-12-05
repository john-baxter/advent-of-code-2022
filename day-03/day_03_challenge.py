input_file = open('day_03_input.txt', 'r')
input_data = input_file.read()
input_list = input_data.split('\n')
compartmentalised_list = [
    [string[:len(string)//2], string[len(string)//2:]] for string in input_list
]

priorities_dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f': 6,
    'g': 7,
    'h': 8,
    'i': 9,
    'j': 10,
    'k': 11,
    'l': 12,
    'm': 13,
    'n': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26,
    'A': 27,
    'B': 28,
    'C': 29,
    'D': 30,
    'E': 31,
    'F': 32,
    'G': 33,
    'H': 34,
    'I': 35,
    'J': 36,
    'K': 37,
    'L': 38,
    'M': 39,
    'N': 40,
    'O': 41,
    'P': 42,
    'Q': 43,
    'R': 44,
    'S': 45,
    'T': 46,
    'U': 47,
    'V': 48,
    'W': 49,
    'X': 50,
    'Y': 51,
    'Z': 52,
}


def find_common_letter(list_of_two_strings):
    for letter in list_of_two_strings[0]:
        if letter in list_of_two_strings[1]:
            return letter


def get_priority_of_common_letter(letter):
    return priorities_dict[letter]


def get_total_of_priorities():
    total = 0
    for pair in compartmentalised_list:
        total += get_priority_of_common_letter(
            find_common_letter(
                pair
            )
        )
    
    return total


print(get_total_of_priorities())
