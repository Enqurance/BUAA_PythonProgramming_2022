import re

a = "MG CL AR"
r = re.compile("[CL]*[AR]*[MG]*")
result = re.match(r, a)
print(result.group())
