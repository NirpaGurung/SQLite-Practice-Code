import sqlite3

#creat or connect to the database
con = sqlite3.connect("StudentDetails.db")

#create a cursor object - 
cur = con.cursor()

#creata the table using CREATE
#execute() method - It is a method of the cursor object and can be used to execute various types of SQL commands. It takes a singleparameter, which is the SQL statement to be executed.
cur.execute('''create table StudentDetail(StudentCode integer,
                                          Name text,
                                          Gender text,
                                          Class text)''')
#The commit() method is used to save the changes to the disk, making them permanent.
con.commit()
print("Table created")

#Define the list of data to be added - data are saved as tuple
items = [(201, 'Sonam', 'Male', 'XII'),
         (202, 'Karma', 'Female', 'IX'),
         (203, 'Dorji', 'Male', 'X')]

#define SQL Query - insert - add a new data to a table. 
query = 'insert into StudentDetail (StudentCode, Name, Gender, Class) values (?,?,?,?)'

#? - place holder of the value that we want to add later. ? represent the data that will be added later.
cur.executemany(query,items)

con.commit()
print("Data Entered")

#Select SQL query to retrieve all the data from the table.
cur.execute('select * from StudentDetail')

#fetch all the rows in the table.
rows = cur.fetchall() #variable rows contains 3 tuples. 

#iterate through the rows and print the data
#used for loop to display each tuple of every rows.
for row in rows:
    print(row)

#close the cursor and connection   
cur.close()
con.close()
