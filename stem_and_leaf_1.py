# Stem and leaves values data.
data = [ 4.7, 3.6, 3.8, 4.7, 4.1, 2.2, 3.6, 4.0, 4.4, 5.0, 
        3.7, 4.6, 4.8, 3.7, 3.2, 2.5, 3.6, 4.5, 4.7, 5.2, 
        4.7, 4.2, 3.8, 5.1, 1.4, 2.1, 3.5, 4.2, 2.4, 5.1]

# Sorting data in order
data = sorted(data)

# Using built in function to convert list in integer with starting and ending values
stem_values = list(range(int(data[0]),int(data[-1])+1))

# Multiplying by 10 to get single digit value
for i in range(len(data)):
    data[i] = data[i] * 10

# Storing values in data integer
data_integer = [int(x) for x in data]

# Making 2D array to store leaf values.
leaf_values = [[] for s in stem_values]

# Getting leaf values.
for value in data_integer:
    leaf_values[stem_values.index(value // 10)].append(value % 10)

# Printing stem and leaf values.
for stem, leaves in zip(stem_values, leaf_values):
    print(stem, "|", *leaves)