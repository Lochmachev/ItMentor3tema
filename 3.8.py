# Найти все простые числа от 2 до 50.



# for i in range (2,50):
#     if i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 !=0 or i==2 or i==3 or i==5 or i==7 :
#         print(i)
# работает в диапозоне до 100



n = int(input("Введите число : "))
a = []
for i in range(2, n+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        a.append(i)
print (a)
