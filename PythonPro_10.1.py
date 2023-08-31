import re

a = 'Raawr, RRR, raawr, asdasd, Rbbbbbbr'

match = re.findall(r'[R][b]+[r]', a)
print(match)