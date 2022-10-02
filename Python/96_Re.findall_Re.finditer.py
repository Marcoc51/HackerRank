import re

exp = r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])'
m = re.findall(exp, input())
if not m:
    print(-1)
else:
    print(*m, sep='\n')
