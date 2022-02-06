x = int(input())
y = int(input())
if x > y:
    print('Nenhuma tabuada no intervalo!')
while x <= y:
    for z in range(1, 11):
        r = x * z
        print(f'{x} x {z} = {r}')
    x += 1
    print('----------')
