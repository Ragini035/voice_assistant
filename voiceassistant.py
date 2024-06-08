import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime


recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
        except sr.UnknownValueError:
            speak("Sorry, I did not understand that.")
            return ""
        except sr.RequestError:
            speak("Sorry, the service is down.")
            return ""
        return command.lower()

def execute_command(command):
    if 'google' in command:
        speak("What should I search for on Google?")
        query = listen()
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        speak(f"Here are the results for {query} on Google")
        
    elif 'youtube' in command:
        speak("What should I search for on YouTube?")
        query = listen()
        url = f"https://www.youtube.com/results?search_query={query}"
        webbrowser.open(url)
        speak(f"Here are the results for {query} on YouTube")
        
    elif 'date' in command:
        today = datetime.date.today().strftime("%B %d, %Y")
        speak(f"Today's date is {today}")
        
    elif 'time' in command:
        now = datetime.datetime.now().strftime("%H:%M")
        speak(f"The current time is {now}")
        
    else:
        speak("Sorry, I didn't understand the command.")

# Main loop to continuously listen for commands
def main():
    speak("How can I assist you today?")
    while True:
        command = listen()
        if command:
            execute_command(command)
        if 'exit' in command or 'stop' in command:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()
