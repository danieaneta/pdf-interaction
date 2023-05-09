import PyPDF2 as pdf
import pyttsx3 as speech

# python PyPDF2 to manipulate and read the PDF 
# Python pyttsx3 for text to speech 

engine = pyttsx3.init()
engine.say("say this text")
engine.runAndWait()
#Open the PFD, store it into a prompt variable  
openPDF = PyPDF2.PdfReader('pdffile.pdf')

engine.say(openPDF)


#Text to speech as per what is given in prompt 
