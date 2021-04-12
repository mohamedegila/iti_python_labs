#problem #3 dividing a string into two halves
def splitter(str):
    '''
    Function to split a given string into two halves
    '''
    mid = (len(str)+1)//2
    return str[:mid], str[mid:]

def front_back(a,b):
    '''
    Function to combine two given strings
    '''
    a_front, a_back = splitter(a)
    b_front, b_back = splitter(b)
    return "".join((a_front, b_front, a_back, b_back))

print(front_back("Mohammed", "Web"))