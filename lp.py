import random

l = int(input('введи какой ты игрок 1 или 2: '))

if l == 1:
    c = random.randrange(2,12)
    print("ваше число: ", c)
    c1 = random.randrange(2, 12)
    print("число бота: ", c1)
    if c1>c:
        print('вы проиграли')
    elif c>c1:
        print('вы выграли')
    elif c==c1:
        print('ничья')

elif l == 2:
    e = random.randrange(2, 12)
    print("число бота: ", e)
    e1 = random.randrange(2, 12)
    print("ваше число: ", e1)
    if e1 > e:
        print('вы выграли')
    elif e>e1:
        print('вы проиграли')
    elif e==e1:
        print('ничья')