class Sort:

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def merge_sort(array):
        """
        Time complexity: O(nLogn)
        Space complexity: O(n)
        """

        def merge(a,b):
            c = []
            while len(a) >= 1 and len(b) >= 1:
                if a[0] < b[0]:
                    c.append(a[0])
                    a.pop(0)
                else:
                    c.append(b[0])
                    b.pop(0)
            
            while len(a) >= 1:
                c.append(a[0])
                a.pop(0)
            
            while len(b) >= 1:
                c.append(b[0])
                b.pop(0)

            return c
        

        length = len(array)

        if length == 1:
            return array

        a = array[:length // 2]
        b = array[length // 2:]

        a = Sort.merge_sort(a)
        b = Sort.merge_sort(b)


        return merge(a, b)
