m=int(input("Enter the marks"))
if (m>100 or m<0):
    print("Invalid marks")
elif (m>=90 and m<=100):
    print("Grade A")        
elif(m>=80 and m<90):
    print("Grade B")    
elif(m>=70 and m<80):
    print("Grade C")
elif(m>=60 and m<70):
    print("Grade D")
else:
    print("Fail")


            