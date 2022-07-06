import re
#open Actual data file name
hand = open('regex_sum_1594825.txt')
sum=0
for line in hand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    for y in x:
        sum=sum+int(y)
print(sum)
