from math import sin, cos

def create_line(x1, y1, x2, y2):
    line = {
        'beg': {'x': x1, 'y': y1},
        'end': {'x': x2, 'y': y2}
    }

    return line


class Polygon:
    def __init__(self, sides, x, y, rotation_angle=None):
        self.sides = sides
        self.center = {'x': x, 'y': y}

        #Shifting the sides according to the center of the shape
        for side in self.sides:
            side['beg']['x'] += self.center['x']
            side['beg']['y'] += self.center['y']
            side['end']['x'] += self.center['x']
            side['end']['y'] += self.center['y']

        if rotation_angle is not None:
            self.rotate(rotation_angle)

    def rotate(self, angle):
        cx, cy = self.center['x'], self.center['y']
        def rotate_point(p):
            px, py = p['x'], p['y']
            rx = cx + cos(angle) * (px - cx) - sin(angle) * (py - cy)
            ry = cy + sin(angle) * (px - cx) + cos(angle) * (py - cy)
            return rx, ry

        for side in self.sides:
            side['beg']['x'], side['beg']['y'] = rotate_point(side['beg'])
            side['end']['x'], side['end']['y'] = rotate_point(side['end'])

    def move(self, x_shift, y_shift):
        self.center['x'] += x_shift
        self.center['y'] += y_shift
        for side in self.sides:
            side['beg']['x'] += x_shift
            side['beg']['y'] += y_shift
            side['end']['x'] += x_shift
            side['end']['y'] += y_shift

    def dump(self):
        string = ''
        for i, side in enumerate(self.sides):
            string += str(i) + ': ' + str(side) + '\n'

        return string

    def check_collision(self, other):
        def intersect(line1, line2):
            def ccw(A, B, C):
                return (C['y']-A['y'])*(B['x']-A['x']) > (B['y']-A['y'])*(C['x']-A['x'])

            ccw1 = ccw(line1['beg'], line2['beg'], line2['end'])
            ccw2 = ccw(line1['end'], line2['beg'], line2['end'])
            ccw3 = ccw(line1['beg'], line1['end'], line2['beg'])
            ccw4 = ccw(line1['beg'], line1['end'], line2['end'])

            return ccw1 != ccw2 and ccw3 != ccw4

        for side in self.sides:
            for other_side in other.sides:
                if intersect(side, other_side):
                    return True

        return False
