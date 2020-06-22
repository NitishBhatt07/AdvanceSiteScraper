import speech_recognition as sr
import wikipedia as wiki
import pyttsx3

try:
    ########### initilazing the TTS ######################
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   # getting details of current speaking rate                     
    engine.setProperty('rate', 145)     # setting up new voice rate
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)     
    engine.setProperty('volume',1)    # setting up volume level  between 0 and 1
    voices = engine.getProperty('voices')       #getting details of current voice
    #engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
    engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

    engine.say("hello Sir ,i can only search the data which is available in wikipedia : ")
    engine.say("what you want to search : ")
    engine.runAndWait()

#################################################################

######### Recognizing the speech ####################################
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("say !")
        audio = r.listen(source)
    if(audio != None):
        search_item = r.recognize_google(audio)
        engine.say("ok sir ! wait for few time , i am searching "+search_item+" on wikipedia: ")
        engine.runAndWait()
        print(r.recognize_google(audio))
    else:
         engine.say("sorry sir ,i did't get that : ")
##################################################################
        
########## getiing sentance from wikipedia################################
    result = wiki.page(wiki.search(search_item)[0])
    result_list = result.summary
    count = 0
    words = " "
    for i in range(len(result_list)):
        if count>=3:
            break      
        else:
             words = words+result_list[i]
        if result_list[i] == '.':
            count +=1
###################################################################
    print(words)
    engine.say("Sir !"+words)
    engine.runAndWait()

    engine.say("sir ,enter q to exit : ")
    engine.runAndWait()
    end = input("enter 'q' to quit: ")
    if(end == 'q'):
        engine.stop()
        exit(0)
   
    
except:
    engine.say("sorry sir i not able to find word on wikipedia,..ask only wikipedia word..")
    engine.runAndWait()
    print("no result found")
    engine.stop()
