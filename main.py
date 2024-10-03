import numpy as np


def generateArrWithRandomInts(low, high, size):
  return np.random.default_rng().integers(low, high, size)


# 1. Task 1: Creating a 1D NumPy Array
# Create a NumPy array containing the numbers from 1 to 30.
# Print the array and its shape.
# Access and print the element at index 10.

# Initialize an empty array
firstArr = []
# add 1 - 30 to the array
for i in range(30):
  firstArr.append(i+1)
  
# Convert it into Numpy array
firstArr = np.array(firstArr)

# Print the array
print("Generated Array: ", end='')
print(firstArr)

# Print the array shape
print("\nArray shape: ", end='')
print(firstArr.shape, end='')
print(" -> 1D \n")

# Print the element at the 10th index
print("Array's 10 index element: ", end='')
print(firstArr[10])


# 2. Task 2: Creating a 2D NumPy Array
# Reshape the 1D array from Task 1 into a 2D array of shape (6, 5).
# Print the entire 2D array.
# Access and print the element at row 3, column 4.

print("======================================= Second Task ===============================================")

# Assign secondArr with the the FirstArr reshaped
sencondArr = firstArr.reshape(6,5)

# Print the assigned array
print("Reshaped Array: ")
print(sencondArr)

# print the 4 row 5 element/column
print("\n4 row 5 element/column: ", end='')
print(sencondArr[3][4])


print("======================================= Third Task ===============================================")

# 3. Task 3: Subsetting a 2D Array
# Extract and print the third row from the 2D array created in Task 2.
# Extract and print the first two rows and the last three columns.


# Print the Third row - 0 1 2 -> Third 
print("Third row: ")                            
print(sencondArr[2])

# print the first 2 rows 0 and 1 and the last three elements/columns 
print("\nFirst two rows and the last three columns: ")
print(sencondArr[:2, -3:])

print("======================================= Fourth Task ===============================================")

# 4. Task 4: Generating Random Integer Array
# Use the numpy.random module to generate a 1D array of 15 random integers
# between 10 and 100.
# Print the array and find its maximum and minimum values.

# Use np.random to generate 15 integers between 10 to 100
# default_rng in the Constructor for a new Generator with the default BitGenerator (PCG64). if we dont use this function
# with np.random Numpy will not generate know how to generate the random nuber it needs an "Sequence" 
fourthArray = np.random.default_rng().integers(low=10, high=100, size=15)


# Print the generated array
print("Generated Array: ", end='')
print(fourthArray)

# Print the lowest value and the highest value inside the array
print("Minimum: ", end='')
print(fourthArray.min())
print("Maximum: ", end='')
print(fourthArray.max())


print("======================================= Fifth Task ===============================================")

# 5. Task 5: Generating a 2D Random Array
# Generate a 2D array of shape (4, 4) with random integers between 0 and
# 50.
# Print the array and find the sum of all the elements in the array.


# Same thing as Task number 4 but this time we are re-defining the shape
fifthArr = np.random.default_rng().integers(low=0, high=50, size=16)
fifthArr = fifthArr.reshape(4,4)


# Print the array and its sum
print("Array generated: ")
print(fifthArr)
print("\nSum: ", end='')
print(fifthArr.sum())


print("======================================= Sixth Task ===============================================")

# 6. Task 6: Manipulating Arrays
# Create a 2D array of random integers (shape 5, 5) between 1 and 20.
# Print the array.
# Set all values in the second row to 0.
# Replace all values greater than 10 with the value 99.

sixthArr = np.random.default_rng().integers(low=1, high=20, size=25)
sixthArr = sixthArr.reshape(5,5)

print("Generated Array: ")
print(sixthArr)


# Set All the element of the second row (index 1) to 0
sixthArr[1] = 0

# Check all the elements inside the array, and if they are bigger than 10 set it to 99
sixthArr[sixthArr > 10] = 99

# Print the result
print("\n\nModified Array: ")
print(sixthArr)



print("======================================= Seventh Task ===============================================")


# 7. Task 7: Arithmetic Operations on Arrays
# Create two 1D arrays of length 5 with random integers between 1 and 10.
# Perform element-wise addition, subtraction, and multiplication on the two
# arrays.
# Print the results.

seventhArr1 = generateArrWithRandomInts(1, 10, 5)
seventhArr2 = generateArrWithRandomInts(1, 10, 5)

print("Original first array: ", end='')
print(seventhArr1)
print("\nOriginal second array: ", end='')
print(seventhArr2)

# Addition
print("\nAddition")
print(np.add(seventhArr1, seventhArr2))

# Subtraction
print("\nSubtraction")
print(np.subtract(seventhArr1, seventhArr2))

# Multiply
print("\nMultiplication")
print(np.multiply(seventhArr1, seventhArr2))


print("======================================= Eighth Task ===============================================")

# 8. Task 8: Broadcasting in NumPy
# Create a 1D array of length 4 with values [2, 4, 6, 8].
# Create a 2D array of shape (3, 4) with random integers between 1 and 5.
# Add the 1D array to each row of the 2D array using broadcasting, then
# print the result.

firstEighthArr = np.array([2,4,6,8])

# Generate the Array with the requested size and element range
secondEighthArr = generateArrWithRandomInts(1, 5, (3 * 4))

# Reshape the array to the requested shape
secondEighthArr = secondEighthArr.reshape(3,4)  

print("First Arr: ", end='')
print(firstEighthArr)

print("\nSecond Arr")
print(secondEighthArr)


print("\nAddition: ")
print(secondEighthArr + firstEighthArr)



print("======================================= Ninth Task ===============================================")

# 9. Task 9: Filtering an Array
# Generate a 1D array of 20 random integers between 1 and 100.
# Print all elements of the array that are greater than 50.
# Replace all values less than 30 with -1 and print the modified array.

# Generate the Array with the requested size and element range
firstNinthArr = generateArrWithRandomInts(1, 100, 20)


# All the elements inside the Array that are greater than 50
print("Elements greater than 50: ")
print(firstNinthArr[firstNinthArr > 50])

# Change all the elements inside the array to -1 if they are smaller than 30
firstNinthArr[firstNinthArr < 30] = -1

print("\nModified Array: ")
print(firstNinthArr)

# 10. Task 10: Reshaping Arrays
# Create a 1D array of 12 random integers between 1 and 50.
# Reshape the array into a 3x4 2D array.
# Transpose the array (swap rows and columns) and print the result.

print("======================================= Ninth Task ===============================================")

# Generate the Array with the requested size and element range
tenthArr =  generateArrWithRandomInts(1, 50, 12)

# Transform the array into the requested shape
tenthArr = tenthArr.reshape(3,4)

print("Original Array: ")
print(tenthArr)

# Transpose function swap rows to columns and vice-versa
tenthArr = np.array(tenthArr).transpose()

print("\nTransposed Array: ")
print(tenthArr)
