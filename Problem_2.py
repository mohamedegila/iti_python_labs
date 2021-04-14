 
#Problem #2 remove duplicates from given list 

def unique_list(elements):
  '''
  Function to remove duplicates from given list 
  '''
  single_list = []
  for element in elements:
    if element not in single_list:
      single_list.append(element)
  return single_list

elements = [7, 7, 8, 8, 5]
print("List Before:  " , elements)
print("============================") 
print("List After:  " , unique_list(elements))