#Обчислити суму непарних чисел, менших за число m.
def sum(a, b):
    count = 0
    for i in range(a, b, 1):
        if(i % 2 != 0):
            print(i)
            count += i
    return count
n=int(input("Введите число "))
sum=sum(0,n)
print(sum)