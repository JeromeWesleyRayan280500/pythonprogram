print("Enter '0' for exit.");
dd= input("Enter any character: ");
if dd== '0':
    exit();
else:
    if((dd>='a' and dd<='z') or (dd>='A' and dd<='Z')):
    	print(dd, "is an alphabet.");
    else:
    	printc(dd, "is not an alphabet.");
