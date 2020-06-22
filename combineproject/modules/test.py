import sr
import wiki
import tts
import stackoverflow as so
import webbrowser

titles = []
links = []

tts.text_to_speech("hello Sir ,i can only search the data which is available in wikipedia and stackoverflow: ")

while(True):
    tts.text_to_speech("sir which option you want to use: ")
    option = input("1: wikipedia \n2: stackoverflow\n")       
                
    if(option == "2"):
        tts.text_to_speech("what you want to search : ")
        text = sr.speech_output()
        if text != "failed":
            print(text)
            tts.text_to_speech("ok sir ! wait for few time , i am searching, "+str(text) +" on stack overflow")
            titles = so.get_overflow_titles(text)
            links = so.get_overflow_links(text)
            
            count = 1
            for title in titles:
                print(str(count)+":"+title)
                count +=1
            tts.text_to_speech("which answer do you want to open in browser")
            print(len(links))
            link_no = int(input("enter the number of answer: "))
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            url = "https://stackoverflow.com/"+links[link_no-1]
            webbrowser.get(chrome_path).open_new_tab(url)
             
            tts.text_to_speech("enter 'q', to exit, and any key, to continue" )
            var = input("enter 'q' to exit and,any key to continue: ")
            if(var == 'q'):
                 exit(0)
            else:
                continue     
        else:
            tts.text_to_speech("sorry sir ! ,i did't get speech input")

    elif(option == "1"):
        tts.text_to_speech("what you want to search : ")
        text = sr.speech_output()
        if text != "failed":
            print(text)
            tts.text_to_speech("ok sir ! wait for few time , i am searching, "+str(text)+" on wikipedia")
            words = wiki.get_wiki_data(text)
            if words != "failed":
                print(words)
                tts.text_to_speech("sir !"+words)
                tts.text_to_speech(",...enter 'q', to exit, and any key, to continue" )
                var = input("enter 'q' to exit and any key to continue: ")
                if(var == 'q'):
                    exit(0)
                else:
                    continue
            else:
                ttss.text_to_speech("sorry sir ! ,i did't get data on wikipedia")
        else:
            tts.text_to_speech("sorry sir ! ,i did't get speech input")

    if(option !="1" or option !="2"):
        count = 0
        tts.text_to_speech("invalid option selected ,select valid option")
        exit(1)    

            
                
                                    
        
    
    


