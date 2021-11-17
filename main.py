
def calcSampleMean(values):
    sum = 0
    for value in values:
        sum += value

    return sum / len(values)


def calcsxx(values, mean):
    sum = 0
    for value in values:
        sum += (value - mean) ** 2

    return sum


def calcxy(valuesx, valuesy, meanx, meany):
    sum = 0
    # assuming that len of valuesx is equal to len of valuesy
    for i in range(0, len(valuesx)):
        sum += (valuesx[i] - meanx) * (valuesy[i] - meany)

    return sum


# give a list of tuples
def calcb1(valuesx, valuesy):
    meanx = calcSampleMean(valuesx)
    meany = calcSampleMean(valuesy)

    sxx = calcsxx(valuesx, meanx)
    sxy = calcxy(valuesx, valuesy, meanx, meany)

    return sxy / sxx


def calcb0(b1, valuesx, valuesy):
    return calcSampleMean(valuesy) - b1 * calcSampleMean(valuesx)

def calcR2(valuesx, valuesy):
    meanx = calcSampleMean(valuesx)
    meany = calcSampleMean(valuesy)

    sxy_squared = calcxy(valuesx, valuesy, meanx, meany) ** 2
    sxx = calcsxx(valuesx, meanx)
    syy = calcsxx(valuesy, meany)

    return sxy_squared / (sxx * syy)

lengthOfInput = input("Amount of points: ")

x = []
y = []

for i in range(0, int(lengthOfInput)):
    xinput = input("x: ")
    yinput = input("y: ")
    x.append(float(xinput))
    y.append(float(yinput))

#x = [0.93, 0.47, 0.26, 0.16, 0.97, 0.74, 0.93, 0.36, 0.48, 0.49, 0.84, 0.77]
#y = [8.56, 5.98, 6.83, 5.26, 9.78, 7.51, 8.41, 6.72, 6.82, 5.14, 7.56, 6.64]

print("-------------")
print("Values: ")
print("X: ")
print(x)
print("Y: ")
print(y)

b1 = calcb1(x, y)
b0 = calcb0(b1, x, y)

print("-------------")
print("B1: ")
print(b1)
print("B0: ")
print(b0)

print("-------------")
print("This gives the estimated line: ")
print("y = " + str(b0) + " + " + str(b1) + "x")
print("-------------")

print("R^2")
print(calcR2(x, y))

print("-------------")



