def list_sum(num_list):
    if len(num_list) == 0:
        return 0
    return num_list[0] + list_sum(num_list[1:])
print(list_sum([1, 2, 3, 5, 10]))