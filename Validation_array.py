#Assignment2 Validation of array:-

input_array = ["impolite", "cows", "undress", "rule", "illustrious", "beam", "helpless", "gold", "hair", "vacuous", "help", "guess", "squalid", "wonderful", "memorise", "present", "painful", "brake", "sand", "lip", "rainstorm", "talk", "abashed", "box", "partner", "chop", "tenuous", "robin", "trees", "moor", "hunt", "pack", "old-fashioned"]

validation_array = ["cows", "partner", "wonderful", "rainstorm", "pack", "painful"]

def list_comprehension(a,b):
  
        
    temp=[elem for elem in a if not elem  in b ]
    print(temp)
    
print("entered array is :- ",input_array)
print ("After validation")

print(list_comprehension(input_array,validation_array))




