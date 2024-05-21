import numpy as np
from scipy.interpolate import CubicSpline
from mpmath import iv

xValuesRanges = [(1.9, 2.1), (2.9, 3.1), (3.9, 4.1), (5.9, 6.1)]  # Przedziały x
yValuesRanges = [(0.9, 1.1), (1.9, 2.1), (2.9, 3.1), (4.9, 5.1)]  # Przedziały y


def calculateRanges(start, end, derStart, derEnd, xValues, yValues):


    # Przedział x
    xStart = iv.mpf(start)
    xEnd = iv.mpf(end)

    xValuesInterval = np.array(xValues)  # Przedziały x
    yValuesInterval = np.array(yValues)  # Przedziały y

    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(derStart)
    derivativeEnd = iv.mpf(derEnd)

    # Tworzenie funkcji sklejanej
    csInterval = CubicSpline(
        xValuesInterval[:, 0],
        yValuesInterval[:, 0],
        bc_type=(
            (1, derivativeStart),
            (1, derivativeEnd)
        )
    )

    # Wartości na końcach przedziału
    valueStartInterval = csInterval(iv.mpf(xStart))
    valueEndInterval = csInterval(iv.mpf(xEnd))


    # Współczynniki funkcji sklejanej
    coefficientsInterval = csInterval.c


    return valueStartInterval, valueEndInterval, coefficientsInterval

def calculationFloat(start, end, derStart, derEnd, xValues, yValues):
    
    # Przedział
    xStart = iv.mpf(start)
    xEnd = iv.mpf(end)


    # Pochodne na końcach przedziałów
    derivativeStart = iv.mpf(derStart)    
    derivativeEnd = iv.mpf(derEnd)


    # Dane wejściowe - przedziały x i odpowiadające im wartości y
    xValuesFloat = np.array(xValues)  # Przedziały x
    yValuesFloat = np.array(yValues)  # Przedziały y
    
    
    # Tworzenie funkcji sklejanej
    csFloat = CubicSpline(xValuesFloat, yValuesFloat, bc_type=((1, derivativeStart), (1, derivativeEnd)))
    
    # Wartości na końcach przedziału
    valueStartFloat = csFloat(xStart)
    valueEndFloat = csFloat(xEnd)
    
    # Współczynniki funkcji sklejanej
    coefficientsFloat = csFloat.c
    

    return valueStartFloat, valueEndFloat, coefficientsFloat

valueStartInterval, valueEndInterval, coefficientsInterval = calculateRanges(
    start=1,
    end=7,
    derStart=6,
    derEnd=14,
    xValues=xValuesRanges,
    yValues=yValuesRanges
)



print("Wartość na początku przedziału (przedziałowa):", valueStartInterval)
print("Wartość na końcu przedziału (przedziałowa):", valueEndInterval)
print("Współczynniki funkcji sklejanej (przedziałowa):", coefficientsInterval)
