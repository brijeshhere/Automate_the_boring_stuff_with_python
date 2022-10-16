import re, pyperclip

text=str(pyperclip.paste())

phone=re.compile(r'''(
(\d{3})  #City Code
(\s|-|\.)+   #separators
(\d{8})     #last Eight number
)''',re.VERBOSE)
email=re.compile(r'''(
([a-zA-Z0-9_.+%-]+)
\@
([a-zA-Z0-9.-]+)
(\.[a-zA-Z]{2,5})
)''',re.VERBOSE)
foundph=phone.findall(text)
foundemail=email.findall(text)
i=len(foundph)
j=len(foundemail)
for each in range(0,i):
    print(foundph[each][0])
for each in range(0,j):
    print(foundemail[each][0])
