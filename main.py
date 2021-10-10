import random
import functools
import matplotlib.pyplot as plt


def point():
    point = [random.randint(-15, 15), random.randint(-15, 15)]
    return point


def generatePoints():
    polygonPoints = []

    for _ in range(int(input('Enter count of random points: '))):
        polygonPoints.append(point())

    return polygonPoints


def showPlot(points, grahamIndexes, title):
    for p in points:
        plt.scatter(p[0], p[1], color="red")

    for i in grahamIndexes:
        plt.scatter(points[i][0], points[i][1], color="green")

    plt.fill(
        [points[i][0] for i in grahamIndexes],
        [points[i][1] for i in grahamIndexes],
        fill=False
    )

    plt.title(title)
    plt.savefig('demo.png', bbox_inches='tight')


def isLeft(a, b, point):  # On which side is the point relative to AB
    return (b[0] - a[0]) * (point[1] - b[1]) - (b[1] - a[1]) * (point[0] - b[0])


def scan(points):
    lengthPoints = len(points)
    pointsNum = list(range(lengthPoints))

    # search minimal x
    for i in range(1, lengthPoints):
        if points[pointsNum[i]][0] < points[pointsNum[0]][0]:
            pointsNum[i], pointsNum[0] = pointsNum[0], pointsNum[
                i]
    # sort
    base = pointsNum[0]
    del pointsNum[0]
    pointsNum.sort(key=functools.cmp_to_key(lambda x, y: isLeft(points[base], points[y], points[x])))
    pointsNum.insert(0, base)

    # look at the angles and cut them
    S = [pointsNum[0], pointsNum[1]]
    for i in range(2, lengthPoints):
        while isLeft(points[S[-2]], points[S[-1]], points[pointsNum[i]]) < 0:
            del S[-1]
        S.append(pointsNum[i])
    return S


if __name__ == '__main__':
    points = generatePoints()
    indexes = scan(points)
    showPlot(points, indexes, "Graham scan")
