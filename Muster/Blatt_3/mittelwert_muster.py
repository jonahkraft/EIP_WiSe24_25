a = [7, 20, 5, -1, 3, 11, 32, 17, 42]

n = len(a)

s = 0
for i in a:
    s += i

my = s/n
print(my)

v = 0
for i in range(len(a)):
    v += (a[i] - my)**2

v /= n
print(v)
