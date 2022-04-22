#Calc v1.1
from colorama import init
from colorama import Fore, Back, Style
init()
print( Fore.GREEN )
print("Добро пожаловать в простейший калькулятор!")
print( Fore.CYAN )
num1 = float( input("Введите первое число:") ) 
print( Fore.YELLOW )
oper = input("Введите операцию (+,-,/,*)")
print( Fore.CYAN )
num2 = float( input("Введите второе число:") )
print( Fore.RED )
if oper =="+":
    print(num1 + num2)
if oper =="-":
    print(num1 - num2)
if oper =="/":
    print(num1 / num2)
if oper =="*":
    print(num1 * num2)
input()
