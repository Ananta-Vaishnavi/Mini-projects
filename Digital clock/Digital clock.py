from time import strftime
from tkinter import Label,Tk
#window Config for clock
window=Tk()
window.title('DIGITAL CLOCK OF GST')
window.geometry('200x200')
window.config(bg='#610C63')
window.resizable(True,True)
#Label config
clock_label=Label(window,bg='white',fg='red',font=('Helvetica',30,'bold'),relief='flat')
clock_label.place(x=150,y=100)

def updating_label():
  current_time=strftime('%H : %M : %S')
  clock_label.configure(text=current_time)
  clock_label.after(80, updating_label)
updating_label()
window.mainloop()
