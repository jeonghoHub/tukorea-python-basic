import random
bigdata = []
nodata = []
for i in range(100):
    bigdata.append(random.choice(list(range(1, 34))))
    if i == 10:
        bigdata.append('\n')
print(bigdata)
for i in range(1, 34):
    if i not in bigdata:
        nodata.append(i)
print('존재하지 않는 값(들):', nodata)