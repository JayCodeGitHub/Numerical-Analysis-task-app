import numpy as np
from scipy.interpolate import CubicSpline
from mpmath import iv

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

