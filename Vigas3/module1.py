from random import *
def arvud_loendis():
    """
    Выполняет работу с заданным числовым диапазоном, находит положительные числа, находит отрицательные числа и составляет список чисел по возрастанию.
    После чего высчитывает среднее число всего списка, только положительных и только отрицательных чисел и добавляет их в основной массив.
    
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    pos=neg=null=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """
    Меняет числа местами в случае ошибки ввода
    :Param int a: Минимальное число
    :Param int b: Максимальное число
    :rtype: int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend:list,a:int,b:int):
    """
    Генерирует список случайных значений заданного диапазона
    :Param int n: кол-во значений 
    :Param list loend: список для записи значений 
    :Param int a: Минимальныое значение 
    :Param int b: Максимальное значение 
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend:list,p:list,n:list,nol:list):
    """
    Генерируте списки положительных чисел, отрицательных чисел и список чисел = 0
    :Param list loend: Список всех чисел 
    :Param list p: Список положительных чисел
    :Param list n: Список отрицательных чисел 
    :Param list nol: Список чисел со значением 0 
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend:list):
    """
    Высчитавет среднее арифметическое число из списка
    :Param loend: Список всех значений из которых будем получать среднее число
    :rtype: var  
    """
    n=len(loend)
    if n==0:
        kesk=0
    
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend:list,el:float):
    """
    Добавляет среднее значение негативных и отрицательных чисел в основной список 
    :Param list loend: Основной список со всеми значениями 
    :Param float: среднее значения как отрицательных, так и положительных чисел 
    """
    loend.append(el)
    loend.sort()

arvud_loendis
