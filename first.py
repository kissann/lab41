#Реалізуйте введення даних у один рядок до двовимірного масиви цілих чисел. Забезпечте коректність введення даних у двовимірний список.
# Перевірте, чи даний двовимірний список цілих чисел має вертикальну вісь симетрії.
'''x = print("Введите ряды целых чисел через пробел для заполнения таблицы. Когда закончите нажмите 0: ")
a=[]
i=0
while True:
    n=input("Ряд ")
    a.append([])
    for c in list(n):
        print(c)
        c=int(c)
        if c==0:
            break
        else:
            print(i)
            a[i].append(c)
            i=i+1
            print(a)
print(a)'''
n = int(input("Enter number rows :"))
m = int(input("Enter number cloums :"))
num_lst = []
i=0
for i in range(n):
    num_lst.append([int(j) for j in input("Enter a series of numbers across the space ").split()])
    print(len(num_lst[i]))

if len(num_lst[i])!=m:
    print("Количество столбиков вышло за предел")
i=i+1
for i in num_lst:
    print(i)


