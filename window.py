import tkinter as tk
from interval import interval

from calculation import calculate
from calculationInterval import calculateInterval


xValuesRanges = [(1.9, 2.1), (2.9, 3.1), (3.9, 4.1), (5.9, 6.1)]  # Przedziały x
yValuesRanges = [(0.9, 1.1), (1.9, 2.1), (2.9, 3.1), (4.9, 5.1)]  # Przedziały y

xValuesFloat = [17, 20, 23, 24, 25, 27, 27.7]
yValuesFloat = [4.5, 7.0, 6.1, 5.6, 5.8, 5.2, 4.1]
f1x0Float = 3.0
f1xnFloat = -4.0

xiInput = 23.5


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
    
    interpolationPointsLabel = tk.Label(root, text="Węzły Interpolacji")
    interpolationPointsLabel.pack(padx=10, pady=20)

    interpolationPointsEntry = tk.Entry(root)
    interpolationPointsEntry.pack()

    derivativesLabel = tk.Label(root, text="Wartości pochodnych na końcach przedziału")
    derivativesLabel.pack(padx=10, pady=10)

    derivativesEntry = tk.Entry(root)
    derivativesEntry.pack()

    xiInputEntry = tk.Label(root, text="Punk interpolacji (x)")
    xiInputEntry.pack(padx=10, pady=10)

    rangeEntry = tk.Entry(root)
    rangeEntry.pack()


    button = tk.Button(root, text="Wykonaj Obliczenia", command=lambda: runCalculate())
    button.pack(padx=15, pady=15)


    def runCalculate():
        if radio_var.get() == "Option 1":
            c, Value, n, xi = calculate(
                x = xValuesFloat,
                f = yValuesFloat,
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
        elif radio_var.get() == "Option 2":
            c, Value, n, xi = calculateInterval(
                x = [interval[16.9, 17.1], interval[19.9, 20.1], interval[22.9, 23.1], interval[23.9, 24.1], interval[24.9, 25.1], interval[26.9, 27.1], interval[27.6, 27.8]],
                f = [interval[4.4, 4.6], interval[6.9, 7.1], interval[6.0, 6.2], interval[5.5, 5.7], interval[5.7, 5.9], interval[5.1, 5.3], interval[4.0, 4.2]],
                f1x0 = interval[2.9, 3.1],
                f1xn = interval[-4.1, -3.9],
                xi = 23.5
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
        elif radio_var.get() == "Option 3":
            c, Value, n, xi = calculateInterval(
                x = [interval[16.9, 17.1], interval[19.9, 20.1], interval[22.9, 23.1], interval[23.9, 24.1], interval[24.9, 25.1], interval[26.9, 27.1], interval[27.6, 27.8]],
                f = [interval[4.4, 4.6], interval[6.9, 7.1], interval[6.0, 6.2], interval[5.5, 5.7], interval[5.7, 5.9], interval[5.1, 5.3], interval[4.0, 4.2]],
                f1x0 = interval[2.9, 3.1],
                f1xn = interval[-4.1, -3.9],
                xi = 23.5
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

    root.mainloop()

