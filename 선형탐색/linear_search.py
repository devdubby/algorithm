
def linear_search(element, some_list):
  for i, value in enumerate(some_list):
    if element == value:
      return i
            
print(linear_search(2, [2, 3, 5, 7, 11]))