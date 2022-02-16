from os import name
from tkinter import *
from DataBaseFunctions import *
from tkinter import messagebox
window = Tk()  # Create instance
# Settings
window.title('سیستم ثبت نام دانشجویان')
window.geometry('800x700')

# Labels

name_lb = Label(window, text='نام')
name_lb.grid(row=0, column=0, padx=5, pady=5)

family_lb = Label(window, text='خانوادگی')
family_lb.grid(row=0, column=2, padx=5, pady=5)

id_lb = Label(window, text='شماره دانشجویی')
id_lb.grid(row=1, column=0, padx=5, pady=5)

age_lb = Label(window, text='سن')
age_lb.grid(row=1, column=2, padx=5, pady=5)

# Functions


def insert_user(st_id, name, family, age):
    res = Insert(st_id, name, family, age)
    if res != False:
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        family_entry.delete(0, END)
        age_entry.delete(0, END)
        messagebox.showinfo(
            'تایید ثبت نام', 'دانشجو جدید با موفقیت ثبت نام کرد')
        show_all()    
    else:
        messagebox.showerror('اخطار', 'این شماره دانشجویی قبلا ثبت شده')


def show_all():
    res = Show()
    if res != False:
        lst_box.delete(0, END)
        for i in res:
            lst_box.insert(0, i)

    else:
        messagebox.showerror('اخطار', 'خطایی در واکشی اطلاعات رخ داده')


def get_selected(e):
    global select
    i = lst_box.curselection()[0]
    select = lst_box.get(i)
    id_entry.delete(0, END)
    id_entry.insert(0, select[1])
    name_entry.delete(0, END)
    name_entry.insert(0, select[2])
    family_entry.delete(0, END)
    family_entry.insert(0, select[3])
    age_entry.delete(0, END)
    age_entry.insert(0, select[4])
    


def delete_user():
    id = select
    res = Delete(id[1])
    if res != False:
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        family_entry.delete(0, END)
        age_entry.delete(0, END)
        messagebox.showinfo('تایید حذف', 'دانشجو با موفقیت حذف شد')
        show_all()

    else:
        messagebox.showerror('اخطار', 'خطایی در حذف اطلاعات رخ داده')

def search_user(id,name,family,age) :
    res = Search(id=id,name=name,family=family,age=age)
    if res != False:
        lst_box.delete(0, END)
        for i in res:
            lst_box.insert(0, i)

    else:
        messagebox.showerror('اخطار', 'خطایی در واکشی اطلاعات رخ داده')


def update_user(st_id,name,family,age) :
    id = select[0]
    res = Update(st_id,name,family,age,id)
    if res != False :
        messagebox.showinfo('تایید  بروز رسانی','بروز رسانی با موفقیت انجام شد')
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        family_entry.delete(0, END)
        age_entry.delete(0, END)
        show_all()
    else :
        messagebox.showerror('اخطار','خطایی در بروز رسانی صورت گرفت')    


# Enteries
name_entry = Entry(window)
name_entry.grid(row=0, column=1)

family_entry = Entry(window)
family_entry.grid(row=0, column=3)

id_entry = Entry(window)
id_entry.grid(row=1, column=1)

age_entry = Entry(window)
age_entry.grid(row=1, column=3)

search_entry = Entry(window)
search_entry.grid(row=3, column=3)


lst_box = Listbox(window, width=60, height=30)
lst_box.grid(row=3, column=1, columnspan=1, rowspan=2, padx=10, pady=10)

scroll = Scrollbar(window)
scroll.grid(row=3, column=0)

lst_box.configure(yscrollcommand=scroll.set)
scroll.configure(command=lst_box.yview)

lst_box.bind("<<ListboxSelect>>", get_selected)

# Buttons

add_btn = Button(window, text='افزودن', command=lambda: insert_user(
    id_entry.get(), name_entry.get(), family_entry.get(), age_entry.get()))
add_btn.grid(row=2, column=0)

edit_btn = Button(window, text='ویرایش' , command= lambda : update_user(id_entry.get(), name_entry.get(), family_entry.get(), age_entry.get()))
edit_btn.grid(row=2, column=1)

delete_btn = Button(window, text='حذف',command= lambda : delete_user())
delete_btn.grid(row=2, column=2)

show_all_btn = Button(window, text='نمایش همه', command=lambda: show_all())
show_all_btn.grid(row=2, column=3)

search_btn = Button(window, text='جستجو' , command= lambda : search_user(id=search_entry.get(),name=search_entry.get(),family=search_entry.get(),age=search_entry.get()))
search_btn.grid(row=3, column=2)
# run

window.mainloop()
