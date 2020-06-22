import pyttsx3

def text_to_speech(text):
    try:
        ########### initilazing the TTS ######################
        engine = pyttsx3.init('sapi5')
        rate = engine.getProperty('rate')   # getting details of current speaking rate                     
        engine.setProperty('rate', 145)     # setting up new voice rate
        volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)     
        engine.setProperty('volume',1)    # setting up volume level  between 0 and 1
        voices = engine.getProperty('voices')       #getting details of current voice
        #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
        engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female
        # for language.
        #engine.setProperty("language",'hi')
        engine.say(text)
        engine.runAndWait()
    except:
        engine.stop()
