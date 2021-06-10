import re
from collections import OrderedDict
from pprint import pprint

desc = "Create by CreateImage(i-0bcde089139cf6) for ami-767fdd03"
regex = r"^Create by CreateImage\((.*?\) for (.*?) "
matches = re.finditer(regex, desc, re.MULTILINE)
for matchNum, match in enumerate(matches):
    return match.groups()
return '',''
# s = parse_description(desc)
print(s)
