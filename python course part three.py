import re

text = " random string. ks24175@gmail.com . some more random text. your_name.8-8@company.net"

pattern = re.compile("[a-zA-Z0-9\. \-_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+")

result = pattern.findall(text)

print(result)