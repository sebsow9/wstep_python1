max_N = int(input("Maksymalna liczba pierwsza: "))
list_of_numbers = [x for x in range(2, max_N + 1)]
pow_max_N = pow(max_N, 1/2)

def deleting_numbers(element, my_list, maximum):
    iteration = 2
    secondary_list = my_list
    while element * iteration <= maximum:
        for i in my_list:
            if (element * iteration) == i:
                del secondary_list[secondary_list.index(i)]
        iteration += 1
    return secondary_list

def recursion(maximum, my_list, N):
    i = 0
    while my_list[i] <= maximum:
        my_list = deleting_numbers(my_list[i], my_list, N)
        i += 1
    return my_list

print(recursion(pow_max_N, list_of_numbers, max_N))

