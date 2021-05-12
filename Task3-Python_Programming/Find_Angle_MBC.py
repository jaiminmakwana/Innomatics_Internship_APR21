from math import atan2, degrees, atan

ab = int(input())
bc = int(input())

if ab <= 100 and bc <= 100:
    theta = str(round(degrees(atan2(ab, bc)))) + u"\N{DEGREE SIGN}"
    print(theta)
