usr_choice = int(input("Enter no of your choice: "))

for i in range(usr_choice):
    array1 = list(input("Enter a array:"))
    print (array1)
    print (len(array1))
    
    for i in range(array1):
        if array1.count > 1:
            print("True")
        else:
            print("False")            
    myset = set(array1)
    
    final_list = list(myset)
    final_list.sort()

    print (myset)
    print(final_list)
