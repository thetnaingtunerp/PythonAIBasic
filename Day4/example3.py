# open()
# x =open("example4.py", 'w')

a =open("example4.py", 'w')
a.write("Mg Mg is Boy")
a.close()
r =open("example4.py", 'r')
print(r.read())