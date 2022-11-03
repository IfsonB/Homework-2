string = input("Enter any string: ")
for i in range(len(string)):
    print("The ASCII value of character %c = %d" %(string[i], ord(string[i])))
ASCII_value = [ord(ch) for ch in string]
print("The ASCII value of characters:", ASCII_value)
ASCII_value = sum(ord(ch) for ch in string)
print("The ASCII value of characters:", ASCII_value)
ASCII_value = sum(map(ord, string))
print("The ASCII value of characters:", ASCII_value)

number_array = list() 
number = input("Enter the number of elements you want:") 
print ('Enter numbers in array: ') 
for i in range(int(number)): 
    n = input("number :") 
    number_array.append(int(n)) 
print ('ARRAY: ',number_array) 

