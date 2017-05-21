def fib(x):
  i , j = 1 , 1
  q = 2
  while len(str(i)) < x:
    i , j = i + j , i
    q = q + 1
  return q
  
print fib(1000)