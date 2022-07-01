s1 = ""
for i in s:
  if i.isupper():
    s1 += i.lower()
  else:
    s1 += i.upper()
return s1
