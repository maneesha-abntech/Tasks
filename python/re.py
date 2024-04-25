
import re

mobile =input('enter any mobile number')

m = re.fullmatch('[6-9][0-9]{9}', mobile)
if m==None:
    print("Valid mobile number")
else:
    print("Invalid mobile number")
