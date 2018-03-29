from Xel import *

radius=5
ra=6
org = Xel()
result=""
for i in range(-radius, radius+1):
    for j in range(abs(i)):
        result += " "
    for j in range(ra):
        if org.exa == Exa(i,i,i):
            result += "o "
        else:
            result += ". "
    if i < 0:
        ra += 1
    else:
        ra -= 1
    result += "\n"
print(result)