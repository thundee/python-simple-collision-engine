def create_line(x1, y1, x2, y2):
    line = {
        'beg': {'x': x1, 'y': y1},
        'end': {'x': x2, 'y': y2}
    }

    return line


class Polygon:
    def __init__(self, sides, rotation_angle=None):
        self.sides = sides

        if rotation_angle is not None:
            self.rotate(rotation_angle)

    def rotate(angle):
        print('placeholder')

    def dump(self):
        string = ''
        for i, line in enumerate(self.sides):
            string += str(i) + ': ' + str(line) + '\n'

        return string
        print('dumped')
