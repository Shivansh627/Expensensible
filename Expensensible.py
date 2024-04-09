import tkinter as tk
# from PIL import Image,ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#list
a=[]
b=[]
c=[]
#show Income
def showincome():
    user_input=Income.get()

    if user_input!=None:
        show.insert(tk.END,f": ₹{user_input}\n")
    c.append(Income.get())

#show expense
def showexpense():
    u1=cat.get()
    u2=exx.get()
    if u1!=None:
        listbox.insert(tk.END,f"{u1}: ₹{u2}\n")
    
    a.append(ex.get())
    b.append(cat.get())    
   
  

    Income.delete(0,tk.END)
    cat.delete(0,tk.END)
    exx.delete(0,tk.END)



#remove item
def remove_item():
    selected_index = show.curselection()
    if selected_index:
        show.delete(selected_index)

    

#total expense
def TotalExpense():
    Exp.delete(0,tk.END)
    s=sum(a)
    Exp.insert(tk.END,s)

#plot graph
def plot_graph():
   
    ax.pie(a,labels=b,autopct='%1.1f%%')
    ax.set_title('Expense Distribution')
    canvas.draw()



#window
expense=tk.Tk()
expense.title("Expensensible")
# expense.resizable(False,False)
expense.geometry("1100x800")
expense.configure(bg="#44CCFF")

#label
image=tk.PhotoImage(file=r"C:\Users\shukl\OneDrive\Pictures\project\Untitled design (1).png")
label=tk.Label(expense,image=image,background="#44CCFF")
label.pack()

expense.iconphoto(False,image)
frame=tk.Frame(expense)
frame.pack()

#income text
label4=tk.Label(expense,text="Income",font=("bold",24),bg="#44CCFF")
label4.place(x=45,y=110)
label5=tk.Label(expense,text="Expenses",font=("bold",24),bg="#44CCFF")
label5.place(x=210,y=110)


#income
income= vars()
exp= vars()

Income=tk.Entry(expense,textvariable=income,width=7,font="arial 30",bg="#44CCFF",justify="center")
Income.place(x=40,y=155)

Exp=tk.Listbox(expense,height=1,width=7,font="arial 30",bg="#44CCFF",justify="center",border=0)
Exp.place(x=205,y=155)


#button
button1 = tk.Button(expense, text="Show Income", command=showincome , bg="#44CCFF")
button1.place(x=150,y=220)

button = tk.Button(expense, text="Show Expense", command=showexpense , bg="#44CCFF")
button.place(x=150,y=370)


#show income
show = tk.Listbox(expense,bg="#44CCFF",justify="right",bd=0)
show.place(x=45,y=410)

sshow=tk.Label(expense,text="Income is  ",bd=0,bg="#44ccff")
sshow.place(x=47,y=411)


#listbox
listbox=tk.Listbox(expense,bg="#44CCFF",bd=0,border=0)
listbox.place(x=170,y=410)

#remove button
remove=tk.Button(expense,text="Remove Data",bg="#44CCFF",command=remove_item)
remove.place(x=50,y=600)

#categories
cate=vars()
cat=tk.Entry(expense,textvariable=cate,width=25,bg="#44CCFF",justify="right")
cat.place(x=40,y=285)

categ=tk.Label(expense,text="Category:",bd=0,bg="#44CCFF")
categ.place(x=42,y=266)

#expenses
ex=tk.IntVar()
exep=tk.Label(expense,text="Add Expense:",bd=0,bg="#44CCFF")
exep.place(x=42,y=306)

exx=tk.Entry(expense,textvariable=ex,width=25,bg="#44CCFF",justify="right")
exx.place(x=40,y=325)

rup=tk.Label(expense,text="₹",bd=0,bg="#44CCFF")
rup.place(x=41,y=326)

#total button
tot=tk.Button(expense,text="total enpense",bg="#44CCFF", command=TotalExpense)
tot.place(x=132,y=600)

#canvas
fig, ax=plt.subplots()
canvas=FigureCanvasTkAgg(fig,master=expense)
canvas.get_tk_widget().place(x=430,y=200)

#plot button
plot=tk.Button(expense,text="Plot Graph",bg="#44CCFF", command=plot_graph)
plot.place(x=215,y=600)
expense.mainloop()
