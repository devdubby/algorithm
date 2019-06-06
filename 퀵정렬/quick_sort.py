def swap_elements(my_list, index1, index2):
  my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

def partition(my_list, start, end):
  # 코드를 작성하세요.
  p = end
  i = start
  b = start
  while i < p:
    if my_list[i] <= my_list[p]:
      swap_elements(my_list, i, b)
      b += 1
    i += 1
  swap_elements(my_list, p, b)
  return b

def quicksort(my_list, start, end):
  if end - start < 1:
    return
  pivot_index = partition(my_list, start, end)
  quicksort(my_list, start, pivot_index - 1)
  quicksort(my_list, pivot_index + 1, end)
    

list1 = [1, 3, 5, 7, 9, 11, 13, 11]
quicksort(list1, 0, len(list1) - 1)
print(list1)

list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
quicksort(list2, 0, len(list2) - 1)
print(list2)