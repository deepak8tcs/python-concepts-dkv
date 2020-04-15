# A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern.
# RegEx can be used to check if a string contains the specified search pattern.

import re
#in-built python module for regex

#Search the string to see if it starts with "The" and ends with "Spain":
txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

###-###-#### Format for a Phone Number

# phonenumber = "516-111-2222"
# regex = "\w{3}-\w{3}-\w{4}"
# if re.search(regex, phonenumber):
#     print("Valid phone number")
       
# else:
#     print("Invalid phone number")
        