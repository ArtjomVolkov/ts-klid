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
a=input("Купи слона!")
while a.lower() !="слон":
	a=input("Все говорят" +a+"!А ты купи!!!")
print("Слон твой!")

