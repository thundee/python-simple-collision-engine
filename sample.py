import collider
import math

#Declare sides(Note, that lines are relative to [0, 0])
rect_sides = [
    collider.create_line(-2, 2, 2, 2),
    collider.create_line(2, 2, 2, -2),
    collider.create_line(2, -2, -2, -2),
    collider.create_line(-2, -2, -2, 2)
]

#Create polygon at [5, 0]
rectangle = collider.Polygon(rect_sides, 5, 0)

#Rotate polygon
rectangle.rotate(math.radians(45))

#Move 10 points along X axis and 5 along y axis
#End position is [15, 5]
rectangle.move(10, 5)


#Create new polygon...
triangle_sides = [
    collider.create_line(-2, 0, 0, 2),
    collider.create_line(0, 2, 2, 0),
    collider.create_line(2, 0, -2, 0)
]

#Placing new polygon nearly the recrangle
triangle = collider.Polygon(triangle_sides, 12, 5)


print('Is collision detected: ' + str(triangle.check_collision(rectangle)))

print('Moving triangle...')

triangle.move(-8, 0)

print('Is collisition detected: ' + str(triangle.check_collision(rectangle)))
print('Done!')
