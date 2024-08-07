import tkinter
from PIL import Image, ImageTk

root = tkinter.Tk()
root.title('To Do List')
root.geometry('450x600')
root.resizable(False,False)


task_list = []

def add_task():
    task = task_entry.get()
    task_entry.delete(0,tkinter.END)
    if task:
        with open('tasklist.txt','a') as taskfile:
            taskfile.write(f'{task}\n')
        task_list.append(task)
        listbox.insert(tkinter.END,task)


def delete_task():
    global task_list
    task = str(listbox.get(tkinter.ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        listbox.delete(tkinter.ANCHOR)


def edit_task():
    global task_list
    task = str(listbox.get(tkinter.ANCHOR))
    task_entry.insert(0, task)
    listbox.delete(tkinter.ANCHOR)
    if task in task_list:
        index = task_list.index(task)
    def update():
        new_task = task_entry.get()
        task_list[index] = new_task
        with open('tasklist.txt','w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
        update_button.destroy()
        listbox.insert(tkinter.ANCHOR, new_task)
        task_entry.delete(0, tkinter.END)
    update_button = tkinter.Button(frame,text='UPDATE',bg='#7F82BB',font = 'arial 18 bold', width=6,command=update)
    update_button.place(x=350,y=0)

    
def open_task_file():
    try:
        global task_list
        with open('taskfile.txt','r') as taskfile:
            tasks = taskfile.readlines()
        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert('end',task)
    except:
        file = open('tasklist.txt','w')
        file.close()


tasks_icon = tkinter.PhotoImage(file='images/download.png')
root.iconphoto(False,tasks_icon)

topbar_image = tkinter.PhotoImage(file='images/Untitled.png')
tkinter.Label(root, image=topbar_image).pack()

original_image = Image.open('images/task.png')
resized_image = original_image.resize((40, 40)) 
option_image = ImageTk.PhotoImage(resized_image)
tkinter.Label(root, image=option_image, bg='#7F82BB').place(x=250,y=15)


heading = tkinter.Label(root,text='TASKS', fg='white', font='arial 20 bold',bg='#7F82BB')
heading.place(x=140,y=20)

frame = tkinter.Frame(root,width=500,height=50, bg='white')
frame.place(x=0,y=180)

task = tkinter.StringVar()
task_entry = tkinter.Entry(frame,width=18,font='arial 20', bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

add_button = tkinter.Button(frame,text='ADD',bg='#7F82BB',font = 'arial 20 bold', width=6,command=add_task)
add_button.place(x=350,y=0)

frame1 = tkinter.Frame(root, bd=3,width=700,height=300,bg='#7F82BB')
frame1.pack(pady=(160,0))
listbox = tkinter.Listbox(frame1,font='arial',width=45 ,height=15 ,bg='#B4CDCD',fg='black',cursor='hand2',selectbackground='#7F82BB')
listbox.pack(side='left',fill='both',padx=2)
scrollbar = tkinter.Scrollbar(frame1)
scrollbar.pack(side='right',fill='both')

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

open_task_file()

original_bin = Image.open('images/bin.png')
resized_bin = original_bin.resize((35, 35)) 
delete_icon = ImageTk.PhotoImage(resized_bin)
tkinter.Button(root,image=delete_icon,bd=0,command=delete_task).place(x=170,y=550)


original_edit = Image.open('images/edit.png')
resized_edit = original_edit.resize((25,25))
edit_icon = ImageTk.PhotoImage(resized_edit)
tkinter.Button(root,image=edit_icon,command=edit_task).place(x=225,y=550)


root.mainloop()
