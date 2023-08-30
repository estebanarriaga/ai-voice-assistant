import os
import openai
import pyaudio
import playsound 
from gtts import gTTS
import speech_recognition as sr


openai.api_key = os.getenv("OPENAI_API_KEY")

# myPyAudio = pyaudio.PyAudio()
# print(myPyAudio.get_device_count)

lang = 'en'

while True:

  def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
      audio = r.listen(source)
      said = ""
      print(audio)
    
      try:
        said = r.recognize_google(audio)
        print(said)

        if "Jack" in said:
          completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": said}])
          text = completion.choices[0].message.content
          speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
          speech.save("welcome.mp3")
          playsound.playsound("welcome.mp3")
     
      except Exception:
        print("Exception")

    return said

  get_audio()