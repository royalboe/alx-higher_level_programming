def search_replace(my_list, search, replace):
    dup = []
    for i in range(len(my_list)):
        if my_list[i] == search:
            dup.append(replace)
        else:
            dup.append(my_list[i])
    return dup
