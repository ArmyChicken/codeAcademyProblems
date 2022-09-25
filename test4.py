def remove_duplicates(list_num):
  list_dup = []
  for num in list_num:
    if num not in list_dup:
      list_dup.append(num)
    else:
      continue
  return list_dup

print(remove_duplicates([1, 1, 2, 2]))