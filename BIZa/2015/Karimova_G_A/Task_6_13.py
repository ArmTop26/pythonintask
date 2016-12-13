import random
print("Попробуйте угадать один из спутников Марса, который я загадала")
sputnic = ("Деймос,Фобос")
sp = random.choice(sputnic)
guess = input("Введите спутник:")
while (sp !=guess):
 print("Не угадал, попробуй еще раз")
 sp = input("Введите другой спутник:")
print("Вы угадали!")
input("Нажмите Enter, чтобы выйти")