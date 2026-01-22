import datetime
import pyttsx3
import webbrowser
import time
import speech_recognition as sr

# ============== CONFIG ==============
assistantName = "kelly"
userName = "Lahari"

def init_engine():
    """Initialize and return a fresh pyttsx3 engine."""
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)  # default voice
    engine.setProperty('rate', 170)
    return engine

def speak(text):
    """Speak the text using a fresh engine each time to ensure voice works."""
    engine = init_engine()  # fresh engine for each command
    print("SPEAKING:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.2)  # small delay ensures speech finishes

def speakDateTime():
    """Speak the current date and time."""
    now = datetime.datetime.now()
    message = (
        f"{userName}, the current time is {now.strftime('%I:%M %p')} "
        f"and today is {now.strftime('%A, %B %d, %Y')}"
    )
    speak(message)

def hearMe():
    """Get typed command from the user."""
    return input(f"{userName}, enter your command: ").lower().strip()

# ============== MAIN PROGRAM ==============
if __name__ == "__main__":

    # Startup greeting
    speak(f"Hello {userName}, How Can I Help You ? .")
    speak("You can ask me to open Google, Instagram, Python tutorials, or tell you the date and time.")

    while True:
        query = hearMe()

        # Date and time
        if "time" in query or "date" in query or "datetime" in query:
            speakDateTime()

        # Python programming tutorials
        elif "python programming tutorial" in query or "python tutorial" in query:
            speak("Opening Python programming tutorials on YouTube")
            webbrowser.open("https://www.youtube.com/results?search_query=python+programming+tutorial")

        # Open Google
        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        # Open Instagram
        elif "open instagram" in query:
            speak("Opening Instagram")
            webbrowser.open("https://www.instagram.com")

        # Exit the assistant
        elif "exit" in query or "quit" in query:
            speak(f"Goodbye {userName}. Have a nice day.")
            time.sleep(0.5)  # ensures goodbye finishes
            break

        # Anything else → search Google
        else:
            speak(f"Searching Google for {query}")
            webbrowser.open("https://www.google.com/search?q=" + query)
