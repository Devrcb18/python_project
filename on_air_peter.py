import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import pyjokes
from datetime import datetime
from googlesearch import search
asp = pyttsx3.init()
rate = asp.getProperty('rate')
voices=asp.getProperty('voices')
def speak(text):
    print(text.title())
    asp.say(text)
    asp.runAndWait()

def show_time():
    current_time = datetime.now().strftime("%H:%M:%S")
    speak(f"The current time is {current_time}")
def process(command):
    if "open google" in command.lower():
        webbrowser.open("https://google.com")
    elif "open instagram" in command.lower():
        webbrowser.open("https://instagram.com")
    elif "open youtube" ==command.lower():
        webbrowser.open("https://youtube.com")
    elif "time" in command.lower():
        show_time()
    elif "joke" in command.lower():
        speak(pyjokes.get_joke())
    elif "score" in command.lower():
        speak("opening cricinfo")
        webbrowser.open("https://espncricinfo.com")
    elif "open youtube and play" in command.lower():
        speak("what to play")
        with sr.Microphone() as  vs:
                                ca = recognizer.listen(vs, timeout=3, phrase_time_limit=5)
                                link1 = recognizer.recognize_google(ca)
                                webbrowser.open(f"https://www.youtube.com/results?search_query={link1}")
    elif "set alarm" in command.lower():
        speak("ok! enter the time")
        t_alarm=input("Enter time format(hrs:min)---\n")
        stop=False
        while stop == False:
         tn = str(datetime.now().time())
         if  t_alarm in tn:
            song=r"C:\Users\acer\Downloads\mr_bean_intro_music.mp3"
            os.system(f'start {song}')
            stop = True
    elif "exit" in command.lower():
                        speak("Goodbye!")
                        exit()           
    else:
        print(command)   

if __name__ == "__main__":
    speak("on air  Peter".center(40," "))
    speak(f"Hello! I am Peter, speaking at {rate} words per minute.")
    speak(" Listening...")
    recognizer = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            try:
                audio = recognizer.listen(source, timeout=2, phrase_time_limit=2)
                trigger = recognizer.recognize_google(audio)
                
                if trigger.lower() == "hello":
                    speak("Yes, give me a command.")
                    while True:
                        try:
                            with sr.Microphone() as command_source:
                                command_audio = recognizer.listen(command_source, timeout=3, phrase_time_limit=5)
                                command = recognizer.recognize_google(command_audio)
                                if "exit" in command.lower():
                                    speak("Goodbye!")
                                    exit()
                                process(command)
                        except sr.UnknownValueError:
                            print("..")
                        except sr.RequestError as e:
                            speak(f"Network error: {e}")
                        except Exception as e:
                            pass
                
                else:
                    print(trigger)
            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Network error: {e}")
            except Exception as e:
                 pass
