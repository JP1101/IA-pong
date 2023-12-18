import math

def ReLu(n):
    return max(0, n)



def CalcA(V1, V2):
    return math.degrees(math.atan(V1/V2))


def CalcNeurone(x1, w1, x2, w2, x3, w3, b):
    y = ReLu(x1*w1 + x2*w2 + x3*w3 + b)
    return y