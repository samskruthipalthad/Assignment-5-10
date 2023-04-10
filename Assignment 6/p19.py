# From a list containing ints, strings and floats, make three lists to store them separately


mixed_list=[2,7.51,"Hello i am samskruthi",4,9.93,4,6]

seperate_list1=[]
seperate_list2=[]
seperate_list3=[]

for i in (mixed_list):
  if type(i)==int:
    seperate_list1.append(i)
  
  elif type(i)==float:
    seperate_list2.append(i)
  

  elif type(i)==str:
    seperate_list3.append(i)

    
print("int list is:",seperate_list1)
print("float list is:",seperate_list2)
print("string list is:",seperate_list3)