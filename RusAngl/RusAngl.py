from Mymodule import *

rus=[]
ang=[]
rus=loef('rus.txt',rus)
#print(rus)
ang=loef('ang.txt',ang)
#print(ang)

print("Добро пожаловаться в Русско-Английский переводчик")
while True:
    language=input("С какого на какой язык вы хотите выполнить перевод?\nДобавить новое слово - Y\nПеревести слово - T\nУвидеть список слов - N\nНашел ошибку - V\nПроговорить слово - R\nПроверка знаний - L\nВыбери вариант: ")
    print()
    if language.upper()=="Y":
        rus=newWord("rus.txt", input("Новое слово(Рус): "))
        ang=newWord("ang.txt", input("Перевод(Англ): "))
    elif language.upper()=="N":
        for i in range(len(rus)):
            print(rus[i]+"-"+ang[i])
    elif language.upper()=="T":
        translate(rus,ang)
    elif language.upper()=="V":
        error(rus,"rus.txt", ang,"ang.txt")
    elif language.upper()=="R":
        keel=input("На каком языке?(ru,et,en)")#ru et en
        sona=input("Слово:")
        heli(sona,keel)
    elif proverka.upper()=="L":
        proverka=input("Хотите ли сделать проверку знаний?")
        otvet=input("Ответ:")
    else:break
