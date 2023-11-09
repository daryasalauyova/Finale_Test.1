# Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
# Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
 
initial_array = input("Enter text separated by commas: ").split(",")  

new_array = [] 

for string in initial_array:  
    if len(string) <= 3:  
        new_array.append(string)  

if new_array: 
    print(new_array)  
else:
    print([])  