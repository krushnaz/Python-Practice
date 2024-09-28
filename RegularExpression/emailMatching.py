import re

email_pattern = re.compile(r"[\w\.]+@[\w\.]+\.com")
text = "this is email for support : support@gmail.com"
match = email_pattern.search(text)

print(match)
if match :
    print("email found :"+match.group())
else :
    print("email not found ")
    