from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox

class Employee:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        title = Label(self.root, text="Employee Management System", bd=10, relief=GROOVE,
                      font=("Arial", 40, "bold"), bg="#34495E", fg="white")
        title.pack(side=TOP, fill=X)

        self.eid_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.Contact_var = StringVar()
        self.dob_var = StringVar()
        self.dept_var = StringVar()
        self.joining_date_var = StringVar()
        self.salary_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#87CEEB")
        Manage_Frame.place(x=20, y=100, width=490, height=700)

        m_title = Label(Manage_Frame, text="Manage Employees", bg="#87CEEB", fg="black",
                        font=("Arial", 30, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        fields = [
            ("Employee Id", self.eid_var),
            ("Name", self.name_var),
            ("Email id", self.email_var),
            ("Contact", self.Contact_var),
            ("D.O.B", self.dob_var),
            ("Department", self.dept_var),
            ("Joining Date", self.joining_date_var),
            ("Salary", self.salary_var)
        ]

        for i, (label, var) in enumerate(fields, start=1):
            Label(Manage_Frame, text=label, bg="#87CEEB", fg="black",
                  font=("Arial", 16, "bold")).grid(row=i, column=0, pady=10, padx=20, sticky="w")
            Entry(Manage_Frame, textvariable=var, font=("Arial", 14), bd=5, relief=GROOVE).grid(
                row=i, column=1, pady=10, padx=10, sticky="w")

        Label(Manage_Frame, text="Gender", bg="#87CEEB", fg="black",
              font=("Arial", 16, "bold")).grid(row=9, column=0, pady=10, padx=20, sticky="w")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var,
                                    font=("Arial", 14), state='readonly')
        combo_gender['values'] = ("male", "female", "other")
        combo_gender.grid(row=9, column=1, padx=10, pady=10)

        Label(Manage_Frame, text="Address", bg="#87CEEB", fg="black",
              font=("Arial", 16, "bold")).grid(row=10, column=0, pady=10, padx=20, sticky="w")
        self.txt_Address = Text(Manage_Frame, width=25, height=4, font=("Arial", 12))
        self.txt_Address.grid(row=10, column=1, pady=10, padx=10, sticky="w")

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="#87CEEB")
        Detail_Frame.place(x=550, y=100, width=900, height=700)

        Label(Detail_Frame, text="Search By", bg="#87CEEB", fg="black", font=("Arial", 16, "bold")).grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, width=10, font=("Arial", 14), state='readonly')
        combo_search['values'] = ("eid", "name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=20)
        Entry(Detail_Frame, textvariable=self.search_txt, font=("Arial", 14), bd=5, relief=GROOVE).grid(row=0, column=2, pady=10, padx=20, sticky="w")
        Button(Detail_Frame, text="Search", width=20, pady=5, command=self.search_data, bg="#16A085", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=3, padx=10, pady=10)

        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#87CEEB")
        Table_Frame.place(x=30, y=70, width=800, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Employee_table = ttk.Treeview(Table_Frame,
                                           columns=("eid", "name", "email", "gender", "Contact", "dob", "Address", "department", "joining_date", "salary"),
                                           xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Employee_table.xview)
        scroll_y.config(command=self.Employee_table.yview)

        for col in self.Employee_table["columns"]:
            self.Employee_table.heading(col, text=col.capitalize())
            self.Employee_table.column(col, width=100)

        self.Employee_table["show"] = "headings"
        self.Employee_table.pack(fill=BOTH, expand=1)
        self.Employee_table.bind("<ButtonRelease-1>", self.get_cursor)

        # Button Frame moved to Detail_Frame
        btn_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="#87CEEB")
        btn_Frame.place(x=30, y=560, width=800, height=130)

        Button(btn_Frame, text="Add", width=12, command=self.add_Employee, bg="#27AE60", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)
        Button(btn_Frame, text="Update", width=12, command=self.update_data, bg="#2980B9", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=1, padx=10, pady=10)
        Button(btn_Frame, text="Delete", width=12, command=self.delete_data, bg="#C0392B", fg="white", font=("Arial", 14, "bold")).grid(row=0, column=2, padx=10, pady=10)
        Button(btn_Frame, text="Clear", width=12, command=self.clear, bg="#F39C12", fg="white", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10)
        Button(btn_Frame, text="Show All", width=12, command=self.fetch_data, bg="#8E44AD", fg="white", font=("Arial", 14, "bold")).grid(row=1, column=1, padx=10, pady=10)

        self.fetch_data()

    def add_Employee(self):
        if self.eid_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All fields are required!")
            return
        con = pymysql.connect(host="localhost", user="root", password="Asraut@123", database="EMS")
        cur = con.cursor()
        cur.execute("INSERT INTO Employee2 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
            self.eid_var.get(), self.name_var.get(), self.email_var.get(), self.gender_var.get(),
            self.Contact_var.get(), self.dob_var.get(), self.txt_Address.get('1.0', END),
            self.dept_var.get(), self.joining_date_var.get(), self.salary_var.get()
        ))
        

        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Employee added successfully")
        

    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Asraut@123", database="EMS")
        cur = con.cursor()
        cur.execute("SELECT * FROM Employee2")
        rows = cur.fetchall()
        if rows:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for row in rows:
                self.Employee_table.insert('', END, values=row)
        con.close()

    def clear(self):
        for var in [self.eid_var, self.name_var, self.email_var, self.gender_var,
                    self.Contact_var, self.dob_var, self.dept_var, self.joining_date_var, self.salary_var]:
            var.set("")
        self.txt_Address.delete("1.0", END)

    def get_cursor(self, ev):
        cursor_row = self.Employee_table.focus()
        contents = self.Employee_table.item(cursor_row)
        row = contents['values']
        self.eid_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.Contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0", END)
        self.txt_Address.insert(END, row[6])
        self.dept_var.set(row[7])
        self.joining_date_var.set(row[8])
        self.salary_var.set(row[9])

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Asraut@123", database="EMS")
        cur = con.cursor()
        cur.execute("""UPDATE Employee2 SET name=%s, email=%s, gender=%s, Contact=%s, dob=%s, Address=%s,
                       department=%s, joining_date=%s, salary=%s WHERE eid=%s""", (
            self.name_var.get(), self.email_var.get(), self.gender_var.get(),
            self.Contact_var.get(), self.dob_var.get(), self.txt_Address.get('1.0', END),
            self.dept_var.get(), self.joining_date_var.get(), self.salary_var.get(), self.eid_var.get()))
        con.commit()
        con.close()
        self.fetch_data()
        messagebox.showinfo("Success", "Employee details updated successfully")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Asraut@123", database="EMS")
        cur = con.cursor()
        cur.execute("DELETE FROM Employee2 WHERE eid=%s", (self.eid_var.get(),))
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="Asraut@123", database="EMS")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM Employee2 WHERE {self.search_by.get()} LIKE %s", ('%' + self.search_txt.get() + '%',))
        rows = cur.fetchall()
        if rows:
            self.Employee_table.delete(*self.Employee_table.get_children())
            for row in rows:
                self.Employee_table.insert('', END, values=row)
        con.close()


root = Tk()
app = Employee(root)
root.mainloop()