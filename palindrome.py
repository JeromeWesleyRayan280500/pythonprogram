m=int(input("Enter number:"))
temp=m
rev=0
while(m>0):
    dig=m%10
    rev=rev*10+dig
    m=m//10
if(temp==rev):
    print(" YesThe number is a palindrome!")
else:
    print(" NoThe number isn't a palindrome!")
