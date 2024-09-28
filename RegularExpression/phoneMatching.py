import re 
phone_pattern = re.compile("(\d{3})-(\d{4})-(\d{3})")
text = "this is my phone number : 123-4567-890"
match = phone_pattern.search(text)

print(match.group())
