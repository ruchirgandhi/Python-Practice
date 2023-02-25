import re
text = "Agent's phone number is 408-555-1234, other phone number is 555-123-9876"

pattern = r"\d{3}-\d{3}-\d{4}"

print(pattern in text)

res = re.search(pattern,text)

print(res)
print(res.group())
print(re.findall(pattern,text))



for match in re.finditer(pattern,text):
    print(match.group())




# OR operation


text = " THIS is my dog"

print(re.search(r'cat| dog', text))

# wildcard (.) wild card

text = " the cat in the hat with the splat"

print(re.findall(r"(...at)",text))

# starts with ^


text = "1 is the number"

print(re.findall(r"(^\d)",'1 is a number'))

#ends with $

print(re.findall(r"(\d$)","the number is 20"))

# Exclude

print(re.findall(r"[^\d]+",'The number is 2100'))

text = " there are 3 numbers 34 inside 5 this sentence"

list = (re.findall(r'[^\d ]+', text))
print(' '.join(list))

text=  "this is so much fun! 3 i would rather do it again, and again !! :)"

list = (re.findall(r"[^\d! ,:)]+",text))
new= ' '.join(list)

print(new)

text = " only find the hypen-words in this sentenace, but yu know how long-ish it will take"

print(re.findall(r"[\w]+-[\w]+", text))

new = (re.search(r"[\w]+-[\w]+", text))

print(new.group(0))