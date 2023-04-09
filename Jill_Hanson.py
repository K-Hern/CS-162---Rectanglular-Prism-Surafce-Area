# 2. rect_solid_area (length, width, height) which will return the area of a solid rectangular object
def rect_solid_area(length, width, height):
    area = 2 * (rect_area(length, width) + rect_area(height, length) + rect_area(height, width))
    return area
