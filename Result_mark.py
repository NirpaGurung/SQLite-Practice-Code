from tkinter import *

root = Tk()
root.title("Result")
root.geometry("400x500")

Label(root, text="Result Generator", font=('Times New Roman', 20, 'bold')).grid(row=0, column=1, padx=5, pady=5)

# Create a function to add information in the window
def add_info():
    code_value = code.get()
    name_value = name.get()
    cl_value = cl.get()
    sec_value = sec.get()  # Added this line
    gen_value = gen.get()
    eng_value = float(eng.get())  # Corrected variable names
    dzo_value = float(dzo.get())  # Corrected variable names
    math_value = float(math.get())  # Corrected variable names
    sci_value = float(sci.get())  # Corrected variable names
    ict_value = float(ict.get())  # Corrected variable names

    # Calculate total and average marks
    total_marks = eng_value + dzo_value + math_value + sci_value + ict_value
    average_mark = (total_marks / 500) * 100

    # Display the total and average marks in the corresponding Entry widgets
    tot.set(total_marks)
    ave.set(average_mark)

# Define the variable to store the input
code = StringVar()
name = StringVar()
cl = StringVar()
sec = StringVar()
gen = StringVar()
eng = DoubleVar()
dzo = DoubleVar()
math = DoubleVar()
sci = DoubleVar()
ict = DoubleVar()
tot = DoubleVar()
ave = DoubleVar()

Label(root, text="Std_code:").grid(row=1, column=0, padx=5, pady=5)
Std_code_entry = Entry(root, textvariable=code).grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Name").grid(row=2, column=0, padx=5, pady=5)
Name_entry = Entry(root, textvariable=name).grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Class").grid(row=3, column=0, padx=5, pady=5)
Class_entry = Entry(root, textvariable=cl).grid(row=3, column=1, padx=5, pady=5)

Label(root, text="Section:").grid(row=4, column=0, padx=5, pady=5)
Section_entry = Entry(root, textvariable=sec).grid(row=4, column=1, padx=5, pady=5)

Label(root, text="Gender:").grid(row=5, column=0, padx=5, pady=5)
Gender_entry = Entry(root, textvariable=gen).grid(row=5, column=1, padx=5, pady=5)

Label(root, text="English:").grid(row=6, column=0, padx=5, pady=5)
Entry(root, textvariable=eng).grid(row=6, column=1, padx=5, pady=5)

Label(root, text="Dzongkha:").grid(row=7, column=0, padx=5, pady=5)
Entry(root, textvariable=dzo).grid(row=7, column=1, padx=5, pady=5)

Label(root, text="Mathematics:").grid(row=8, column=0, padx=5, pady=5)
Entry(root, textvariable=math).grid(row=8, column=1, padx=5, pady=5)

Label(root, text="Science:").grid(row=9, column=0, padx=5, pady=5)
Entry(root, textvariable=sci).grid(row=9, column=1, padx=5, pady=5)

Label(root, text="ICT:").grid(row=10, column=0, padx=5, pady=5)
Entry(root, textvariable=ict).grid(row=10, column=1, padx=5, pady=5)

Canvas(root, bg="red", width=400, height=2).grid(row=11, columnspan=5)

# Create a Calculate Button to calculate the Total and Average of student
Button(root, text="Calculate", command=add_info).grid(row=12, column=1, padx=5, pady=5)

# Create a label and text area to display the total
Label(root, text="Total:").grid(row=13, column=0, padx=5, pady=5)
Entry(root, textvariable=tot).grid(row=13, column=1, padx=5, pady=5)

# Create a label and text area to display the average
Label(root, text="Average:").grid(row=14, column=0, padx=5, pady=5)
Entry(root, textvariable=ave).grid(row=14, column=1, padx=5, pady=5)

root.mainloop()
