import tkinter as tk
from tkinter import ttk

win =tk.Tk()
win.geometry("1350x700+0+0")
win.title(" Student Management System ")

title_label = tk.Label(win, text="Student Management System", font=("Arial", 30, "bold"), border=12, relief=tk.GROOVE, bg="lightgrey")
title_label.pack(side=tk.TOP, fill=tk.X)

detail_frame = tk.LabelFrame(win, text="Enter Details", font=("Arial", 20), bd=12, relief=tk.GROOVE, bg="lightgrey")
detail_frame.place(x=20, y=90, width=420, height=575)

data_frame = tk.Frame(win, bd=12, bg="lightgrey", relief=tk.GROOVE)
data_frame.place(x=475, y=90, width=810, height=575)


#   ====entry box =====

rollno_lbl = tk.Label(detail_frame, text="Roll No", font=("Arial", 15), bg="lightgrey")
rollno_lbl.grid(row=0, column=0, padx=2, pady=2)
rollno_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
rollno_ent.grid(row=0, column=1, padx=2, pady=2)

name_lbl = tk.Label(detail_frame, text="Name", font=("Arial", 15), bg="lightgrey")
name_lbl.grid(row=1, column=0, padx=2, pady=2)
name_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
name_ent.grid(row=1, column=1, padx=2, pady=2)

class_lbl = tk.Label(detail_frame, text="Class", font=("Arial", 15), bg="lightgrey")
class_lbl.grid(row=2, column=0, padx=2, pady=2)
class_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
class_ent.grid(row=2, column=1, padx=2, pady=2)

section_lbl = tk.Label(detail_frame, text="Section", font=("Arial", 15), bg="lightgrey")
section_lbl.grid(row=3, column=0, padx=2, pady=2)
section_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
section_ent.grid(row=3, column=1, padx=2, pady=2)

contact_lbl = tk.Label(detail_frame, text="Contact", font=("Arial", 15), bg="lightgrey")
contact_lbl.grid(row=4, column=0, padx=2, pady=2)
contact_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
contact_ent.grid(row=4, column=1, padx=2, pady=2)

fathersnm_lbl = tk.Label(detail_frame, text="Father's Name", font=("Arial", 15), bg="lightgrey")
fathersnm_lbl.grid(row=5, column=0, padx=2, pady=2)
fathersnm_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
fathersnm_ent.grid(row=5, column=1, padx=2, pady=2)

address_lbl = tk.Label(detail_frame, text="Address", font=("Arial", 15), bg="lightgrey")
address_lbl.grid(row=6, column=0, padx=2, pady=2)
address_ent = tk.Entry(detail_frame, bd=7, font=("arial", 15))
address_ent.grid(row=6, column=1, padx=2, pady=2)









win.mainloop()
