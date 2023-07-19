array = []
number =  int(input ("tedad adad baraye moghayese ra vared namayid  "))
array_sort =[]
for i in range(0 , number):
  
    x = int(input("adad ra vared konid  "))
    array.append(x)
    i += 1

print("array = " , array)
array_sort = array.sort()   
print("array sort = ", array_sort ) 

x=len(array) 
i=0
for i in range(x):
    if array[i] == array_sort[i] :
        print("arraye moratab ast")
        
    else:
        print("arraye namoratab ast")
        
    i+=1           


