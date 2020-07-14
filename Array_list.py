input_array = input("Enter items separated by comma"+"\n")
array_list = input_array.split(",")

print("\n")
print("Printing all items names")
for name in array_list:
    print(name)

def reject():
    rej = input("enter that you want to exclude")
    rej.lower()
    for name in array_list:
        
        
        if rej == name :
            array_list.remove(name)
            print(array_list)
print(reject())
        

