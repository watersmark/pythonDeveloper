# управление потоком

# после первого выполненного блока, выходит их цикла
company = 'google.com'

if 'com' in company:
    print("good")
elif 'goog' in company:
    print('good1')
else:
    print('bad')

# аналог тернарного оператора
winner = 'Argentina' if 5 > 4 else 'Jamaica'
print(winner)

# оператор while
indexLoop = 0
while(indexLoop < 10):
    indexLoop += 1

# встроенный range
# иттерируемся по целым числам
# последнее число не входит
# range(start, stop, step)
for i in range(3):
    print(i, end=" ")

print()
for i in range(1, 10, 2):
    print(i, end=" ")

print()
for i in range(-5, -1, 1):
    print(i, end=" ")
