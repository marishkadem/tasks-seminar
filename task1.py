#Напишите программу, которая принимает 
#а вход цифру, обозначающую день недели, 
#и проверяет, является ли этот день выходным.

#Пример:

#                - 6 -> да
#                - 7 -> да
#                - 1 -> нет

day = int(input("введите день недели "))
if day > 5 and day < 8:
    print("Этот день - выходной")
elif day <= 5 and day > 0:
    print("Этот день - рабочий")
else:
    print("попробуйте ввести другой день")



