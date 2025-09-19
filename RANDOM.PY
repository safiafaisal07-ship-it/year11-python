#Define a function to calculate the area of a rectangle
def calculate_area(length, width):
    area = length * width
    return area

# Input length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Call the function and store the result in a variable
rectangle_area = calculate_area(length, width)

# Output the result
print("The area of the rectangle is:", rectangle_area)
