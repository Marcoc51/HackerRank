from cmath import phase

cmx = complex(input())
print(f"%.3f" % abs(cmx))
print(f"%.3f" % phase(cmx))
