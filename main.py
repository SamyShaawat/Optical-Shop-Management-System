from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox, filedialog
import csv
import os
import sqlite3

db = "visions.db"
mydata = []


class shop:
    def __init__(self, root):
        self.root = root
        self.root.title(" Opticals ")
        self.root.geometry("1390x740+0+0")

        title = Label(
            self.root,
            text="Gamya Visions",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="blue",
        )
        title.pack(side=TOP, fill=X)

        self.OrderNo_var = StringVar()
        self.Orderdate_var = StringVar()
        self.Name_var = StringVar()
        self.Phone_var = StringVar()
        self.Age_var = StringVar()
        self.Gender_var = StringVar()
        self.Lenstype_var = StringVar()
        self.Fsize_var = StringVar()
        self.Total_var = StringVar()
        self.Amount_var = StringVar()
        self.Balance_var = StringVar()
        self.Remarks_var = StringVar()
        self.sph1_var = StringVar()
        self.sph2_var = StringVar()
        self.cyl1_var = StringVar()
        self.cyl2_var = StringVar()
        self.axis1_var = StringVar()
        self.axis2_var = StringVar()
        self.add1_var = StringVar()
        self.add2_var = StringVar()
        self.pd1_var = StringVar()
        self.pd2_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Manage_Frame.place(x=2, y=35, width=500, height=700)

        m_title = Label(
            Manage_Frame,
            text="Customer Details",
            font=("times new roman", 17, "bold"),
            bg="white",
            fg="black",
        )
        m_title.grid(row=0, columnspan=2, pady=0)

        orderno = Label(
            Manage_Frame,
            text="Order No:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        orderno.grid(row=1, column=1, pady=4, sticky=W + N)

        orderno_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.OrderNo_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        orderno_enter.grid(row=1, column=2, pady=4, sticky=W + N)

        date = Label(
            Manage_Frame,
            text="Order Date:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        date.grid(row=2, column=1, pady=4, sticky=W + N)

        date_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Orderdate_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        date_enter.grid(row=2, column=2, pady=4, sticky=W + N)

        name = Label(
            Manage_Frame,
            text="Name:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        name.grid(row=3, column=1, pady=4, sticky=W + N)

        name_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Name_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        name_enter.grid(row=3, column=2, pady=4, sticky=W + N)

        phone = Label(
            Manage_Frame,
            text="Phone:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        phone.grid(row=4, column=1, pady=4, sticky=W + N)

        phone_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Phone_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        phone_enter.grid(row=4, column=2, pady=4, sticky=W + N)

        age = Label(
            Manage_Frame,
            text="Age:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        age.grid(row=5, column=1, pady=4, sticky=W + N)

        age_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Age_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        age_enter.grid(row=5, column=2, pady=4, sticky=W + N)

        gender = Label(
            Manage_Frame,
            text="Gender:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        gender.grid(row=6, column=1, pady=4, sticky=W + N)

        gender_entry = ttk.Combobox(
            Manage_Frame,
            width=27,
            textvariable=self.Gender_var,
            font=("times new roman", 15, "bold"),
        )
        gender_entry["values"] = ("Male", "Female", "Others")
        gender_entry.grid(row=6, column=2, padx=0, pady=10)

        total = Label(
            Manage_Frame,
            text="Total:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        total.grid(row=7, column=1, pady=4, sticky=W + N)

        total_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Total_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        total_enter.grid(row=7, column=2, pady=4, sticky=W + N)

        amount = Label(
            Manage_Frame,
            text="Advance:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        amount.grid(row=8, column=1, pady=4, sticky=W + N)

        amount_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Amount_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        amount_enter.grid(row=8, column=2, pady=4, sticky=W + N)

        balance = Label(
            Manage_Frame,
            text="Balance:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        balance.grid(row=9, column=1, pady=4, sticky=W + N)

        balance_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Balance_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        balance_enter.grid(row=9, column=2, pady=4, sticky=W + N)

        ltype = Label(
            Manage_Frame,
            text="Lens Type:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        ltype.grid(row=10, column=1, pady=10, sticky=W + N)

        ltype_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Lenstype_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        ltype_enter.grid(row=10, column=2, pady=10, sticky=W + N)

        ftype = Label(
            Manage_Frame,
            text="Frame Size:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        ftype.grid(row=11, column=1, pady=10, sticky=W + N)

        ftype_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Fsize_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        ftype_enter.grid(row=11, column=2, pady=10, sticky=W + N)

        # details
        pres1_Frame = Frame(Manage_Frame, bd=2, relief=RIDGE, bg="white")
        pres1_Frame.place(x=8, y=540, width=455, height=140)

        od = Label(
            pres1_Frame,
            text="O.D",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=13, column=0, pady=4, sticky=W + N)

        os = Label(
            pres1_Frame,
            text="O.S",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        os.grid(row=14, column=0, pady=4, sticky=W + N)

        od = Label(
            pres1_Frame,
            text="sph",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=12, column=1, pady=16, padx=20, sticky=W + N)

        sph1 = Entry(
            pres1_Frame,
            textvariable=self.sph1_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        sph1.grid(row=13, column=1, padx=5, sticky=W + N)

        sph2 = Entry(
            pres1_Frame,
            textvariable=self.sph2_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        sph2.grid(row=14, column=1, padx=5, sticky=W + N)

        od = Label(
            pres1_Frame,
            text="cyl",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=12, column=2, pady=16, padx=20, sticky=W)

        cyl_Frame = Frame(pres1_Frame, bd=0, relief=RIDGE, bg="white")
        cyl_Frame.place(x=115, y=60, width=74, height=76)

        cyl1 = Entry(
            cyl_Frame,
            textvariable=self.cyl1_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        cyl1.grid(row=15, column=2, padx=0, pady=0, sticky=W + N)

        cyl2 = Entry(
            cyl_Frame,
            textvariable=self.cyl2_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        cyl2.grid(row=16, column=2, padx=0, pady=6, sticky=W + N)

        od = Label(
            pres1_Frame,
            text="axis",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=12, column=3, pady=16, padx=20, sticky=W)

        axis_Frame = Frame(pres1_Frame, bd=0, relief=RIDGE, bg="white")
        axis_Frame.place(x=185, y=60, width=74, height=76)

        axis1 = Entry(
            axis_Frame,
            textvariable=self.axis1_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        axis1.grid(row=17, column=3, padx=5, sticky=W + N)

        axis2 = Entry(
            axis_Frame,
            textvariable=self.axis2_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        axis2.grid(row=18, column=3, padx=5, pady=6, sticky=W + N)

        od = Label(
            pres1_Frame,
            text="add",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=12, column=4, pady=16, padx=20, sticky=W)

        add_Frame = Frame(pres1_Frame, bd=0, relief=RIDGE, bg="white")
        add_Frame.place(x=260, y=60, width=74, height=76)

        add1 = Entry(
            add_Frame,
            textvariable=self.add1_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        add1.grid(row=25, column=4, padx=5, sticky=W + N)

        add2 = Entry(
            add_Frame,
            textvariable=self.add2_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        add2.grid(row=26, column=4, padx=5, pady=6, sticky=W + N)

        od = Label(
            pres1_Frame,
            text="pd",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        od.grid(row=12, column=5, pady=16, padx=20, sticky=W)

        pd_Frame = Frame(pres1_Frame, bd=0, relief=RIDGE, bg="white")
        pd_Frame.place(x=335, y=60, width=74, height=76)

        pd1 = Entry(
            pd_Frame,
            textvariable=self.pd1_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        pd1.grid(row=25, column=5, padx=5, sticky=W + N)

        pd2 = Entry(
            pd_Frame,
            textvariable=self.pd2_var,
            bg="white",
            width=6,
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        pd2.grid(row=26, column=5, padx=5, pady=6, sticky=W + N)

        remarks = Label(
            Manage_Frame,
            text="Remarks:",
            bg="white",
            fg="blue",
            font=("times new roman", 15, "bold"),
        )
        remarks.grid(row=12, column=1, pady=10, sticky=W + N)

        remarks_enter = Entry(
            Manage_Frame,
            width=28,
            textvariable=self.Remarks_var,
            bg="white",
            fg="black",
            font=("times new roman", 15, "bold"),
        )
        remarks_enter.grid(row=12, column=2, pady=10, sticky=W + N)

        # details frame
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="white")
        Detail_Frame.place(x=500, y=37, width=1000, height=700)

        search = Label(
            Detail_Frame,
            text="Search_by:",
            bg="white",
            font=("times new Roman", 14, "bold"),
        )
        search.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        combo_box = ttk.Combobox(
            Detail_Frame,
            textvariable=self.search_by,
            width=10,
            font=("times new Roman", 14, "bold"),
            state="readonly",
        )
        combo_box["values"] = ("Name", "Phone")
        combo_box.grid(row=0, column=1, padx=0, pady=10)

        search_box = Entry(
            Detail_Frame,
            textvariable=self.search_text,
            font=("times new Roman", 15, "bold"),
            bd=2,
            relief=GROOVE,
        )
        search_box.grid(row=0, column=2, padx=10, sticky="w")

        searchd = Button(
            Detail_Frame,
            command=self.search_data,
            text="Search",
            width=5,
            height=1,
            bg="orange",
        ).grid(row=0, column=3, padx=10)
        show = Button(
            Detail_Frame,
            command=self.fetch_data,
            text="Show_all",
            width=5,
            height=1,
            bg="orange",
        ).grid(row=0, column=4, padx=10)

        rel = Button(
            Detail_Frame,
            text="Reload",
            command=self.refresh_data,
            width=5,
            height=1,
            bg="orange",
        )
        rel.grid(row=0, column=5, padx=10)
        # button frame
        but_Frame = Frame(Detail_Frame, bd=2, relief=RIDGE, bg="skyblue")
        but_Frame.place(x=5, y=540, width=750, height=120)

        save = Button(
            but_Frame,
            text="Add",
            command=self.add_customer,
            width=7,
            height=2,
            bg="orange",
        ).grid(row=1, column=0, padx=30, pady=30)
        clear = Button(
            but_Frame, text="Clear", command=self.clear, width=7, height=2, bg="orange"
        ).grid(row=1, column=1, padx=30)
        update = Button(
            but_Frame,
            text="Update",
            command=self.update_data,
            width=7,
            height=2,
            bg="orange",
        ).grid(row=1, column=2, padx=30)
        delete = Button(
            but_Frame,
            text="Delete",
            command=self.delete_data,
            width=7,
            height=2,
            bg="orange",
        ).grid(row=1, column=3, padx=30)

        export_data = Button(
            but_Frame,
            text="Export",
            width=7,
            height=2,
            bg="orange",
            command=self.export_data,
        ).grid(row=1, column=4, padx=30)

        # table frame

        table_frame = Frame(Detail_Frame, bd=2, relief=GROOVE, bg="white")
        table_frame.place(x=5, y=40, width=850, height=480)

        scroll_x = Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(table_frame, orient=VERTICAL)
        self.Customer_table = ttk.Treeview(
            table_frame,
            columns=(
                "OrderNo",
                "Date",
                "Name",
                "Phone",
                "Age",
                "Gender",
                "Total",
                "Amount",
                "Balance",
                "Lens Type",
                "Frame size",
                "Remarks",
                "sph1",
                "sph2",
                "cyl1",
                "cyl2",
                "axis1",
                "axis2",
                "add1",
                "add2",
                "pd1",
                "pd2",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
        )
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Customer_table.xview)
        scroll_y.config(command=self.Customer_table.yview)
        self.Customer_table.heading("OrderNo", text="OrderNo:")
        self.Customer_table.heading("Date", text="Date:")
        self.Customer_table.heading("Name", text="Name:")
        self.Customer_table.heading("Phone", text="Phone:")
        self.Customer_table.heading("Age", text="Age:")
        self.Customer_table.heading("Gender", text="Gender:")
        self.Customer_table.heading("Total", text="Total:")
        self.Customer_table.heading("Amount", text="Advance:")
        self.Customer_table.heading("Balance", text="Balance:")
        self.Customer_table.heading("Lens Type", text="Lens Type:")
        self.Customer_table.heading("Frame size", text="Frame Size:")
        self.Customer_table.heading("Remarks", text="Remarks:")
        self.Customer_table.heading("sph1", text="sph1:")
        self.Customer_table.heading("sph2", text="sph2:")
        self.Customer_table.heading("cyl1", text="cyl1:")
        self.Customer_table.heading("cyl2", text="cyl2:")
        self.Customer_table.heading("axis1", text="axis1:")
        self.Customer_table.heading("axis2", text="axis2:")
        self.Customer_table.heading("add1", text="add1:")
        self.Customer_table.heading("add2", text="add2:")
        self.Customer_table.heading("pd1", text="pd1:")
        self.Customer_table.heading("pd2", text="pd2:")

        self.Customer_table["show"] = "headings"
        self.Customer_table.column("OrderNo", width=140)
        self.Customer_table.column("Date", width=110)
        self.Customer_table.column("Name", width=170)
        self.Customer_table.column("Phone", width=150)
        self.Customer_table.column("Age", width=80)
        self.Customer_table.column("Gender", width=100)
        self.Customer_table.column("Total", width=150)
        self.Customer_table.column("Amount", width=150)
        self.Customer_table.column("Balance", width=150)
        self.Customer_table.column("Lens Type", width=170)
        self.Customer_table.column("Frame size", width=170)
        self.Customer_table.column("Remarks", width=170)
        self.Customer_table.column("sph1", width=80)
        self.Customer_table.column("sph2", width=80)
        self.Customer_table.column("cyl1", width=80)
        self.Customer_table.column("cyl2", width=80)
        self.Customer_table.column("axis1", width=80)
        self.Customer_table.column("axis2", width=80)
        self.Customer_table.column("add1", width=80)
        self.Customer_table.column("add2", width=80)
        self.Customer_table.column("pd1", width=80)
        self.Customer_table.column("pd2", width=80)
        self.Customer_table.pack(fill=BOTH, expand=1)
        self.Customer_table.bind("<ButtonRelease-1>", self.get_cursor)

        self.create_table()
        self.fetch_data()

    def create_table(self):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers (
                    orderno TEXT, 
                    date TEXT, 
                    name TEXT, 
                    phone TEXT, 
                    age TEXT, 
                    gender TEXT, 
                    total TEXT, 
                    advance TEXT, 
                    balance TEXT, 
                    ltype TEXT, 
                    fsize TEXT, 
                    remarks TEXT, 
                    sph1 TEXT, 
                    sph2 TEXT, 
                    cyl1 TEXT, 
                    cyl2 TEXT, 
                    axis1 TEXT, 
                    axis2 TEXT, 
                    add1 TEXT, 
                    add2 TEXT, 
                    pd1 TEXT, 
                    pd2 TEXT)"""
        )
        conn.commit()
        conn.close()

    def add_customer(self):
        if self.Phone_var.get() == "" or self.Name_var.get() == "":
            messagebox.showerror("Error", "All fields are required!!")
        else:
            conn = sqlite3.connect(db)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO customers VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (
                    self.OrderNo_var.get(),
                    self.Orderdate_var.get(),
                    self.Name_var.get(),
                    self.Phone_var.get(),
                    self.Age_var.get(),
                    self.Gender_var.get(),
                    self.Total_var.get(),
                    self.Amount_var.get(),
                    self.Balance_var.get(),
                    self.Lenstype_var.get(),
                    self.Fsize_var.get(),
                    self.Remarks_var.get(),
                    self.sph1_var.get(),
                    self.sph2_var.get(),
                    self.cyl1_var.get(),
                    self.cyl2_var.get(),
                    self.axis1_var.get(),
                    self.axis2_var.get(),
                    self.add1_var.get(),
                    self.add2_var.get(),
                    self.pd1_var.get(),
                    self.pd2_var.get(),
                ),
            )
            self.fetch_data()
            self.clear()
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_data(self):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        global mydata
        mydata = rows
        if len(rows) != 0:
            self.Customer_table.delete(*self.Customer_table.get_children())
            for row in rows:
                self.Customer_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.OrderNo_var.set("")
        self.Orderdate_var.set("")
        self.Name_var.set("")
        self.Phone_var.set("")
        self.Age_var.set("")
        self.Gender_var.set("")
        self.Total_var.set("")
        self.Amount_var.set("")
        self.Balance_var.set("")
        self.Lenstype_var.set("")
        self.Fsize_var.set("")
        self.Remarks_var.set("")
        self.sph1_var.set("")
        self.sph2_var.set("")
        self.cyl1_var.set("")
        self.cyl2_var.set("")
        self.axis1_var.set("")
        self.axis2_var.set("")
        self.add1_var.set("")
        self.add2_var.set("")
        self.pd1_var.set("")
        self.pd2_var.set("")

    def get_cursor(self, eve):
        cursor_row = self.Customer_table.focus()
        contents = self.Customer_table.item(cursor_row)
        row = contents["values"]

        self.OrderNo_var.set(row[0])
        self.Orderdate_var.set(row[1])
        self.Name_var.set(row[2])
        self.Phone_var.set(row[3])
        self.Age_var.set(row[4])
        self.Gender_var.set(row[5])
        self.Total_var.set(row[6])
        self.Amount_var.set(row[7])
        self.Balance_var.set(row[8])
        self.Lenstype_var.set(row[9])
        self.Fsize_var.set(row[10])
        self.Remarks_var.set(row[11])
        self.sph1_var.set(row[12])
        self.sph2_var.set(row[13])
        self.cyl1_var.set(row[14])
        self.cyl2_var.set(row[15])
        self.axis1_var.set(row[16])
        self.axis2_var.set(row[17])
        self.add1_var.set(row[18])
        self.add2_var.set(row[19])
        self.pd1_var.set(row[20])
        self.pd2_var.set(row[21])

    def update_data(self):
        if (
            self.Phone_var.get() == ""
            or self.Name_var.get() == ""
            or self.OrderNo_var.get() == ""
        ):
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = sqlite3.connect(db)
            cur = conn.cursor()
            cur.execute(
                """UPDATE customers SET orderno = ?, date = ?, name = ?, phone = ?, age = ?, gender = ?, total = ?, advance = ?, balance = ?, 
                        ltype = ?, fsize = ?, remarks = ?, sph1 = ?, sph2 = ?, cyl1 = ?, cyl2 = ?, axis1 = ?, axis2 = ?, add1 = ?, add2 = ?, pd1 = ?, pd2 = ? 
                        WHERE orderno = ?""",
                (
                    self.OrderNo_var.get(),
                    self.Orderdate_var.get(),
                    self.Name_var.get(),
                    self.Phone_var.get(),
                    self.Age_var.get(),
                    self.Gender_var.get(),
                    self.Total_var.get(),
                    self.Amount_var.get(),
                    self.Balance_var.get(),
                    self.Lenstype_var.get(),
                    self.Fsize_var.get(),
                    self.Remarks_var.get(),
                    self.sph1_var.get(),
                    self.sph2_var.get(),
                    self.cyl1_var.get(),
                    self.cyl2_var.get(),
                    self.axis1_var.get(),
                    self.axis2_var.get(),
                    self.add1_var.get(),
                    self.add2_var.get(),
                    self.pd1_var.get(),
                    self.pd2_var.get(),
                    self.OrderNo_var.get(),
                ),
            )
            self.fetch_data()
            self.clear()
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Record has been updated")

    def delete_data(self):
        conn = sqlite3.connect(db)
        cursor_row = self.Customer_table.focus()
        contents = self.Customer_table.item(cursor_row)
        if cursor_row:
            cur = conn.cursor()
            cur.execute(
                "DELETE FROM customers WHERE orderno = ?", (self.OrderNo_var.get(),)
            )
            conn.commit()
            conn.close()
            self.fetch_data()
            self.clear()
            messagebox.showinfo("Success", "Record has been deleted successfully")
        else:
            messagebox.showerror("Error", "No data is choosed to delete")

    def search_data(self):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM customers WHERE "
            + str(self.search_by.get())
            + " LIKE '%"
            + str(self.search_text.get())
            + "%'"
        )
        rows = cur.fetchall()

        if len(rows) != 0:
            self.Customer_table.delete(*self.Customer_table.get_children())
            for row in rows:
                self.Customer_table.insert("", END, values=row)
            conn.commit()
        conn.close()

    def export_data(self):
        if len(mydata) < 1:
            messagebox.showerror("Error", "No data found")
            return False
        f = filedialog.asksaveasfilename(
            initialdir=os.getcwd(),
            title="Save CSV",
            filetypes=(("CSV file", "*.csv"), ("All files", "*.*")),
        )
        with open(f, mode="w") as customers_details:
            exp_writer = csv.writer(customers_details, delimiter=",")
            for i in mydata:
                exp_writer.writerow(i)
        messagebox.showinfo(
            "Data exported",
            "Your data has been exported to " + os.path.basename(f) + " successfully",
        )

    def refresh_data(self):
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers")
        rows = cur.fetchall()
        global mydata
        mydata = rows
        if len(rows) != 0:
            self.Customer_table.delete(*self.Customer_table.get_children())
            for row in rows:
                self.Customer_table.insert("", END, values=row)
            conn.commit()
        conn.close()


root = Tk()
ob = shop(root)
root.mainloop()
