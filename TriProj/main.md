You can also use the below function to get the list.

    import pprint

    def get_triangled_list(l, rows, typ='lower'):
        if type(l) is not list:
            print 'First parameter should be a list'
            return None

        if type(rows) is not int:
            print 'Second parameter should be a list'
            return None

        if not(typ == 'lower' or typ == 'upper'):
            print 'ERROR:', typ, 'is not allowed type'
            return None

        new_l = []
        length = len(l)
        num_items = ((rows-1) * rows)/ 2

        if length != num_items:
            print 'ERROR: ', 'There should be exactly', num_items, 'items for ', rows, 'rows, found', length, 'items.'
            return None

        if typ == 'upper':
            for i in range(rows):
                temp_l = [0]*(i+1) + [l.pop(0) for j in range(7-(i+1))] 
                new_l.append(temp_l)
        elif typ=='lower':
            for i in range(rows):
                temp_l = [l.pop(0) for j in range(i)] + [0]*(rows-i)
                new_l.append(temp_l)

        return new_l

    if __name__ == '__main__':
        l = [10,20,40,46,33,14,12,46,52,30,59,18,11,22,30,2,11,58,22,72,12]

        # TEST CASE 1 (LOWER TRIANGLE, default)
        new_lower = get_triangled_list(l, 7)
        pprint.pprint(new_lower)
        print('\n')

        # TEST CASE 2 (UPPER TRIANGLE, passing one more parameter)
        l = [10,20,40,46,33,14,12,46,52,30,59,18,11,22,30,2,11,58,22,72,12]
        new_upper = get_triangled_list(l, 7, 'upper')
        pprint.pprint(new_upper)

### Output &raquo;

    [[0, 0, 0, 0, 0, 0, 0],
     [10, 0, 0, 0, 0, 0, 0],
     [20, 40, 0, 0, 0, 0, 0],
     [46, 33, 14, 0, 0, 0, 0],
     [12, 46, 52, 30, 0, 0, 0],
     [59, 18, 11, 22, 30, 0, 0],
     [2, 11, 58, 22, 72, 12, 0]]


    [[0, 10, 20, 40, 46, 33, 14],
     [0, 0, 12, 46, 52, 30, 59],
     [0, 0, 0, 18, 11, 22, 30],
     [0, 0, 0, 0, 2, 11, 58],
     [0, 0, 0, 0, 0, 22, 72],
     [0, 0, 0, 0, 0, 0, 12],
     [0, 0, 0, 0, 0, 0, 0]]
