import tkinter as tk
from interval import interval

from calculation import calculate
from calculationInterval import calculateInterval
from validation import validation

xValuesInterval = [interval[16.9, 17.1], interval[19.9, 20.1], interval[22.9, 23.1], interval[23.9, 24.1], interval[24.9, 25.1], interval[26.9, 27.1], interval[27.6, 27.8]]
yValuesInterval = [interval[4.4, 4.6], interval[6.9, 7.1], interval[6.0, 6.2], interval[5.5, 5.7], interval[5.7, 5.9], interval[5.1, 5.3], interval[4.0, 4.2]]
f1x0Interval = interval[2.9, 3.1]
f1xnInterval = interval[-4.1, -3.9]


# xValuesInterval = [16.9, 17.1], [19.9, 20.1], [22.9, 23.1], [23.9, 24.1], [24.9, 25.1], [26.9, 27.1], [27.6, 27.8]
# yValuesInterval = [4.4, 4.6], [6.9, 7.1], [6.0, 6.2], [5.5, 5.7], [5.7, 5.9], [5.1, 5.3], [4.0, 4.2]

# d = [2.9, 3.1], [-4.1, -3.9]



# xValuesIntervalNumbers = 17, 20, 23, 24, 25, 27, 27.7
# yValuesIntervalNumbers = 4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1

# d = 3.0, -4.0



# xValuesFloat = 17, 20, 23, 24, 25, 27, 27.7
# yValuesFloat = 4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1

# f1x0Float = 3.0
# f1xnFloat = -4.0

# xiValue = 23.5

def window():
    root = tk.Tk()
    root.title("Funkcja sklejana stopnia trzeciego")

    root.geometry("950x600")

    label = tk.Label(root, text="Obliczanie wartości i współczynników funkcji sklejanej stopnia trzeciego")
    label.pack(side=tk.TOP,padx=20, pady=20)
    
    radio_var = tk.StringVar(value="Option 1")


    info = tk.Text(root, width=70, height=50)
    info.pack(side=tk.RIGHT, padx=70)

    arithmeticLabel = tk.Label(root, text="Wybierz rodzaj arytmetyki")
    arithmeticLabel.pack(padx=15, pady=15)

    radio1 = tk.Radiobutton(root, text="Zwykła (zmienno pozycyjna)", variable=radio_var, value="Option 1")
    radio1.pack()

    radio2 = tk.Radiobutton(root, text="Przedziałowa (dane liczby)", variable=radio_var, value="Option 2")
    radio2.pack()

    radio3 = tk.Radiobutton(root, text="Przedziałowe (dane przedziały)", variable=radio_var, value="Option 3")
    radio3.pack()
    
    xValuesLabel = tk.Label(root, text="Wartości x")
    xValuesLabel.pack(padx=10, pady=10)

    xValuesEntry = tk.Entry(root)
    xValuesEntry.pack()

    yValuesLabel = tk.Label(root, text="Wartości y")
    yValuesLabel.pack(padx=10, pady=10)

    yValuesEntry = tk.Entry(root)
    yValuesEntry.pack()

    derivativesLabel = tk.Label(root, text="Wartości pochodnych na końcach przedziału")
    derivativesLabel.pack(padx=10, pady=10)

    derivativesEntry = tk.Entry(root)
    derivativesEntry.pack()

    xiInputEntry = tk.Label(root, text="Punk interpolacji (x)")
    xiInputEntry.pack(padx=10, pady=10)

    xiEntry = tk.Entry(root)
    xiEntry.pack()

    button = tk.Button(root, text="Wykonaj Obliczenia", command=lambda: runCalculate())
    button.pack(padx=15, pady=15)

    def runCalculate():
        if radio_var.get() == "Option 1":
            error = False
            if not (validation(xiEntry.get(), 1)):
                error = 1
            if not (validation(derivativesEntry.get(), 2)):
                error = 2
            if not (validation(xValuesEntry.get(), 2) and validation(yValuesEntry.get(), 2)):
                error = 3
            derivatives = derivativesEntry.get().split(',')
            xValues = xValuesEntry.get().split(',')
            yValues = yValuesEntry.get().split(',')
            if not (len(xValues) == len(yValues)):
                error = 4
            elif not (len(derivatives) == 2):
                error = 5
            
            if error == 1:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne dane xi")
            elif error == 2:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne pochodne")
            elif error == 3:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zły format danych x lub y")
            elif error == 4:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Ilość danych x oraz y nie zgadza się")
            elif error == 5:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zła ilość pochodnych")
            
            if not error:
                try:
                    xiInput = float(xiEntry.get())
                    xValues = [float(x) for x in xValues]
                    yValues = [float(y) for y in yValues]
                    f1x0Float = [float(x) for x in derivatives][0]
                    f1xnFloat = [float(x) for x in derivatives][1]
                    c, Value, n, xi = calculate(
                        x = xValues,
                        f = yValues,
                        f1x0 = f1x0Float,
                        f1xn = f1xnFloat,
                        xi = xiInput
                    )

                    info.delete('1.0', tk.END)

                    title = f"Wartość w punkcie {xi}:\n\n{Value:.14e}"
                    subTitle = "Współczynniki:"

                    value = f"{title}\n\n\n{subTitle}\n\n"
                    info.insert(tk.END, value)

                    for i in range(n):
                        for j in range(4):
                            if(c[j][i] > 0 ):
                                info.insert(tk.END, f"a[{j},{i}] =  {c[j][i]:.14e}\n")
                            else:
                                info.insert(tk.END, f"a[{j},{i}] = {c[j][i]:.14e}\n")
                except ValueError:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "Coś poszło nie tak: upewni się że wprowadzone dane nadają się do obliczeń")
        elif radio_var.get() == "Option 2":
            error = False
            if not (validation(xiEntry.get(), 1)):
                error = 1
            if not (validation(derivativesEntry.get(), 2)):
                error = 2
            if not (validation(xValuesEntry.get(), 2) and validation(yValuesEntry.get(), 2)):
                error = 3
            derivatives = derivativesEntry.get().split(',')
            xValues = xValuesEntry.get().split(',')
            yValues = yValuesEntry.get().split(',')
            if not (len(xValues) == len(yValues)):
                error = 4
            elif not (len(derivatives) == 2):
                error = 5
            
            if error == 1:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne dane xi")
            elif error == 2:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne pochodne")
            elif error == 3:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zły format danych x lub y")
            elif error == 4:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Ilość danych x oraz y nie zgadza się")
            elif error == 5:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zła ilość pochodnych")
            
            if not error:
                try:
                    xiInput = float(xiEntry.get())
                    xValues = [interval[float(x)-0.00000000000001, float(x)+0.00000000000001] for x in xValues]
                    yValues = [interval[float(y)-0.00000000000001, float(y)+0.00000000000001] for y in yValues]
                    f1x0Float = interval[float(derivatives[0])-0.00000000000001, float(derivatives[0])+0.00000000000001]
                    f1xnFloat = interval[float(derivatives[1])-0.00000000000001, float(derivatives[1])+0.00000000000001]

                    c, Value, n, xi = calculateInterval(
                        x = xValues,
                        f = yValues,
                        f1x0 = f1x0Float,
                        f1xn = f1xnFloat,
                        xi = xiInput
                    )

                    info.delete('1.0', tk.END)

                    title = f"Wartość w punkcie {xi}:\n\n({Value[0]:.14e}, {Value[1]:.14e})"
                    subTitle = "Współczynniki:"

                    value = f"{title}\n\n\n{subTitle}\n\n"
                    info.insert(tk.END, value)

                    for i in range(n):
                        for j in range(4):
                            if(c[0][j][i] > 0 and  c[1][j][i] > 0):
                                info.insert(tk.END, f"a[{j},{i}] = (  {c[0][j][i]:.14e},  {c[1][j][i]:.14e} )\n")
                            elif(c[0][j][i] < 0 and  c[1][j][i] > 0):
                                info.insert(tk.END, f"a[{j},{i}] = ({c[0][j][i]:.14e}, {c[1][j][i]:.14e})\n")
                            elif(c[0][j][i] > 0 and  c[1][j][i] < 0):
                                info.insert(tk.END, f"a[{j},{i}] = ({c[0][j][i]:.14e}, {c[1][j][i]:.14e})\n")
                            else:
                                info.insert(tk.END, f"a[{j},{i}] = ( {c[0][j][i]:.14e}, {c[1][j][i]:.14e} )\n")
                except ValueError:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "Coś poszło nie tak: upewni się że wprowadzone dane nadają się do obliczeń")
        elif radio_var.get() == "Option 3":
            error = False
            if not (validation(xiEntry.get(), 1)):
                error = 1
            if not (validation(derivativesEntry.get(), 3)):
                error = 2
            if not (validation(xValuesEntry.get(), 3) and validation(yValuesEntry.get(), 3)):
                error = 3
            derivatives = derivativesEntry.get()[1:-1].split('], [')
            xValues = xValuesEntry.get()[1:-1].split('], [')
            yValues = yValuesEntry.get()[1:-1].split('], [')
            if not (len(xValues) == len(yValues)):
                error = 4
            elif not (len(derivatives) == 2):
                error = 5
            
            if error == 1:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne dane xi")
            elif error == 2:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Wprowadzono błędne pochodne")
            elif error == 3:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zły format danych x lub y")
            elif error == 4:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Ilość danych x oraz y nie zgadza się")
            elif error == 5:
                info.delete('1.0', tk.END)
                info.insert(tk.END, "Zła ilość pochodnych")


            if not error:
                try:
                    xiInput = float(xiEntry.get())

                    derivatives = derivativesEntry.get()
                    derivatives = derivatives[1:-1].split('], [')
                    derivatives = [interval[float(x.split(',')[0])-0.00000000000001, float(x.split(',')[1])+0.00000000000001] for x in derivatives]


                    xValues = xValuesEntry.get()
                    xValues = xValues[1:-1].split('], [')
                    xValues = [interval[float(x.split(',')[0])-0.00000000000001, float(x.split(',')[1])+0.00000000000001] for x in xValues]

                    yValues = yValuesEntry.get()
                    yValues = yValues[1:-1].split('], [')
                    yValues = [interval[float(x.split(',')[0])-0.00000000000001, float(x.split(',')[1])+0.00000000000001] for x in yValues]


                    c, Value, n, xi = calculateInterval(
                        x = xValuesInterval,
                        f = yValuesInterval,
                        f1x0 = f1x0Interval,
                        f1xn = f1xnInterval,
                        xi = xiInput
                    )

                    info.delete('1.0', tk.END)

                    title = f"Wartość w punkcie {xi}:\n\n({Value[0]:.14e}, {Value[1]:.14e})"
                    subTitle = "Współczynniki:"

                    value = f"{title}\n\n\n{subTitle}\n\n"
                    info.insert(tk.END, value)

                    for i in range(n):
                        for j in range(4):
                            if(c[0][j][i] > 0 and  c[1][j][i] > 0):
                                info.insert(tk.END, f"a[{j},{i}] = (  {c[0][j][i]:.14e},  {c[1][j][i]:.14e} )\n")
                            elif(c[0][j][i] < 0 and  c[1][j][i] > 0):
                                info.insert(tk.END, f"a[{j},{i}] = ({c[0][j][i]:.14e}, {c[1][j][i]:.14e})\n")
                            elif(c[0][j][i] > 0 and  c[1][j][i] < 0):
                                info.insert(tk.END, f"a[{j},{i}] = ({c[0][j][i]:.14e}, {c[1][j][i]:.14e})\n")
                            else:
                                info.insert(tk.END, f"a[{j},{i}] = ( {c[0][j][i]:.14e}, {c[1][j][i]:.14e} )\n")
                except ValueError:
                    info.delete('1.0', tk.END)
                    info.insert(tk.END, "Coś poszło nie tak: upewni się że wprowadzone dane nadają się do obliczeń")

    root.mainloop()

