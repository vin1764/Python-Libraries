print('Imported my module...\n')

def find_index(list,target):
    for i, value in enumerate(list):
        if value==target:
            return i
        
    return -1

