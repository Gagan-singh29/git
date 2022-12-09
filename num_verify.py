m = str(input("Enter the mobile no="))
length = len(m)
if length==10:
   if m.isdigit()==True:
      print(m,'is valid mobile number')
   else:
      print("mobile number must contain digit only")    
else:
    print(m,"is invalid mobile number")    
