#Напиcать программу,
#которая принимает на вход вещественное число и показывает сумму его цифр.

#x = input('Введите число ')

#def summa(x):                            
    #if float(x) < 0:                            
       # x = float(x) * (-1)
    #number = 0

    #for i in str(x):
        #if i != '.':
            #number += int(i)
    #return number

   
#print(f'Сумма чисел равна {summa(x)}')

# Напишите программу, которая
# принимает на вход число N и выдает набор произведений чисел от 1 до N.


#def factorial (number, count = 1):
    #for i in range(1, number + 1):
        #count *= i
    #return count

#n = int(input('Введите цифру: '))
#print(f'Набор числовых произведенний от 1 {n} = ', end = '')
#for i in range(1, n + 1):
    #if i == n: 
        #print(f'{factorial(i)}')
    #else:
        #print(f'{factorial(i)}', end = ', ')


#Задать список из n чисел последовательности 
# $(1+\frac 1 n)^n$ и вывести на экран их сумму.


     
#n = int(input('Введите количество чисел в последовательности: '))


#sum = 0
#for i in range(0, n):
    
    #input_value = int(input(f'Введите число #{i}: '))
    
    #sum += input_value

#print('Сумма всех чисел последовательности:', sum)