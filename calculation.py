import numpy as np
from scipy.interpolate import CubicSpline
from mpmath import iv

xValues = [(1.9, 2.1), (2.9, 3.1), (3.9, 4.1), (5.9, 6.1)]  # Przedziały x
yValues = [(0.9, 1.1), (1.9, 2.1), (2.9, 3.1), (4.9, 5.1)]  # Przedziały y


def calculateRanges(start, end, xValues, yValues):


    # Przedział x
    xStart = iv.mpf(start)
    xEnd = iv.mpf(end)

    xValuesInterval = np.array(xValues)  # Przedziały x
    yValuesInterval = np.array(yValues)  # Przedziały y

    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(6)
    derivativeEnd = iv.mpf(14)

    # Tworzenie funkcji sklejanej
    csInterval = CubicSpline(xValuesInterval[:, 0], yValuesInterval[:, 0], bc_type=((1, derivativeStart), (1, derivativeEnd)))

    # Wartości na końcach przedziału
    valueStartInterval = csInterval(iv.mpf(xStart))
    valueEndInterval = csInterval(iv.mpf(xEnd))


    # Współczynniki funkcji sklejanej
    coefficientsInterval = csInterval.c


    return valueStartInterval, valueEndInterval, coefficientsInterval


valueStartInterval, valueEndInterval, coefficientsInterval = calculateRanges(
    start=1,
    end=7,
    xValues=xValues,
    yValues=yValues
)



print("Wartość na początku przedziału (przedziałowa):", valueStartInterval)
print("Wartość na końcu przedziału (przedziałowa):", valueEndInterval)
print("Współczynniki funkcji sklejanej (przedziałowa):", coefficientsInterval)
