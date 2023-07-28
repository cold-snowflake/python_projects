a = ['a', 'b', 'c', 'e', 'f', 'g', 'h']
int_list = list(range(101))

def binar_search(alph_array, item):
    first_pos = 0
    last_pos = len(alph_array)-1
    iterations = 0 


    while first_pos <= last_pos:
        center_value = (first_pos + last_pos) // 2
        iterations += 1
        if alph_array[center_value] == item:
            print(iterations)
            return alph_array.index(alph_array[center_value])
        else:
            if item < alph_array[center_value]:
                last_pos = center_value - 1
            else:
                first_pos = center_value +1
    print(iterations)
    return False
