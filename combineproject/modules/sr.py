import speech_recognition as sr

def speech_output():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say !")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            if text != " ":
                 return text
            else:
                return "failed"
        except:
            print("sorry, error in Recognizer ")
    
