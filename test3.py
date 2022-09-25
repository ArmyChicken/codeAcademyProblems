def count(sequence, item):
  total_count = 0
  for x in sequence:
    if x == item:
      total_count += 1
    else:
      continue
  return(total_count)

print(count([1, 2, 1, 1], 1))