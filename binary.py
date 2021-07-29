
def binary():
    pass


l = ['']
for _ in range(15):
    # print(l)
    # print([int(num, 2) for num in l if len(num) > 0])
    # print()
    x = l.pop(0)
    l = l + [x + '0', x + '1']

print(l)
print([int(i, 2) for i in l])