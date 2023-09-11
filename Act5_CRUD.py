import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def main():
    # Connect to the StudentResult database
    conn = sqlite3.connect('StudentResult.db')
    cur = conn.cursor()

    # Create a table if it doesn't already exist
    cur.execute('''CREATE TABLE IF NOT EXISTS StdDetails (StdCode STRING PRIMARY KEY NOT NULL,
                                                        Name STRING NOT NULL,
                                                        Class STRING NOT NULL,
                                                        English REAL NOT NULL,
                                                        Dzongkha REAL NOT NULL,
                                                        Maths REAL NOT NULL,
                                                        ICT REAL NOT NULL,
                                                        Total REAL NOT NULL,
                                                        Average REAL NOT NULL,
                                                        Remark STRING NOT NULL)''')

    # Tkinter GUI
    root = Tk()
    root.title("Result Generator(PP - III)")
    root.config(bg='Navy')
    Label(root, text="RESULT GENERATOR (PP - III)", font=("Arial Rounded MT Bold",18), bg="Coral").grid(row=0, column=0,  padx=10, columnspan=4, pady=10)

    Canvas(root,width=380, height=3, bg="purple").grid(row=1,columnspan=5)#line1
    
    # Define variable to store user inputs and values from calculations
    code = StringVar()
    name = StringVar()
    _class = StringVar()
    eng = DoubleVar()
    dzo = DoubleVar()
    maths = DoubleVar()
    ict = DoubleVar()
    total = DoubleVar()
    avg = DoubleVar()
    remark = StringVar()

    # Create a label and text entry for student code
    stdcode_label = Label(root, text="Student Code:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=2,column=0,padx=10,pady=10)
    stdcode_entry = Entry(root, textvariable=code,highlightcolor="Coral",highlightbackground="Coral").grid(row=2,column=1,columnspan=2,padx=10,pady=10)

    # Create a label and text entry for student name
    name_label = Label(root, text="Student Name:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=3,column=0,padx=10,pady=10)
    name_entry = Entry(root,textvariable=name,highlightcolor="Coral",highlightbackground="Coral").grid(row=3,column=1,columnspan=2,padx=10,pady=10)
    
    # Create a label and text entry for class
    class_label = Label(root, text="Class:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=4,column=0,padx=10,pady=10)
    class_entry = Entry(root,textvariable=_class,highlightcolor="Coral",highlightbackground="Coral").grid(row=4,column=1,columnspan=2,padx=10,pady=10)
    
    # Create a label and text entry for English Marks
    eng_label = Label(root, text="English:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=5,column=0,padx=10,pady=10)
    eng_entry = Entry(root,textvariable=eng,highlightcolor="Coral",highlightbackground="Coral").grid(row=5,column=1,columnspan=2,padx=10,pady=10)
    
    # Create a label and text entry for Dzongkha Marks
    dzo_label = Label(root, text="Dzongkha:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=6,column=0,padx=10,pady=10)
    dzo_entry = Entry(root,textvariable=dzo,highlightcolor="Coral",highlightbackground="Coral").grid(row=6,column=1,columnspan=2,padx=10,pady=10)

    # Create a label and text entry for Maths marks
    maths_label = Label(root, text="Maths:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=7,column=0,padx=10,pady=10)
    maths_entry = Entry(root,textvariable=maths,highlightcolor="Coral",highlightbackground="Coral").grid(row=7,column=1,columnspan=2,padx=10,pady=10)

    # Create a label and text entry for ICT
    ict_label = Label(root, text="ICT:",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=8,column=0,padx=10,pady=10)
    ict_entry = Entry(root,textvariable=ict,highlightcolor="Coral",highlightbackground="Coral").grid(row=8,column=1,columnspan=2,padx=10,pady=10)

    Canvas(root,width=380, height=3, bg="purple").grid(row=9,columnspan=5)#line2
    
    # Create a function to calculate the total and average of every student
    def calculate():
        total.set(eng.get() + dzo.get() + maths.get() + ict.get())
        avg.set(total.get()/4)
        round_value=round(avg.get(),2)
        avg.set(round_value)
        if (avg.get()>=40):
            remark.set("Passed")
        else:
            remark.set("Failed")
    
    # Create a function to add the student info to the database
    def add_details():
        # defining the DoubleVar() data type as float
        # save the values of the variables in a new set of variables
        code_value = code.get()
        name_value = name.get()
        _class_value = _class.get()
        eng_value = float(eng.get())
        dzo_value = float(dzo.get())
        maths_value = float(maths.get())
        ict_value = float(ict.get())
        total_value = float(total.get())
        avg_value = float(avg.get())
        remark_value = remark.get()

        # Query to insert the data into the table
        cur.execute('''INSERT INTO StdDetails
        VALUES (?,?,?,?,?,?,?,?,?,?)''', (code_value,name_value,_class_value,eng_value,dzo_value,maths_value,ict_value,total_value,avg_value,remark_value))

        conn.commit()

        # Clearing the data entered in variables to enter new set of data
        code.set("0")
        name.set("")
        _class.set("")
        eng.set(0)
        dzo.set(0)
        maths.set(0)
        ict.set(0)
        total.set(0)
        avg.set(0)
        remark.set("")
    
        messagebox.showinfo("Success", "Information added in the database.")

    # Create a button to calulate thet total, average of every student
    calc_button = Button(root, text = "calculate",font=("Arial Rounded MT Bold",12),bg="Dark Red", command = calculate,highlightcolor="Forest Green",highlightbackground="Forest Green").grid(row=10,column=1,columnspan=2,padx=10,pady=10)

    # Create a label and text area to display the total
    total_label = Label(root, text="Total",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=11,column=0,padx=10,pady=10)
    tmarks_label = Label(root, textvariable = total,bg="Coral").grid(row=11,column=1,columnspan=2,padx=10,pady=10)
                
    # Create a label and text area to display the average
    avg_label = Label(root, text="Average",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=12,column=0,padx=10,pady=10)
    avgmarks_label = Label(root, textvariable = avg,bg="Coral").grid(row=12,column=1,columnspan=2,padx=10,pady=10)

    # Create a label and text area to display the remark
    remark_label = Label(root, text="Remark",font=("Arial Rounded MT Bold",12),bg="Coral").grid(row=13,column=0,padx=10,pady=10)
    result = Label(root, textvariable = remark,bg="Coral").grid(row=13,column=1,columnspan=2,padx=10,pady=10)
    
                
    # Create a button to add details in the database
    add_button = Button(root, text="Add Info",font=("Arial Rounded MT Bold",12),bg="Dark Red", command=add_details,highlightcolor="Coral", highlightbackground="Coral").grid(row=14,column=0,padx=10,pady=10)

    # Create a function to destroy the current window
    # and display the data from the database in a new window
    def display_data():
        #Create a function to destroy and close the program
        def end_display():
            # Create afunction to display the current window and call the previous window
            final_result.destroy()
            main()
        def end_erase():
            # Query to delete all records from the table in database
            # So that table is empty when the program runs again
            cur.execute("DELETE FROM StdDetails")
            conn.commit()
            messagebox.showinfo("Success","Data successfully deleted")
            end_display()
        #destroy the current window
        root.destroy()
        
        #create a new window
        final_result = Tk()
        final_result.title("Result Generator(PP - III)")

            
        Label(final_result,text="Consolidated Result Sheet", font=("Arial Rounded MT Bold",18),bg="Dark Red").grid(row=0, column=0,  padx=10, columnspan=4, pady=10)
        done = Button(final_result, text="Done",font=("Arial Rounded MT Bold",12),bg="Dark Red",command=end_display).grid(row=1,column=0,padx=10,pady=10)
        erase = Button(final_result, text="Erase All",font=("Arial Rounded MT Bold",12),bg="Dark Red",command=end_erase).grid(row=1,column=1,padx=10,pady=10)
    
        # Create the Treeview to display the data retrieved from database
        tree = ttk.Treeview(final_result, columns=("StdCode", "Name","Class","English","Dzongkha","Maths","ICT","Total","Average","Remark"), show="headings")
        tree.heading("StdCode", text="Student Code")
        tree.heading("Name", text="Name")
        tree.heading("Class", text="Class")
        tree.heading("English", text="English")
        tree.heading("Dzongkha", text="Dzongkha")
        tree.heading("Maths", text="Maths")
        tree.heading("ICT", text="ICT")
        tree.heading("Total", text="Total")
        tree.heading("Average", text="Average")
        tree.heading("Remark", text="Remark")
        tree.column("StdCode", width=200)
        tree.column("Name", width=200)
        tree.column("Class", width=100,anchor="center")
        tree.column("English", width=100,anchor="center")
        tree.column("Dzongkha", width=100,anchor="center")
        tree.column("Maths", width=100,anchor="center")
        tree.column("ICT", width=100,anchor="center")
        tree.column("Total", width=100,anchor="center")
        tree.column("Average", width=100,anchor="center")
        tree.column("Remark", width=100,anchor="center")
        tree.grid(row=2, column=0, columnspan=12)
        # select the data from the table   
        cur.execute("SELECT * FROM StdDetails")
        rows = cur.fetchall()
        # Iterate to display every record from the table
        for row in rows:
            tree.insert("", END, values=row)
    
        final_result.mainloop()

    # Create a button to display the data
    Button(root, text="Display Data",font=("Arial Rounded MT Bold",12),bg="Dark Red", command=display_data,highlightcolor="Coral",highlightbackground="Coral").grid(row=14,column=1,padx=10,pady=10)
    root.mainloop()

    # Close the cursor and connection
    cur.close()
    conn.close()
    
main()
