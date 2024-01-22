import speech_recognition as sr
import pyttsx3

engine=pyttsx3.init()

recognizer = sr.Recognizer()

def perform_calculation(command):
    try:
        command=command.replace("x","*")
        command=command.replace("X","*")
        result = eval(command)
        print (f"Result: {result}")
        return (f"Result: {result}")
    except Exception as e:
        return ("This is not a valid arithmatic operation. Please try again.")

while True:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)  
    try:
        command = recognizer.recognize_google(audio)
        print("You said: " + command)
        if "calculate" in command:
            command.lower()
            calculation = command.split("calculate")[1].strip()
            response = perform_calculation(calculation)
            engine.say(response)
            engine.runAndWait()
        elif "exit" in command:
            engine.say("Exiting the program.")
            engine.runAndWait()
            break
    except sr.UnknownValueError:
        engine.say("Sorry, I could not understand your speech.")
        engine.runAndWait()
    except sr.RequestError as e:
        engine.say("Error connecting to the Google Web Speech API: {0}".format(e))
        engine.runAndWait()