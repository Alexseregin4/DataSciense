import sys
import random
import string
from os import system
from random import randint

def display_menu(menu):
    """
    Select task from homework1 menu.
    :param menu: dictionary, key identifies a value which is a task name
    :return:
    """
    for k, function in menu.items():
        print(k, function.__name__)


def TASK1():
    print("Создать кортеж, содержащий 4 разных числа. Вывести на экран значение второго элемента кортежа.")
    MyList = []
    i=int(input("Enter count of Typle elements:"))
    for j in range(i):
        MyList.append(random.randint(1,100))
    MyTuple = tuple(MyList)
    ii=int(input("Enter number of Typle elements:"))
    try:
        print('Randomised TYPLE is: ', MyTuple)
        print('The', ii, 'typle element is:', MyTuple[ii-1])
    except:
        print(ii ,'Is invalid element number')
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout


def TASK2():
    print("2.	Написать программу, которая принимает строку от пользователя и выводит количество символов в этой строке.")
    a = str(input("Enter your string:"))
    n = len(a)
    print('Your string', a, 'length is', n)
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout


def TASK3():
    print("3.	Создать словарь, содержащий информацию о студенте: имя, возраст, курс. Вывести всю информацию о студенте на экран.")
    my_dict = {'name': '', 'age': '', 'course': ''}
    my_dict['name'] = str(input("Enter student name:"))
    my_dict['age'] = str(input("Enter student age:"))
    my_dict['course'] = str(input("Enter student course:"))
    print('Your dictionary is: ', my_dict)
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout

def TASK4():
    print("4.	Используя цикл, создать список, содержащий все целые числа от 1 до 10, и вывести его на экран.") # Simulate function output.
    MyList2 = []
    i=int(input("Enter count of List elements:"))
    for j in range(i):
        MyList2.append(j+1)
    print('Your list is:', MyList2)
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout

def TASK5():
    print("5.	Написать функцию, которая принимает список чисел и возвращает их сумму.")
    MyList3 = []
    i=int(input("Enter count of List elements:"))
    for j in range(i):
        MyList3.append(random.randint(1,100))
    s = sum(MyList3)
    print('Your list is:', MyList3, 'sum is:', s)
    input("Press Enter to Continue\n")
    system('cls')  # clears stdout

def TASK6():
    print("6.	Создать множество из 5 разных чисел, затем добавить в него новое число и вывести на экран.")
    MySet = set()
    i = int(input("Enter count of Set elements:"))
    for j in range(i):
        MySet.add(random.randint(1,100))
    print('Your set is:', MySet)
    try:
        n = int(input("Enter number for add to Set:"))
        MySet.add(n)
    except ValueError: print("Please enter a number")
    print('Your new set is:', MySet)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK7():
    print("7.	Написать программу, которая принимает от пользователя целое число и выводит на экран его квадрат.")
    i = int(input("Enter the number:"))
    a = i**2
    print('Your number squared  is:', a)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK8():
    print("8.	Создать словарь с пятью парами «ключ-значение», где ключи - названия фруктов, а значения - их цвета. Вывести значения всех ключей.")
    my_dict = {'orange': 'orange', 'apple': 'red', 'kiwi': 'green', 'banana': 'yellow', 'mango': 'green'}
    my_dict_keys = list(my_dict.keys())
    print('Your dictionary is', my_dict)
    print('The keys of dictionary is ', my_dict_keys)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK9():
    print("9.	Написать функцию, которая принимает строку и выводит ее в обратном порядке.")
    a = str(input("Enter your string:")) [::-1]
    print('Your reverse string is', a)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK10():
    print("10.	Создать список из 5 строк и заменить в нем третий элемент на новую строку.")
    MyList = []
    N = 10
    i = int(input("Enter count of strings in List: "))
    for j in range(i):
        MyList.append(''.join(random.choices(string.ascii_letters +
                                 string.digits, k=N)))
    print("String List is ", MyList)
    n = int(input("Enter the number of List element that you want to change :"))
    s = str(input('Enter new string: '))
    MyList[n-1] = s
    print("New List is:", MyList)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK11():
    print("11.	Создать кортеж из 6 элементов разных типов данных и вывести на экран тип каждого элемента.")
    my_typle = (10, 2.13, "square", 89, 'C', True)
    print("Your Tuple is: ", my_typle)
    print("Type of Tuple element is: ", list(map(type, my_typle)))
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK12():
    print("12.	Написать программу, которая принимает от пользователя два числа и выводит их произведение.")
    n = int(input("Enter first number:"))
    i = int(input("Enter first number:"))
    print("The produce of tu numbers is: ", n*i)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK13():
    print("13.	Создать словарь, содержащий информацию о книге (автор, название, год издания), и вывести эту информацию на экран.")
    print("The same of TASK3")
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK14():
    print("14.	Создать множество, содержащее названия 5 разных городов, затем удалить одно название и вывести оставшиеся.")
    MySet = set()
    My_List = ["Minsk", "Gomel", "Vitebsk", "Grodno", "Paris"]
    MySet.update(My_List)
    print('Your set is:', MySet)
    try:
        n = str(input("What City would you like to del:"))
        MySet.remove(n)
    except ValueError:
        print("Please enter a wrong city")
    print('Your new set is:', MySet)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK15():
    print("15.	Написать функцию, которая принимает список чисел и возвращает максимальное из них.")
    MyList = []
    i=int(input("Enter count of List elements:"))
    for j in range(i):
        MyList.append(random.randint(1,100))
    m = str(max(MyList))
    print('Your List is:', MyList, "Max number in List", m)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK16():
    print("16.	Создать список чисел от 1 до 20, а затем создать новый список, содержащий только четные числа из первого списка.")
    MyList = []
    MyList_odd = []
    i = 20
    for j in range(i):
        MyList.append(j+1)
    for num in MyList:
        if num % 2 == 0: MyList_odd.append(num)
    print('Your List is:', MyList)
    print("Odds in List is:", MyList_odd)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK17():
    print("17.	Написать программу, которая принимает от пользователя строку и выводит True, если строка является палиндромом, и False в противном случае.")
    s=str(input("Enter a string: ")).lower()
    if s==s [::-1] : b = True
    else: b = False
    print('The string is palindrome: ', b)
    input("Press Enter to Continue\n")
    system('cls')  # clears

def TASK18():
    print("17.	Написать программу, которая принимает от пользователя строку и выводит True, если строка является палиндромом, и False в противном случае.")
    s=str(input("Enter a string: ")).lower()
    if s==s [::-1] : b = True
    else: b = False
    print('The string is palindrome: ', b)
    input("Press Enter to Continue\n")
    system('cls')  # clears


def done():
    system('cls')  # clears stdout
    print("Goodbye")
    sys.exit()


def main():
    # Create a menu dictionary where the key is an integer number and the
    # value is a task name.
    functions_names = [TASK1, TASK2, TASK3, TASK4, TASK5, TASK6, TASK7, TASK8, TASK9, TASK10, TASK11, TASK12, TASK13, TASK14, TASK15, TASK16, TASK17, done]
    menu_items = dict(enumerate(functions_names, start=1))

    while True:
        display_menu(menu_items)
        selection = int(
            input("Please enter your selection number: "))  # Get function key
        selected_value = menu_items[selection]  # Gets the function name
        selected_value()  # add parentheses to call the function


if __name__ == "__main__":
    main()