# CS 16X Git Assignment

# rect_solid_area (length, width, height) which will return the area of a solid rectangular object
def rect_solid_area(length, width, height):
    area = 2 * (rect_area(length, width) + rect_area(height, length) + rect_area(height, width))
    return area

# Function returns area of rectangle given length & width
def rect_area(length, width):
    area = length * width
    return area
    
# Request the dimension of a solid rectangular object
length = int(input("Enter the length of the the object as an integer: "))
width = int(input("Enter the width of the the object as an integer: "))
height = int(input("Enter the height of the the object as an integer: "))

surface_area = rect_solid_area(length, width, height)

print("Length = ", length, "Width = ", width, "Height = ", height)
print("Total Surface Area = ", surface_area)
