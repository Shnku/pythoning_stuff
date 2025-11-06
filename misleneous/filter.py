def positive(a):
  if a > 0:
    return a;


lst = [9,4,-8,-5,-8,4,8,5]
out = list(filter(positive,lst))
print(out)