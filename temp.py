import math

points = [(2, 3), (5, 7), (1, 8), (4, 2)]


def euclideanDistance(point1, point2):
    distance = math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)
    return distance

distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print("Minimum mesafe:", min_distance)
