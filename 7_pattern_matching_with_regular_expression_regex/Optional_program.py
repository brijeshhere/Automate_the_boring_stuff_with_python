import re, pyperclip

text=str(pyperclip.paste())

ssn_ccn=re.compile(r'\d{3}-\d{2}-\d{4},|\d{4}\s\d{4}\s\d{4}\s\d{4},')
_date=re.compile(r'(\d+)/(\d+)/(\d{4})')
newtext=ssn_ccn.sub('',text)
print(_date.sub(r'\3/\1/\2',newtext))
