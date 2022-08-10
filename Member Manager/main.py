from cProfile import label
from cgitb import text
from cmath import e
from hashlib import new
from telnetlib import DO
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as messagebox
from turtle import bgcolor, left, width
from unicodedata import name
from unittest import result
import mysql.connector as mysql
from datetime import datetime
import sqlite3

root = Tk()
winHeight = 630
winWidth = 1100
winBg = "#404745"
barBg = "#6A7371"


root.iconbitmap('favicon.ico')
root.title('Student Manager')
root.geometry(f"{winWidth}x{winHeight}")
root['background'] = winBg
root.attributes('-alpha',0.97)
root.attributes('-topmost', 0)

# Database Connection
db = 'biet_students_22-23'
conn = sqlite3.connect(f'{db}.db')
cursor = conn.cursor()

filterBg = "#34282C"
radioBg = "#27332F"
radioFg = "#00FFFF"
_filteredItems = []



def CreateTable():
    cursor.execute("""CREATE TABLE if not exists Students_List(
                        id int(8) Primary Key,
                        name varchar(50) Not Null,
                        dept char(3),
                        year char(3),
                        roll char(10) UNIQUE,
                        mobile int(12),
                        amount int(6),
                        performance varchar(20),
                        datetime varchar(20)
                        );
                """)

    conn.commit()
    
def CreateTable_sqlite3():
    cursor.execute("""CREATE TABLE IF NOT EXISTS Students_List(
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        dept TEXT ,
                        year TEXT,
                        roll TEXT NOT NULL UNIQUE,
                        mobile INTEGER,
                        amount INTEGER,
                        performance TEXT,
                        datetime TEXT
                        )
                """)
    conn.commit()

def InputUI():
    
    global name_label
    name_label = Label(root, text='Name: ', font=('Helventica, 16'), bg=winBg, fg='white')
    name_label.pack()
    name_label.place(x=30, y=10)

    global name_input
    name_input = Entry(root, width=50, font=('Helventica, 16'))
    name_input.pack()
    name_input.place(x=250, y=10)


    global dept_label
    dept_label = Label(root, text='Dept: ', font=('Helventica, 16'), bg=winBg, fg='white')
    dept_label.pack()
    dept_label.place(x=30, y=50)

    global dept_input
    dept_input = Entry(root, width=10, font=('Helventica, 16'))
    dept_input.pack()
    dept_input.place(x=250, y=50)


    global year_label
    year_label = Label(root, text='Year: ', font=('Helventica, 16'), bg=winBg, fg='white')
    year_label.pack()
    year_label.place(x=30, y=90)

    global year_input
    year_input = Entry(root, width=10, font=('Helventica, 16'))
    year_input.pack()
    year_input.place(x=250, y=90)


    global roll_label
    roll_label = Label(root, text='Roll: ', font=('Helventica, 16'), bg=winBg, fg='white')
    roll_label.pack()
    roll_label.place(x=30, y=130)

    global roll_input
    roll_input = Entry(root, width=10, font=('Helventica, 16'))
    roll_input.pack()
    roll_input.place(x=250, y=130)


    global mobile_label
    mobile_label = Label(root, text='Mobile: ', font=('Helventica, 16'), bg=winBg, fg='white')
    mobile_label.pack()
    mobile_label.place(x=30, y=170)

    global mobile_input
    mobile_input = Entry(root, width=15, font=('Helventica, 16'))
    mobile_input.pack()
    mobile_input.place(x=250, y=170)


    global amount_label
    amount_label = Label(root, text='Amount: ', font=('Helventica, 16'), bg=winBg, fg='white')
    amount_label.pack()
    amount_label.place(x=30, y=210)

    global amount_input
    amount_input = Entry(root, width=7, font=('Helventica, 16'))
    amount_input.pack()
    amount_input.place(x=250, y=210)


    global preform_label
    preform_label = Label(root, text='Performance: ', font=('Helventica, 16'), bg=winBg, fg='white')
    preform_label.pack()
    preform_label.place(x=30, y=250)

    global preform_input
    preform_input = Entry(root, width=30, font=('Helventica, 16'))
    preform_input.pack()
    preform_input.place(x=250, y=250)

    global search_input
    search_input = Entry(root, width=30, font=('Helventica, 18'), bg='#E4E799')
    search_input.pack()
    search_input.place(x=370, y=310)

def FilterUI():
    filterFrame = Frame(root, width=400, height=180, bg=filterBg)
    filterFrame.pack()
    filterFrame.place(x=550, y=55)
    
    DeptFilterLayout(filterFrame)
    YearFilterLayout(filterFrame)
    
    showFilter = Button(filterFrame, text='Filter', font='Helventica, 16', command=Filter, bg='lightblue')
    showFilter.place(x=130, y=125)
    
    showFilter = Button(filterFrame, text='Reset', font='Helventica, 16', command=Reset, bg='yellow')
    showFilter.place(x=200, y=125)

def DeptFilterLayout(filterFrame):
    r_dept_ce = StringVar()
    global _dept_ce
    _dept_ce = r_dept_ce
    
    r_dept_cse = StringVar()
    global _dept_cse
    _dept_cse = r_dept_cse
    
    r_dept_ece = StringVar()
    global _dept_ece
    _dept_ece = r_dept_ece
    
    r_dept_ee = StringVar()
    global _dept_ee
    _dept_ee = r_dept_ee
    
    r_dept_me = StringVar()
    global _dept_me
    _dept_me = r_dept_me
    
    
    ce_btn = Checkbutton(filterFrame, text='CE', font='Helventica, 14', variable=r_dept_ce, onvalue=1, offvalue=0)
    ce_btn.pack()
    ce_btn.place(x=10, y=10)
    ce_btn.deselect()
    
    cse_btn = Checkbutton(filterFrame, text='CSE', font='Helventica, 14', variable=r_dept_cse, onvalue=1, offvalue=0)
    cse_btn.pack()
    cse_btn.place(x=75, y=10)
    cse_btn.deselect()
    
    ece_btn = Checkbutton(filterFrame, text='ECE', font='Helventica, 14', variable=r_dept_ece, onvalue=1, offvalue=0)
    ece_btn.pack()
    ece_btn.place(x=152, y=10)
    ece_btn.deselect()
    
    ee_btn = Checkbutton(filterFrame, text='EE', font='Helventica, 14', variable=r_dept_ee, onvalue=1, offvalue=0)
    ee_btn.pack()
    ee_btn.place(x=229, y=10)
    ee_btn.deselect()
    
    me_btn = Checkbutton(filterFrame, text='ME', font='Helventica, 14', variable=r_dept_me, onvalue=1, offvalue=0)
    me_btn.pack()
    me_btn.place(x=292, y=10)
    me_btn.deselect()

def YearFilterLayout(filterFrame):
    r_year_1st = StringVar()
    global _year_1st
    _year_1st = r_year_1st
    
    r_year_2nd = StringVar()
    global _year_2nd
    _year_2nd = r_year_2nd
    
    r_year_3rd = StringVar()
    global _year_3rd
    _year_3rd = r_year_3rd
    
    r_year_4th = StringVar()
    global _year_4th
    _year_4th = r_year_4th
    
    
    firstYear = Checkbutton(filterFrame, text='1st', font='Helventica, 14', variable=r_year_1st, onvalue=1, offvalue=0)
    firstYear.pack()
    firstYear.place(x=10, y=55)
    firstYear.deselect()
    
    secondYear = Checkbutton(filterFrame, text='2nd', font='Helventica, 14', variable=r_year_2nd, onvalue=1, offvalue=0)
    secondYear.pack()
    secondYear.place(x=73, y=55)
    secondYear.deselect()
    
    thirdYear = Checkbutton(filterFrame, text='3rd', font='Helventica, 14', variable=r_year_3rd, onvalue=1, offvalue=0)
    thirdYear.pack()
    thirdYear.place(x=141, y=55)
    thirdYear.deselect()
    
    fourthYear = Checkbutton(filterFrame, text='4th', font='Helventica, 14', variable=r_year_4th, onvalue=1, offvalue=0)
    fourthYear.pack()
    fourthYear.place(x=205, y=55)
    fourthYear.deselect()

def Filter():
    CleanTree()
    
    Get_CE_Dept()
    Get_CSE_Dept()
    Get_ECE_Dept()
    Get_EE_Dept()
    Get_ME_Dept()
    
    Get_1st_Year()
    Get_2nd_Year()
    Get_3rd_Year()
    Get_4th_Year()
    
    if _dept_ce.get() == '0' and _dept_cse.get() == '0' and _dept_ece.get() == '0' and _dept_ee.get() == '0' and _dept_ee.get() == '0' and _year_1st.get() == '0' and _year_2nd.get() == '0' and _year_3rd.get() == '0' and _year_4th.get() == '0':

        TreeView()
        return
        
        
    
    
    _newFilteredItems =[]
    
    for row in _filteredItems:
        if row not in _newFilteredItems:
            _newFilteredItems.append(row)
            
    InsertInTree(_newFilteredItems)
    _filteredItems.clear()


def Get_CE_Dept():
    try:
        if (_dept_ce.get() == '1'):
            sql = "SELECT * FROM Students_List WHERE dept=?"
            values=('CE',)
        
            cursor.execute(sql,values)
            ceResult = cursor.fetchall()
            conn.commit()
            AppendFilteredItem(ceResult, _filteredItems)
    except:
        pass
    

def Get_CSE_Dept():
    if (_dept_cse.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE dept=?"
        values=('CSE',)

        cursor.execute(sql,values)
        cseResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(cseResult, _filteredItems)
    else:
        pass

def Get_ECE_Dept():
    if (_dept_ece.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE dept=?"
        values=('ECE',)

        cursor.execute(sql,values)
        eceResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(eceResult, _filteredItems)
    else:
        pass

def Get_EE_Dept():
    if (_dept_ee.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE dept=?"
        values=('EE',)

        cursor.execute(sql,values)
        eeResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(eeResult, _filteredItems)
    else:
        pass

def Get_ME_Dept():
    if (_dept_me.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE dept=?"
        values=('ME',)

        cursor.execute(sql,values)
        meResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(meResult, _filteredItems)
    else:
        pass

def Get_1st_Year():
    if (_year_1st.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE year=?"
        values=('1st',)

        cursor.execute(sql,values)
        _1stResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(_1stResult, _filteredItems)
    else:
        pass

def Get_2nd_Year():
    if (_year_2nd.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE year=?"
        values=('2nd',)

        cursor.execute(sql,values)
        _2ndResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(_2ndResult, _filteredItems)
    else:
        pass

def Get_3rd_Year():
    if (_year_3rd.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE year=?"
        values=('3rd',)

        cursor.execute(sql,values)
        _3rdResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(_3rdResult, _filteredItems)

def Get_4th_Year():
    if (_year_4th.get() == '1'):
        sql = "SELECT * FROM Students_List WHERE year=?"
        values=('4th',)

        cursor.execute(sql,values)
        _4thResult = cursor.fetchall()
        conn.commit()
        AppendFilteredItem(_4thResult, _filteredItems)
    
def AppendFilteredItem(result, list):
    for row in result:
        list.append(row)
        
    return list

def Reset():
    pass

def ftDeptClicked():
    pass
def ftYearClicked():
    pass

def AddData():
    id, name, dept, year, roll, mobile, amount, perform, timeStump = InputDataSet()
    
    if name == "" and dept == "" and year == "" and roll == "" and mobile == "" and amount == "" and perform == "":
        return

    if mobile != '':
        if(IsInt(mobile) == False):
            messagebox.showerror("Error!", "Mobile takes Integer only.")
        
    if amount != '':   
        if(IsInt(amount) == False):
            messagebox.showerror("Error!", "Amount takes Integer only.")
        
    if name == "" or roll == "":
        messagebox.showerror("Error!", "Name & Roll can't be blank.")
        
    elif(checkRoll(roll) == False):
        messagebox.showerror("Error!", f"Roll No - {roll} is allready in record")
    else:
        try:
            sql = "INSERT INTO Students_List (name,dept,year,roll,mobile,amount,performance,datetime)VALUES(?,?,?,?,?,?,?,?)"
            input_data = (name, dept, year, roll, mobile, amount, perform,timeStump)
            cursor.execute(sql, input_data)
            conn.commit()
            messagebox.showinfo("Success!", f"Record of {name} added Successfully!")
            ClearForm()
        except Exception as e:
            messagebox.showerror("Error!", e)
    
    TreeView()

def InputDataSet():
    cursor.execute("SELECT count(*) FROM students_list")
    rowCount = cursor.fetchall()

    id = rowCount[0][0] + 1
    name = name_input.get().upper()
    dept = dept_input.get().upper()
    year = year_input.get().lower()
    roll = roll_input.get().upper()
    mobile = mobile_input.get()
    amount = amount_input.get()
    perform = preform_input.get().upper()
    timeStump = datetime.now().strftime('%d-%m-%Y %H:%M:%S')
    
    try:
        mobile = int(mobile)
        amount = int(amount)
    except Exception as e:
        pass
    
    return id,name,dept,year,roll,mobile,amount,perform,timeStump

def ClearForm():
    name_input.delete(0,END)
    dept_input.delete(0,END)
    year_input.delete(0,END)
    roll_input.delete(0,END)
    mobile_input.delete(0,END)
    amount_input.delete(0,END)
    preform_input.delete(0,END)
    
    name_input.focus()

def DeleteData():
    confirmation = messagebox.askyesno('Delete Record', 'Do you want to delete selected items permanently?')
    if (confirmation == True):
        selectedItem = treeView.selection()[0]
        selectedRow = treeView.item(selectedItem)['values']
        roll = selectedRow[4]
        sql = 'DELETE FROM Students_List WHERE roll = ?'
        values = (roll,)
        cursor.execute(sql, values)
        conn.commit()
        
        TreeView()
    
def EditData():
    ClearForm()
    
    if treeView.selection() == ():
        return
    
    
    selectedItem = treeView.selection()[0]
    selectedRow = treeView.item(selectedItem)['values']
    roll = selectedRow[4]
    
    EditData.saveBtn = Button(root, text='Save', font='Helventica, 18', command=SaveData, bg='lightgreen')
    saveBtn = EditData.saveBtn
    saveBtn.pack()
    saveBtn.place(x=270, y=310)
    
    selectedItem = treeView.selection()[0]
    selectedRow = treeView.item(selectedItem)['values']
    roll = selectedRow[4]
    
    sql = 'SELECT * FROM Students_List WHERE roll = ?'
    values = (roll,)
    
    cursor.execute(sql, values)
    r = cursor.fetchall()
    
    EditData.result = r[0]
    result = EditData.result
    conn.commit()
    
    
    try:
        name_input.insert(0, result[1])
        dept_input.insert(0, result[2])
        year_input.insert(0, result[3])
        roll_input.insert(0, result[4])
        mobile_input.insert(0, result[5])
        amount_input.insert(0, result[6])
        preform_input.insert(0, result[7])
    except:
        pass

def SaveData():
    conf = messagebox.askyesno('Edit', 'Do you want to edit selected?')
    if conf == True:
        pass
    elif(conf == False):
        return
    
    
    try:
        _name = name_input.get().upper()
        _dept = dept_input.get().upper()
        _year = year_input.get().lower()
        _roll = roll_input.get().upper()
        _mobile = mobile_input.get()
        _amount = amount_input.get()
        _perform = preform_input.get().upper()
        
        sql2 = 'UPDATE Students_List SET name=?, dept=?, year=?, roll=?, mobile=?, amount=?, performance=? WHERE id=?'
        values = (_name, _dept, _year, _roll, _mobile, _amount, _perform, EditData.result[0])
        
        
        cursor.execute(sql2, values)
        conn.commit()
        saveBtn = EditData.saveBtn
        saveBtn.destroy()
        
        ClearForm()
        TreeView()
        
    except Exception as e:
        messagebox.showerror("Error!", "Check data & Try again")

def SearchData():
    query = search_input.get().lower()
    if query == '':
        return
    
    global refreshBtn
    refreshBtn = Button(search_input, text='X', font='Helventica, 12', command=CloseSearch, bg='#E4E799', cursor='arrow')
    refreshBtn.pack()
    refreshBtn.place(x=370, y=0)
    
    
    sql = "SELECT * FROM Students_List WHERE name like ? or roll LIKE ?"
    query = f"%{query}%"
    values = (query, query)
    
    cursor.execute(sql, values)
    result = cursor.fetchall()
    conn.commit()
    CleanTree()
    
    # Enter Fiend data in tree
    InsertInTree(result)
    
def Buttons():
    addBtn = Button(root, text='Add', font='Helventica, 18', command=AddData, bg='lightblue')
    addBtn.pack()
    addBtn.place(x=30, y=310)


    editBtn = Button(root, text='Edit', font='Helventica, 18', command=EditData, bg='yellow')
    editBtn.pack()
    editBtn.place(x=100, y=310)


    DeleteBtn = Button(root, text='Delete', font='Helventica, 18', command=DeleteData, bg='red')
    DeleteBtn.pack()
    DeleteBtn.place(x=170, y=310)

    
    searchBtn = Button(root, text='Search', font='Helventica, 18', command=SearchData, bg='lightblue')
    searchBtn.pack()
    searchBtn.place(x=770, y=310)

def CloseSearch():
    TreeView()
    search_input.delete(0, END)
    refreshBtn.destroy()

def TreeView():
    global treeView
    treeView = ttk.Treeview(root)
    treeView.pack()
    treeView.place(x=30, y=390)
    treeView['columns'] = ('Id', 'Name', 'Dept', 'Year','Roll','Mobile','Amount','Performance')
    
    Columns(treeView)
    Headings(treeView)
    
    cursor.execute("SELECT * FROM Students_List")
    result = cursor.fetchall()
    conn.commit()
    
    InsertInTree(result)

def CleanTree():
    for data in treeView.get_children():
        treeView.delete(data)

def Columns(treeView):
    treeView.column('#0', width=0, minwidth=0)
    treeView.column('Id', width=80, anchor=CENTER)
    treeView.column('Name', width=210, anchor=W)
    treeView.column('Dept', width=115, anchor=W)
    treeView.column('Year', width=110, anchor=W)
    treeView.column('Roll', width=130, anchor=W)
    treeView.column('Mobile', width=150, anchor=W)
    treeView.column('Amount', width=100, anchor=W)
    treeView.column('Performance', width=140, anchor=W)

def Headings(treeView):
    treeView.heading('#0', text='')
    treeView.heading('Id', text='Id', anchor=CENTER)
    treeView.heading('Name', text='Student Name', anchor=W)
    treeView.heading('Dept', text='Department', anchor=W)
    treeView.heading('Year', text='Year', anchor=W)
    treeView.heading('Roll', text='Roll', anchor=W)
    treeView.heading('Mobile', text='Mobile', anchor=W)
    treeView.heading('Amount', text='Amount', anchor=W)
    treeView.heading('Performance', text='Performance', anchor=W)
    
def InsertInTree(result):
    id=1
    for row in result:
        if id%2 == 0:
            treeView.insert(parent='',tags=('even',), index='end', iid=id, text='', values=(id  , row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        else:
            treeView.insert(parent='',tags=('odd',), index='end', iid=id, text='', values=(id  , row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
        
        id += 1
        treeView.tag_configure('even', foreground='black', background='white')
        treeView.tag_configure('odd', foreground='black', background='lightgray')

def IsInt(a):

    if type(a) == int:
        return True
    else:
        return False

def checkRoll(roll):
    values = (roll,)
    sql = 'SELECT * FROM Students_List WHERE roll=?'
    
    cursor.execute(sql, values)
    r = cursor.fetchall()
    conn.commit()
    
    for data in r:
        if data[4] == roll:
            return False
        else:
            return True

    

# Call Func...
CreateTable_sqlite3()
InputUI()
FilterUI()
Buttons()
TreeView()

root.mainloop()













#(<(o)>)#

#   Add         Edit        Delete       |O==|       Search

#   id      Name       Dept        year        Roll        Mobile          Amount          Performance         TimeStamp

#   Add         Edit        Delete       |O==|       Search

#(<(o)>)#