from calendar import isleap
ini = int(input())
fim = int(input())
p = 0
for bix in range(ini, fim +1):
    if isleap(bix):
        print(bix)
        p += 1
print('bissextos: {}'.format(p))