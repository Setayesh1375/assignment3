number1 = int(input( "adad 1 ra vared konin : "))
number2 = int(input( "adad 2 ra vared konin : "))

maghsoom_alayh1=[]
maghsoom_alayh2 = []
for i in range (1 , number1+1):
  
   y = number1 % i
   if y == 0:
      maghsoom_alayh1.append(i)
      i+=1
   else:
      i+=1
print("maghsoom alayhaye adad 1 = " , maghsoom_alayh1)      

for i in range (1 , number2+1):
  
   y = number2 % i
   if y == 0:
      maghsoom_alayh2.append(i)
      i+=1
   else:
      i+=1
print("maghsoom alayhaye adad 2 = " , maghsoom_alayh2)

x=len(maghsoom_alayh1) 
y=len(maghsoom_alayh2)
i=1
j=1
moshtarak = []

for i in range(x):
      for j in range (y):
          
          if maghsoom_alayh1[i] == maghsoom_alayh2[j] :
                 moshtarak.append(maghsoom_alayh1[i]) 
                 j+=1
                 
          else:
             j+=1 
      i+=1                
print("maghsoom alayhe moshtarak = ", moshtarak) 
print("b.m.m = " , max(moshtarak))

