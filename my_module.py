
print('Imported my_module...')

test = 'Test String'


def find_index(to_search, target):
    """find the index of a value in a sequence"""
    for i, value in enumerate(to_search):   # to_search is the list
        if value == target:
            return i

    return -1