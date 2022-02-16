import sqlite3
from sqlite3.dbapi2 import Cursor




def Create_Table() :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    cursor.execute('''
    create table if not exists users (
        id INTEGER PRIMARY KEY AUTOINCREMENT ,
        student_id integer (5) UNIQUE ,
        name varchar (50) ,
        family varchar (50) ,
        age integer (3)
        )
    ''')
    conn.commit()
    conn.close()

def Insert(st_id,name,family,age) :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try :
        cursor.execute("insert into users values(Null,?,?,?,?)",(st_id,name,family,age))
        conn.commit()
        conn.close()
    except Exception as e :
        return False    

def Show() :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try :
        cursor.execute("select * from users")
        res = cursor.fetchall()
        conn.close()
        return res
    except Exception as e :
        return False   

def Delete(id) :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try :
        cursor.execute("delete from users where student_id = ?",(id,))
        conn.commit()
        conn.close()
    except Exception as e :
        return False    

def Search(id='',name='',family='',age='') :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try :
        cursor.execute("select * from users where student_id = ? or name = ? or family = ? or age = ?",(id,name,family,age))
        res = cursor.fetchall()
        conn.close()
        return res
    except Exception as e :
        return False  

def Update(st_id,name,family,age,id) :
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    try :
        cursor.execute("update users set student_id = ?, name = ? , family = ? , age = ? where id = ?",(st_id,name,family,age,id))
        conn.commit()
        conn.close()
    except Exception as e :
        return False    




Create_Table()    