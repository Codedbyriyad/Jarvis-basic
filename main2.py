import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    found_british = False
    for voice in voices:
        if "United Kingdom" in voice.name or "UK" in voice.name:
            engine.setProperty('voice', voice.id)
            found_british = True
            break
    if not found_british:
        engine.setProperty('voice', voices[0].id)

    engine.setProperty('rate', 175)    
    engine.setProperty('volume', 1.0) 

    print(f"Jarvis: {text}")
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def process_command(command):
    command = command.lower()
    if "hello" in command:
        speak("Hello Sir. All systems are functioning within normal parameters. How can I assist you?")
    elif "what time is it" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The current time is {current_time}, Sir.")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "stop" in command or "exit" in command:
        speak("Powering down systems. Goodbye, Sir.")
        return False
    return True

if __name__ == "__main__":
    speak("Initializing all systems... Systems online.")
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Calibrating for background noise...")
        r.adjust_for_ambient_noise(source, duration=1)
        
    running = True
    while running:
        with sr.Microphone() as source:
            try:
                print("\nWaiting for wake word 'Jarvis'...")
                # language='en-IN' ব্যবহার করা হয়েছে যাতে আমাদের অ্যাকসেন্ট বুঝে
                audio = r.listen(source, timeout=3, phrase_time_limit=3)
                word = r.recognize_google(audio, language='en-IN')

                if "jarvis" in word.lower():
                    speak("Yes, Sir?")
                    print("Listening for command...")
                    
                    audio = r.listen(source)
                    # এখানেও language='en-IN' ব্যবহার করুন
                    command = r.recognize_google(audio, language='en-IN')
                    print(f"User Command: {command}")
                    
                    running = process_command(command)

            except sr.UnknownValueError:
                print("Jarvis: Sorry, I didn't catch that.")
                continue
            except Exception as e:
                print(f"System Error: {e}")