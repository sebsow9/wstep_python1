max_N = int(input("Maksymalna liczba pierwsza: "))
list_of_numbers = [x for x in range(2, max_N + 1)]
pow_max_N = pow(max_N, 1/2)
i = 0
def deleting_numbers(element, my_list, maximum, max_pow):
    global i

    iteration = 2
    secondary_list = my_list
    if element <= max_pow:
        while element * iteration <= maximum:
            for g in my_list:
                if (element * iteration) == g:
                    del secondary_list[secondary_list.index(g)]
            iteration += 1
        i+=1
        deleting_numbers(my_list[i], secondary_list, maximum, pow_max_N)
    
    return secondary_list



print(deleting_numbers(list_of_numbers[0],list_of_numbers, max_N, pow_max_N))

