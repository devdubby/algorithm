def selection_sort(list):
  for i in range(len(list) - 1):
    min_index = i
    min = list[min_index]
    for j in range((i + 1), len(list)):
      if list[j] <= min:
        min_index = j
        min = list[min_index]
    list[i], list[min_index] = list[min_index], list[i]
  return list

print(selection_sort([10, 8, 7, 2, 9, 1, 4]))