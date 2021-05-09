import re

s = '[bcdfghjklmnpqrstvwxyz]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))