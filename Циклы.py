#print("For".center(60,"-"))
#for i in range(5):
#	print("Hello World!!!")
#print()
#print("While True".center(60,"-"))
#k=0
#while True:
#	k+=1
#	print("Hello World!!!")
#	if k==5: break
#print()
#print("While Tingimusega".center(60,"-"))
#k=0
#while k<5:
#	print("Hello World!!!")
#	k+=1
#print()
#print("(WHILE) 15 раз повторяются числы,среди них целых".center(60,"-"))
#t=0 #количество чисел (arvude kogus)
#q=0 #int
#while t<15:
#	t+=1
	#a=float(input("Sisesta arv =>"))
	#if a==round(a): q+=1
	#print("Täisarvude kogus =>",q)
#print()
#c=0
#q=0
#print("(FOR) 15 раз повторяются числы,среди них целых".center(60,"-"))
#for c in range(15):
#	c=float(input("Sisesta arv =>"))
	#q+=1
#	print("Täisarvude kogus =>",q)
#print()
#A=10
#s=0
#for arv in range(1,A+1):
	#s+=arv
#print("Summa =>",s)
#Задание 3
#from random import *
#k=1
#for i in range(8):
#	B=randint(-100,100)
#	print(B)
#	if B>0: k*=B
#print("Korrutis on",k)
#Задание 4
#for i in range(10,21):
#	print(i**2)
#	print()
#Задание 5
#from random import *
#k=1
#for i in range(10):
#	b=randint(-100,100)
#	print(b)
#	if b<0: k*=b
#print("Сумма отрицательных чисел => -",k)
#Задание 6
#from random import *
#k=1
#for i in range(10):
#	b=randint(-100,100)
#	print(b)
#	if b<0: 
#		print("Отрицательное число",b<0)
#	elif b>0:
#		print("Положительное число",b>0)
#print()
#from random import *
#N=int(input("Mitu: "))
#p=n=o=0
#while N>0:
#		N-=1
#		B=randint(-100,100)
#		print(B)
#		if B>0:
#			p+=1
#		elif B<0:
#			n+=1
#		else:
#			o+=1
#print("Pos:",p)
#print("Neg:",n)
#print("Nuulid:",o)
#print()
##Задание 7
#k=float(input("Введите K =>"))
#a=float(input("Введите A =>"))
#b=float(input("Введите B =>"))
#Задание 8
#a=input("Купи слона!")
#while a.lower() !="слон":
#	a=input("Все говорят" +a+"!А ты купи!!!")
#print("Слон твой!")
#print()
#a=int(input("Введите цифру =>"))
#for i in range(1,10):
#	print(a,"*",i,"=",a*i)
#Задание 15
#for j in range(0,3):
#	for i in range(0,10):
#		print(i,end=" ")
#	print()
#print()
#for g in range(1,10):
#	for i in range(1,10):
#		print(f"{(g*i):2}",end=" ")
#	print()
#for j in range(1,10):
#	for i in range(1,10):
#		if i==j:
#			print(i,end=" ")
#		else:
#			print("0",end=" ")
#	print()

for j in range(0,10):
	for k in range(0,1):
		print("x",end=" ")
	for i in range(1,10):
		if i==j:
			print("x",end=" ")
		else:
			print("0",end=" ")
	print()
#print("Игра мини лотерея!")
#from random import *
#game=0
#computer=randint(0,10)
#print("Компьютер загадал число!")
#while (game==0):
#	user=int(input("Напишите число =>"))
#	if (user==1 or user==2 or user==3 or user==4 or user==5 or user==6 or user==7 or user==8 or user==9):
#		game=1
#if user==1:
#	print("Игрок => 1")
#if user==2:
#	print("Игрок => 2")
#if user==3:
#	print("Игрок => 3")
#if user==4:
#	print("Игрок => 4")
#if user==5:
#	print("Игрок => 5")
#if user==6:
#	print("Игрок => 6")
#if user==7:
#	print("Игрок => 7")
#if user==8:
#	print("Игрок => 8")
#if user==9:
#	print("Игрок => 9")
#if computer==1:
#	print("Компьютер => 1")
#if computer==2:
#	print("Компьютер => 2")
#if computer==3:
#	print("Компьютер => 3")
#if computer==4:
#	print("Компьютер => 4")
#if computer==5:
#	print("Компьютер => 5")
#if computer==6:
#	print("Компьютер => 6")
#if computer==7:
#	print("Компьютер => 7")
#if computer==8:
#	print("Компьютер => 8")
#if computer==9:
#	print("Компьютер => 9")
#if user==1 and computer==1:
#	win=1
#if user==2 and computer==2:
#	win=2
#if user==3 and computer==3:
#	win=3
#if user==4 and computer==4:
#	win=4
#if user==5 and computer==5:
#	win=5
#if user==6 and computer==6:
#	win=6
#if user==7 and computer==7:
#	win=7
#if user==8 and computer==8:
#	win=8
#if user==9 and computer==9:
#	win=9
#if win==1:
#	print("Угадал число!Поздравляю!")
#if win==2:
#	print("Угадал число!Поздравляю!")
#if win==3:
#	print("Угадал число!Поздравляю!")
#if win==4:
#	print("Угадал число!Поздравляю!")
#if win==5:
#	print("Угадал число!Поздравляю!")
#if win==6:
#	print("Угадал число!Поздравляю!")
#if win==7:
#	print("Угадал число!Поздравляю!")
#if win==8:
#	print("Угадал число!Поздравляю!")
#if win==9:
#	print("Угадал число!Поздравляю!")
#else:
#	print("Не угадал!")