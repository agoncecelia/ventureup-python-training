our_list = [90, 30, 100, 2, 5, 200, 300, 450, 1300, 130, 7, 13, 21, 99, 303, 403]


def filter_number(list):
    odd_counter = 0
    odd_numbers = []
    even_counter = 0
    even_numbers = []

    for number in list:
        if number % 2 == 0:
            even_counter += 1
            even_numbers.append(number)
        else:
            odd_counter += 1
            odd_numbers.append(number)
        
    return_object = {
        "odd_counter": odd_counter,
        "odd_numbers": odd_numbers,
        "even_counter": even_counter,
        "even_numbers": even_numbers
    }
    return return_object

print(filter_number(our_list))