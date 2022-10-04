regex_pattern = r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$"

"""
  1.M{0,3} specifies the thousands section. 
 
  2.(CM|CD|D?C{0,3}) is for the hundreds section. 
 
  3.(XC|XL|L?X{0,3}) is for the tens section. 
 
  4.(IX|IV|V?I{0,3}) is the units section. 
"""

import re
print(str(bool(re.match(regex_pattern, input()))))
