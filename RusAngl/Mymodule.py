


def loef(f:str,l:list):
    fail=open(f,"r",encoding="utf-8-sig")
    mas=[] 
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l

def failsalve(f:str,l:list):
    fail=open(f,'w')
    for el in l:
        fail.write(el+'\n')
    fail.close()

def newWord(f:str, rida:str)->list:
    l=[]
    with open(f,"a",encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")
    l=loef(f,l)
    return l

def error(l1:list,f1:str,l2:list,f2:str):
	sona=input("Слово с ошибкой: ")
	if sona not in l1 and sona not in l2:
		print("Такого слова нет в словаре!")
	else:
		if sona in l1:
			tolk=l2[l1.index(sona)]
			l1.remove(sona)
			l2.remove(tolk)
		elif sona in l2:
			tolk=l1[l2.index(sona)]
			l2.remove(sona)
			l1.remove(tolk)
		newWord(l1,input("Введите новое слово: "))
		newWord(l2,input("Enter new word: "))
		failsalve(f1,l1)
		failsalve(f2,l2)
def translate(r:list,a:list):
    word=input("Что перевести?: ")
    if word in r:
        transl=a[r.index(word)]
        print(word+"-"+transl)
    elif word in a:
        transl=r[a.index(word)]
        print(word+"-"+transl)
    else:
        print("Слово отсутствует в словаре")

import os
from gtts import gTTS

def heli(text:str,keel:str):
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")

import random
def proverka(l1:list,l2:list):
    resultat=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    print("random list ",lists)
    for i in range(len(l1)):
        print(l1,l1)
        print(l2,l2)
        otvet=input(f"Переведи слово - '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[i] in l1:
               if l1.index(lists[i])==l2.index(otvet):
                    resultat+=1
                    print("Молодец!Правильно")
                    print()
            elif lists[i] in l2:
                if l2.index(lists[i])==l1.index(otvet):
                    resultat+=1
                    print("Молодец!Правильно")
                    print()
        else:
            print("Неправильно")
            print()
    resultPer=(result/len(l1))*100
    print(f"Ваш результат: {resultPer}%")
