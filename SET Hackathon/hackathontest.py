import speech_recognition as sr
import pyaudio
from fpdf import FPDF
from datetime import datetime
import random, string, os

r = sr.Recognizer()

'''def inp_audio():
    while(True):
        with sr.Microphone() as source:
            audio = r.record(source, duration = 6)

            try:
                stdin = r.recognize_google(audio)
            except:
                print("Input not recognized, please try again")
            else:
                break
        return stdin'''

def inp_audio():
    stdin = input("")
    return stdin

print("Patient first name:")
patientname = inp_audio()

print ("Patient last name:")
patientlast = inp_audio()

print("Doctor name:")
docname = inp_audio()

def check_drug():
    while(True):
        print("Drug perscribed:")

        file = open("drugdatabase.txt")
        search_word = inp_audio()

        if(search_word in file.read()):
            print("Drug found.")
            return search_word
            break
        else:
            print("Invalid drug, please try again")

drugperc = check_drug()

print("Perscription strength (mg):")
drugstr = inp_audio()

print("Perscription form (tablet, liquid, etc...):")
drugform = inp_audio()

print("Perscription refills (#):")
drugrefill = inp_audio()

print("Perscription instructions:")
druginstr = inp_audio()

class PDF(FPDF):
  def header(self):
    self.image('PP2.png', 0, 8, 40)
    self.set_font('helvetica', 'B', 20)
    self.cell(0,10, border=False, ln=1, align='C')
    self.ln(20)


# printing Random DEA#
dea_number = ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(10))

# creating random only digit code
rx_number = ''.join(random.choice(string.digits) for i in range(10))

#Creating current time feature
current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

doctor_name = docname
patient_first_name = patientname
patient_last_name = patientlast
drug = drugperc
instructions = druginstr

pdf = PDF('L', 'mm', 'letter')
pdf.add_page()
pdf.set_font('times',('BI'), 16)
pdf.cell(40, 8, "SET.Hacks Pharmacy",ln=1)

#Preset Address I suppose?, Put a random one idk discuss later *
pdf.set_font('times',('B'), 8)
pdf.cell(40, 0, '999 Juice (W)R(l)d',ln=2)
pdf.cell(40, 8, "DEA#"+" " + dea_number, ln=3)
pdf.cell(40, 0, "RX"+" " + rx_number, ln=4)
pdf.cell(70, 0, "DR"+" " + doctor_name, ln=4, align ='C')

pdf.set_font('times',('B'), 9)
pdf.cell(40, 7, patient_last_name.upper()+ ", " + patient_first_name.upper(),ln=5,)
pdf.set_font('times',('B'), 7)
pdf.cell(70, -6.5, current_date ,ln=5, align='R')

pdf.set_font('times',('B'), 11)
pdf.cell(70,20, "PERSCRIBED DRUG: " + drug.upper(), ln=14)
pdf.cell(70,-8, "DRUG STRENGTH: " + drugstr.upper(), ln=15
pdf.cell(70,20, "DRUG FORM: " + drugform.upper(), ln=14)
pdf.cell(70,-8, "DRUG REFILLS: " + drugrefill.upper(), ln=15)
pdf.cell(70,-8, "DRUG INSTRUCTIONS: " + instructions.upper(), ln=15)

pdf.output('Medicine_prescription.pdf')
os.startfile("Medicine_prescription.pdf")

