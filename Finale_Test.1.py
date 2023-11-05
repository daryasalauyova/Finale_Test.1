
initial_array = input("Enter text separated by commas: ").split(",")  

new_array = [] 

for string in initial_array:  
    if len(string) <= 3:  
        new_array.append(string)  

if new_array: 
    print(new_array)  
else:
    print([])  
