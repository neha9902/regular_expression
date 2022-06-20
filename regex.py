import re

mystr='''Lorem Ipsum is simply dummy text of 
the printing and typesetting industry. Lorem Ipsum 
has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a 
galley of type and scrambled it to make a type 
specimen book. It has survived not only five centuries, 
but also the leap into electronic typesetting, remaining 
essentially unchanged. It was popularised in the 1960s 
with the release of Letraset sheets containing Lorem Ipsum 
passages, and more recently with desktop publishing software 
like Aldus PageMaker including aiiiiiiii versions of Lorem Ipsum. phone no - 1422354-13224
+919856478734
'''


#  META CHARACTER
# patt = re.compile(r'the')

# matches = patt.finditer(mystr)

# for match in matches:
#     print(match)


#patt = re.compile(r'.set')
# patt = re.compile(r'..set')

# matches = patt.finditer(mystr)

# for match in matches:
#     print(match)

#patt = re.compile(r'^Lorem')

#patt = re.compile(r'Ipsum$')


#patt = re.compile(r'ai*')

#patt = re.compile(r'a*i*')
#patt = re.compile(r'ai+')
#patt = re.compile(r'ai{2}')



#patt = re.compile(r'(ai){2}')
#patt = re.compile(r'(ai){1}|t')

#patt = re.compile(r'(ai){1}|is')



# SPECIAL SEQUENCE

#patt = re.compile(r'\ALorem')

#patt = re.compile(r'\band')

#patt = re.compile(r'rem\b')


#patt = re.compile(r'\d{7}-\d{5}')


patt = re.compile(r'.+91\d{10}')
matches = patt.finditer(mystr)

for match in matches:
    print(match)
    
