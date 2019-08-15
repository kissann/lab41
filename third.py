#Задача 3
#У лінгвістичному класі із 10 учнів, кожен з них знає кілька мов. Виведіть
#на екран всі мови, які знає кожен учень та вкажіть учня, який знає найбільше мов. Дозволяється використовувати словники та множини.
import math
people={}
people['Ann'] = {'Russion', 'Ukraine','Germany','French'}
people['Olga'] = {'Russion', 'Ukraine','English'}
people['Sveta']= {  'Russion','Ukraine'}
people['Inna']={ 'Russion','Ukraine'}
people['Oleg']={  'Russion','Ukraine'}
people['Ivan']={  'Russion','Ukraine'}
print(people)
a=[]
mm = len(people['Oleg'])
name='Oleg'
for line in people:
   if mm<len(people[line]):
       mm=len(people[line])
       name=line
print("Ученик который знает больше языков в кол")
print(name)
print(len(people[name]))
mnoz = set(people[name])
for i in people:
    rez=mnoz.intersection(set(people[i]))
    mnoz=rez
print(rez)