# create a rectangle with side lengths a, b
sides = (3, 4)
a, b = sides


def rectangle_info(_a, _b):
    _area = _a * _b
    _circumference = 2 * _a + 2 * _b
    return _area, _circumference


area, circumference = rectangle_info(*sides)

print(f'A rectangle with sidelengths {a} and {b} has area {area} and circumference {circumference}')
