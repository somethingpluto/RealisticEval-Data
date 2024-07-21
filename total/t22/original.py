# CREATED BY CHATGPT
def distance_between_points(x1, y1, x2, y2):
    # Calculate the horizontal and vertical differences
    dx = x2 - x1
    dy = y2 - y1

    # Use the Pythagorean theorem to calculate the distance
    distance = (dx ** 2 + dy ** 2) ** 0.5

    return distance