import numpy as np
from scipy.interpolate import CubicSpline
from mpmath import iv

def calculateRanges(start, end):


    # Przedział x (można go dostosować)
    xStart = iv.mpf(start)
    xEnd = iv.mpf(end)

    xValuesInterval = np.array([(1.9, 2.1), (2.9, 3.1), (3.9, 4.1), (5.9, 6.1)])  # Przedziały x (przedziałowe)
    yValuesInterval = np.array([(0.9, 1.1), (1.9, 2.1), (2.9, 3.1), (4.9, 5.1)])  # Przedziały y (przedziałowe)

    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(6)
    derivativeEnd = iv.mpf(14)

    # Tworzenie funkcji sklejanej - przedziałowa
    csInterval = CubicSpline(xValuesInterval[:, 0], yValuesInterval[:, 0], bc_type=((1, derivativeStart), (1, derivativeEnd)))

    # Wartości na końcach przedziału - przedziałowa
    valueStartInterval = csInterval(iv.mpf(xStart))
    valueEndInterval = csInterval(iv.mpf(xEnd))


    # Współczynniki funkcji sklejanej - przedziałowa
    coefficientsInterval = csInterval.c


    return valueStartInterval, valueEndInterval, coefficientsInterval


valueStartInterval, valueEndInterval, coefficientsInterval = calculateRanges(start=1, end=7)



print("Wartość na początku przedziału (przedziałowa):", valueStartInterval)
print("Wartość na końcu przedziału (przedziałowa):", valueEndInterval)
print("Współczynniki funkcji sklejanej (przedziałowa):", coefficientsInterval)
