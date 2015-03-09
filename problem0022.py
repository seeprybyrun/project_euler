f = open('p022_names.txt','r')
names = f.read()
f.close()

names = names.split(',')
names = [n.strip('"') for n in names]
names.sort()

total = 0
for i,name in enumerate(names):
    s = sum([ ord(c)-64 for c in name ])
    total += s * (i+1)

print total
