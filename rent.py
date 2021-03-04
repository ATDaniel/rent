from tkinter import *


# def rent_percentage(rent, income1, income2):
#     total_income = income1 + income2
#     percentage1 = (rent * income1) / total_income
#     percentage2 = (rent * income2) / total_income
#     response = f'''Person who makes ${income1} pays ${percentage1}.
#         Person who makes ${income2} pays ${percentage2}'''
#     return response

# def main():
#     print("Enter your monthly rent")
#     rent = float(input())
#     print("Enter the first person's yearly salary")
#     income1 = float(input())
#     print("Enter the second person's yearly salary")
#     income2 = float(input())

#     rent_breakdown = rent_percentage(rent, income1, income2)
#     print(rent_breakdown)    

# if __name__ == "__main__":
#     main()

def main():
    def rent_percentage():
        rent_total = float(rent.get())
        income1 = float(p1.get())
        income2 = float(p2.get())
        total_income = income1 + income2
        percentage1 = (rent_total * income1) / total_income
        percentage2 = (rent_total * income2) / total_income
        result1.configure(text="${:.2f}".format(percentage1, 2))
        result2.configure(text="${:.2f}".format(percentage2, 2))

    # Initiate the encapsulating window
    window = Tk()
    window.title("Rent Calculations")
    window.geometry('700x400')

    # window top center title
    label = Label(window, text="Let's do that not-so-fun thing", font=("fira", 20))
    label.grid(column=1, row=0)

    # Rent label and text bar
    rent_label = Label(window, text="Rent: ")
    rent_label.grid(column=0, row=1)
    rent = Entry(window, width=20)
    rent.grid(column=1, row=1)
    rent.focus()

    # first person's salary
    p1_label = Label(window, text="First Person's Salary: ")
    p1_label.grid(column=0, row=2)
    p1 = Entry(window, width=20)
    p1.grid(column=1, row=2)

    # Second person's salary
    p2_label = Label(window, text="Second Person's Salary: ")
    p2_label.grid(column=0, row=3)
    p2 = Entry(window, width=20)
    p2.grid(column=1, row=3)

    # Calculate button
    go = Button(window, text="Calculate", command=rent_percentage, background='black', fg="#40233C")
    go.grid(column=1, row=4, pady=10)

    # Extra padding to get some space
    padding = Label(window, text="")
    padding.grid(column=0, row=5)

    # First Person's result
    result1_label = Label(window, text="First Person: ")
    result1_label.grid(column=0, row=6)
    result1 = Label(window, text="0")
    result1.grid(column=1, row=6)

    # Second person's result
    result2_label = Label(window, text="Second Person: ")
    result2_label.grid(column=0, row=7)
    result2 = Label(window, text=0)
    result2.grid(column=1, row=7)

    window.mainloop()

if __name__ == "__main__":
    main()