regex_pattern = r"[,.]"
# [] for a set of chars
# ,. to split when find , or .

import re
print("\n".join(re.split(regex_pattern, input())))
