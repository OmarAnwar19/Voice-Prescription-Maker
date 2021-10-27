import speech_recognition as sr
import pyaudio
from fpdf import FPDF
from datetime import datetime
import random, string, os
from tkinter import *
import webbrowser

r = sr.Recognizer()

loopcounter = 0

def inp_audio():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(text)
        except:
            print("Input not recognized, please try again")
    return (text)

def check_drug():
    while(True):
        print("Drug prescribed:")

        file = open("drugdatabase.txt")
        search_word = str(inp_audio()).upper()

        if(search_word in file.read()):
            print("Drug found.")
            return search_word
            break
        else:
            print("Invalid drug, please try again")

def save_info():

    global firstname_info
    global lastname_info
    global docname_info

    firstname_info = firstname.get()
    lastname_info = lastname.get()
    docname_info = docname.get()

    print("Logged in succesfully!")
    screen.destroy()

def get_loops():

    global loop_qtty

    loop_qtty = loopnumber.get()

    inputscr.destroy()

inputscr = Tk()
inputscr.geometry("500x200")
inputscr.title("Doctor Login")
heading = Label(text="Doctor Login", bg="grey", fg="black", width="500", height="3")
heading.pack()

firstname_text = Label(text="How many prescriptions would you like to make? ", )
firstname_text.place(x=15, y=70)

loopnumber = IntVar()
loop_in = Entry(textvariable=loopnumber, width="30")
loop_in.place(x=15, y=100)

confirmloops = Button(inputscr, text="Confirm", width="30", height="2", command=get_loops, bg="grey")
confirmloops.place(x=15, y=135)

inputscr.mainloop()

while (loopcounter < loop_qtty):
    screen = Tk()
    screen.geometry("500x375")
    screen.title("Doctor Login")
    heading = Label(text="Doctor Login", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    firstname_text = Label(text="Patient first-name", )
    lastname_text = Label(text="Patient last-name", )
    docname_text = Label(text="Doctor name", )
    firstname_text.place(x=15, y=70)
    lastname_text.place(x=15, y=140)
    docname_text.place(x=15, y=210)

    firstname = StringVar()
    lastname = StringVar()
    docname = StringVar()

    firstname_entry = Entry(textvariable=firstname, width="30")
    lastname_entry = Entry(textvariable=lastname, width="30")
    docname_entry = Entry(textvariable=docname, width="30")

    firstname_entry.place(x=15, y=100)
    lastname_entry.place(x=15, y=180)
    docname_entry.place(x=15, y=240)

    register = Button(screen, text="Log in", width="30", height="2", command=save_info, bg="grey")
    register.place(x=15, y=290)

    screen.mainloop()

    global drugperc, drugstr, drugform, drugrefill, druginstr

    drugperc = check_drug()

    print("Perscription strength (mg):")
    drugstr = inp_audio()

    print("Perscription form (tablet, liquid, etc...):")
    drugform = inp_audio()

    print("Perscription refills (#):")
    drugrefill = inp_audio()

    print("Perscription instructions:")
    druginstr = inp_audio()

    from tkinter import *

    def check_info():

        global infocheck
        infocheck = StringVar()

        info_label = Label(text="What is incorrect: ", )
        info_label.place(x=15, y=250)

        info_modify = Entry(textvariable=infocheck, width="30")
        info_modify.place(x=15, y=280)

        infobutton = Button(window, text="Confirm", width="30", height="2", command=editvalues, bg="grey")
        infobutton.place(x=15, y=320)

        print(infocheck.get())

    def editvalues():
        global changeinfo
        changeinfo = StringVar()

        change_label = Label(text="Change info: ", )
        change_label.place(x=260, y=250)

        change_modify = Entry(textvariable=changeinfo, width="30")
        change_modify.place(x=260, y=280)

        if infocheck.get() == "1":
            changebutton = Button(window, text="1) Confirm", width="30", height="2", command=modify_drug_info, bg="grey")
            changebutton.place(x=260, y=320)
        if infocheck.get() == "2":
            changebutton = Button(window, text="2) Confirm", width="30", height="2", command=modify_strength_info, bg="grey")
            changebutton.place(x=260, y=320)
        if infocheck.get() == "3":
            changebutton = Button(window, text="3) Confirm", width="30", height="2", command=modify_form_info, bg="grey")
            changebutton.place(x=260, y=320)
        if infocheck.get() == "4":
            changebutton = Button(window, text="4) Confirm", width="30", height="2", command=modify_refills_info, bg="grey")
            changebutton.place(x=260, y=320)
        if infocheck.get() == "5":
            changebutton = Button(window, text="5) Confirm", width="30", height="2", command=modify_instr_info, bg="grey")
            changebutton.place(x=260, y=320)
        else:
            print("6) Invalid Entry")

    def modify_drug_info():
        drug = changeinfo.get()
        print("Drug changed succesfully!")
        window.destroy()
    def modify_strength_info():
        strength = changeinfo.get()
        print("Drug strength changed succesfully!")
        window.destroy()
    def modify_form_info():
        form = changeinfo.get()
        print("Drug form changed succesfully!")
        window.destroy()
    def modify_refills_info():
        refills = changeinfo.get()
        print("Drug refills changed succesfully!")
        window.destroy()
    def modify_instr_info():
        instructions = changeinfo.get()
        print("Drug usage instructions changed succesfully!")
        window.destroy()

    window = Tk()
    window.geometry("500x400")
    window.title("Info Verification")
    heading = Label(text="Info Verification", bg="grey", fg="black", width="500", height="3")
    heading.pack()

    infout = Label(text="1) PERSCRIBED DRUG: " + drugperc.upper() +
                   "\n2) DRUG STRENGTH: " + drugstr.upper() + "mg" +
                   "\n3) DRUG FORM: " + drugform.upper() +
                   "\n4) DRUG REFILLS: " + drugrefill.upper() +
                   "\n5) DRUG INSTRUCTIONS: " + druginstr.upper())

    infout.place(x=150, y=75)

    inforight = Button(window, text="Information is correct", width="30", height="2", command=window.destroy, bg="grey")
    infowrong = Button(window, text="Information is not correct", width="30", height="2", command=check_info, bg="grey")
    inforight.place(x=15, y=175)
    infowrong.place(x=260, y=175)

    window.mainloop()

    class PDF(FPDF):
      def header(self):
        self.image('PP1.png', 0, 8, 40)
        self.set_font('helvetica', 'B', 20)
        self.cell(0,10, border=False, ln=1, align='C')
        self.ln(20)

    dea_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))

    rx_number = ''.join(random.choice(string.digits) for i in range(10))

    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    doctor_name = docname_info
    patient_first_name = firstname_info
    patient_last_name = lastname_info

    drug = drugperc
    strength = drugstr
    form = drugform
    refills = drugrefill
    instructions = druginstr

    pdf = PDF('L', 'mm', 'letter')
    pdf.add_page()
    pdf.set_font('times', ('BI'), 16)
    pdf.cell(40, 8, "SET.Hacks Pharmacy", ln=1)

    pdf.set_font('times', ('B'), 8)
    pdf.cell(40, 0, 'SET.Hacks Rd.', ln=2)
    pdf.cell(40, 8, "DEA#" + " " + dea_number, ln=3)
    pdf.cell(40, 0, "RX" + " " + rx_number, ln=4)
    pdf.cell(70, 0, "DR." + " " + doctor_name, ln=4, align='C')

    pdf.set_font('times', ('B'), 9)
    pdf.cell(40, 7, patient_last_name.upper() + ", " + patient_first_name.upper(), ln=5, )
    pdf.set_font('times', ('B'), 7)
    pdf.cell(70, -6.5, current_date, ln=5, align='R')

    pdf.set_font('times', ('B'), 14)
    pdf.cell(70, 20, "PERSCRIBED DRUG: " + drug.upper(), ln=14)
    pdf.set_font('times', ('B'), 11)
    pdf.cell(70, 5, "DRUG STRENGTH: " + strength.upper() + "mg", ln=15)
    pdf.cell(70, 5, "DRUG FORM: " + form.upper(), ln=16)
    pdf.cell(70, 5, "DRUG REFILLS: " + refills.upper(), ln=17)
    pdf.cell(70, 5, "DRUG INSTRUCTIONS: " + instructions.upper(), ln=18)

    pdf.output('Medicine_prescription.pdf')
    webbrowser.open_new("Medicine_prescription.pdf")

    loopcounter += 1

