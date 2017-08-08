import collider

rect_sides = [
    collider.create_line(-2, 2, 2, 2),
    collider.create_line(2, 2, 2, -2),
    collider.create_line(2, -2, -2, -2),
    collider.create_line(-2, -2, -2, 2)
]

rectangle = collider.Polygon(rect_sides)
print(rectangle.dump())
