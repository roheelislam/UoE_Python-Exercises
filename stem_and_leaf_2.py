# Stem and leaves values data.
data_Feb = ['1st February', 45, 68, 70, 61, 54, 80, 72, 69, 73, 72, 58, 72, 64, 45, 42]
data_Aug = ['1st August', 19, 27, 41, 42, 9, 14, 29, 34, 25, 29, 44, 43, 6, 17]

# Sorting data in order after concatinating both arrays.
data = sorted(data_Feb[1:] + data_Aug[1:])

# Getting the first digit from two digit number 
first_values = sorted([int(x/10) for x in data])

#Getting the stem Values
stem_values = list(range(int(first_values[0]), int(first_values[-1])+1))

#Slicing array - Picking the integer values from array
data_integer_aug = sorted([int(x) for x in data_Aug[1:]])

#Initliaze the leaf values from Array
leaf_values_aug = [[] for s in stem_values]

#Slicing array - Picking the integer values from array
data_integer_feb = sorted([int(x) for x in data_Feb[1:]], reverse=True)

#Initliaze the leaf values from Array
leaf_values_feb = [[] for s in stem_values]

#temperoray variable for maximum size
max_size = 0 

#Creating stem leaf pairs for august array - Key Value pair
for value in data_integer_aug:
    leaf_values_aug[stem_values.index(value // 10)].append(value % 10)

#Creating stem leaf pairs for feb array - Key Value pair
for value in data_integer_feb:
    leaf_values_feb[stem_values.index(value // 10)].append(value % 10)

    #Calclating the highest/largest array size for printing the white spaces.
    temp_size = len(leaf_values_feb[stem_values.index(value // 10)])
    if max_size < temp_size:
        max_size = temp_size

#Creating First line for output with white spaces
first_line = []
if max_size < len(data_Feb[0]):
    max_size= len(data_Feb[0])

else:
    temp_size = max_size - len(data_Feb[0])
    iters = 0
    while iters < temp_size:
        first_line.append(' ')
        iters = iters + 1
        
#printing the first line of string
for x in data_Feb[0]:
        first_line.append(x)
first_line.append('| |')

for x in data_Aug[0]:
    first_line.append(x)

print (*first_line)

#Prints the rest of the key value stem & Leaf pairs with trailing white spaces
for items in stem_values:
    temp_array = []
    temp_size = max_size - len(leaf_values_feb[items])
    iters = 0

    #Appending the white spaces at the start
    for x in leaf_values_feb[items]:
        temp_array.append(x)
    for b in range (0, temp_size):
        
        print ("  ", end="")    
    temp_array.append('|'+ str(items) + '|')
    #printing the remainng array values.
    for x in leaf_values_aug[items]:
        temp_array.append(x)

    print(*temp_array)