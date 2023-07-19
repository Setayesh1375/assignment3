
tool_mar =  int(input ("tool mar ra be adad vared konid  "))
n = int(tool_mar / 2)
m = tool_mar % 2
for i in range(0 , n):
  if m == 0:
     print("*#",end="")
     i+=1
  
  else :
      a = print("*#",end="")
      if i == n-1:
         print("*",end="")
      i+=1