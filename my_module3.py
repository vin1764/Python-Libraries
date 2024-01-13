print('Imported my_module3...\n')

def find_index(list,target):
    for i, value in enumerate(list):
        if value==target:
            return i
        
    return -1