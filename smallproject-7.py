# make a program that displays several numbers

# loop


def loop(x):
    var = 0
    for i in range(x):
        var = var + i
    return var

print(loop(10))

for i in range(100):
    print(i)

for i in['master', 'kung', 'foo', 'plain', 'Jane']:
    if 'a' in i:
        continue
    print(i)
        
