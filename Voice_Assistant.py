import pyttsx3
import speech_recognition as sr
import webbrowser as wb
engine = pyttsx3.init()
rate = engine.getProperty('rate')   
#print (rate)                        
engine.setProperty('rate', 200)    
#volume = engine.getProperty('volume')  
#print (volume)                         
#engine.setProperty('volume',1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

pyttsx3.speak("Hello Kajal")
print()
print("Welcome")                    
engine.runAndWait()
pyttsx3.speak("I am your voice assistant")
pyttsx3.speak("How can I help you...?")


while True:
	print()
	print("\t \t Tell me how can i help you... i am listening: ", end='')

	r  =  sr.Recognizer()

	with sr.Microphone() as source:
		pyttsx3.speak('Tell me...')
		audio = r.listen(source)
		pyttsx3.speak('got it... please wait..!!')

	ch = r.recognize_google(audio)

	if("hello" in ch) or ("hi" in ch) and ("hey" in ch):
		pyttsx3.speak("Hii Kajal , how are you ...?")
		
	elif("fine" in ch) or ("what" in ch) and ("about" in ch):
		pyttsx3.speak("i am good")
		
	elif("tell" in ch) or ("about" in ch) and ("yourself" in ch):
		pyttsx3.speak("i am your voice assistant, i can control your linux system")
		
	elif("date" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=date")
		pyttsx3.speak("showing date")
	elif("calendar" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=cal")
		pyttsx3.speak("showing calendar")
	elif("IP" in ch )or ("ip address" in ch) or "address" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=ifconfig")
		pyttsx3.speak("showing IP address")

	elif("amount" in ch) or ("disc" in ch) and ("space" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=df%20-h")
		pyttsx3.speak("showing available disc space")

	elif("pip" in ch) or ("module" in ch) and ("list" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=pip%20module%20list")
		pyttsx3.speak("Here is the list of avaulable modules")
		
	elif("user" in ch) or ("Kajal" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=useradd%20Kajal")
		pyttsx3.speak("Kajal user has been created")  
	elif("restrict" in ch) or ("K" in ch):
		wb.open("http://192.168.43.15/cgi-bin/kajal.py?x=useradd%20-s%20/usr/bin/cal%20K")
		pyttsx3.speak("K user has been created and restricted") 
	elif ("exit" in ch) or ("quit" in ch) or ("bye" in ch) or ("Stop" in ch):
		pyttsx3.speak("Ok, see you soon, have a nice day..!!!")
		break
	else:
		print("not understand, Say it again!!!")