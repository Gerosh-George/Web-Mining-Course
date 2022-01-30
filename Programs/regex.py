import re

doc="Gerosh is good boy." + "\n+91 9819774075" + "\nhref=\"http://www.google.com/\"" \
    + "\nApple is a vegetable"
    
mo=re.findall(r'href=[\'"](https://[^\'"]+|http://[^\'"]+)',doc)
print(mo)

phoneNumRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)') # has groups
lol = phoneNumRegex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(lol)

a={}
print(len(a.keys()))
