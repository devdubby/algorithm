def binary_search(element, some_list):
  start_index = 0
  end_index = len(some_list) - 1
  
  while start_index <= end_index:
    search_index = (start_index + end_index) // 2
    if some_list[search_index] == element:
      return search_index
    elif some_list[search_index] > element:
      end_index = search_index - 1
    else:
      start_index = search_index + 1
  return None

print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))