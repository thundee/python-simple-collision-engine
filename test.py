import collider
import math
import matplotlib.pyplot as plt

rect_sides = [
    collider.create_line(-2, 2, 2, 2),
    collider.create_line(2, 2, 2, -2),
    collider.create_line(2, -2, -2, -2),
    collider.create_line(-2, -2, -2, 2)
]

rectangle = collider.Polygon(rect_sides, 8, 0)

rectangle.rotate(math.radians(20))

coords = [
    [rectangle.sides[0]['end']['x'], rectangle.sides[0]['end']['y']],
    [rectangle.sides[1]['end']['x'], rectangle.sides[1]['end']['y']],
    [rectangle.sides[2]['end']['x'], rectangle.sides[2]['end']['y']],
    [rectangle.sides[3]['end']['x'], rectangle.sides[3]['end']['y']]
]

coords.append(coords[0])

xs, ys = zip(*coords)


rect_sides = [
    collider.create_line(-2, 2, 2, 2),
    collider.create_line(2, 2, 2, -2),
    collider.create_line(2, -2, -2, -2),
    collider.create_line(-2, -2, -2, 2)
]

rectangle1 = collider.Polygon(rect_sides, 2, 0)

rectangle1.rotate(math.radians(45))

coordss = [
    [rectangle1.sides[0]['end']['x'], rectangle1.sides[0]['end']['y']],
    [rectangle1.sides[1]['end']['x'], rectangle1.sides[1]['end']['y']],
    [rectangle1.sides[2]['end']['x'], rectangle1.sides[2]['end']['y']],
    [rectangle1.sides[3]['end']['x'], rectangle1.sides[3]['end']['y']]
]

coordss.append(coordss[0])

xss, yss = zip(*coordss)

print('Collided' if rectangle.check_collision(rectangle1) else 'Did not collide')

plt.figure()
plt.plot(xss, yss)
plt.plot(xs, ys)
plt.show()
