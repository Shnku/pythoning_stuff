def add(a,b):
  return a+b
  
list1=[2,3,7,9]
list2=[5,7,9,6,89]

output=list(map(add,list1,list2))
print(output)