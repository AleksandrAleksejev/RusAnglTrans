


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
def proverka(f:str,l:list):
    proverka 