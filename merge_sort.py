arr = [2,8,5,3,9,4,1]


def merge(a, b):
    c = []

    while len(a) >= 1 and len(b) >= 1:

        if a[0] < b [0]:
            c.append(a[0])
            a.pop(0)
        else:
            c.append(b[0])
            b.pop(0)
    
    # a or b is empty

    while len(a) >= 1:
        c.append(a[0])
        a.pop(0)
    
    while len(b) >= 1:
        c.append(b[0])
        b.pop(0)
    
    print(c)
    return c

def merge_sort(array):
    length = len(array)

    if length == 1:
        return array
    
    array_one = array[0 : length // 2]
    array_two = array[(length // 2) : ]

    array_one = merge_sort(array_one)
    array_two = merge_sort(array_two)

    return merge(array_one, array_two)


print(merge_sort(arr))