def insert_sorted(list2, value):
    for i in range(len(list2)):
        if value <= list2[i]:
            return list2[:i] + [value] + list2[i:]
    return list2 + [value]