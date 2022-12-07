x = int(input()) # Ex. 1
y = int(input())

def division(x, y):
    c = x/y
    return c

res = division(x, y)
print(res)


numbers = input() # Ex. 2 (čísla se zadávají oddělená mezerou)
string_list_of_numbers = numbers.split()
int_list_of_numbers = []
for string_number in string_list_of_numbers:
    string_number_1 = int(string_number)
    int_list_of_numbers.append(string_number_1)

def sum_of_all_numbers(int_list_of_numbers):
    start = 0
    for n in int_list_of_numbers:
        start += n
    return start

res_3 = sum_of_all_numbers(int_list_of_numbers)
print(res_3)


string_1 = input() # Ex. 3
list_1 = list(string_1)
compare_list = (lambda list_1: print("big list") if len(list_1)>5 else print("small list"))
compare_list(list_1)
