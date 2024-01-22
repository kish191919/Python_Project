# pip install gtts               => Convert text to speech
# pip install playsound==1.2.2   => Play an mp3 file with Python
# pip install -U PyObjC          => If the following error occurs, ModuleNotFoundError: No module named 'AppKit'

# Import the gTTS module for text-to-speech conversion
from gtts import gTTS

# Import the playsound module for playing audio          
from playsound import playsound 

# Assign the text "Hi, My name is Danny" to the variable 'text'.
text = "Hi, My name is Danny"

# Create a Text-to-Speech (TTS) object using the 'gTTS' library, passing the 'text' and specifying the language as English ('en').
tts = gTTS(text=text, lang='en')

# Save the generated speech as an MP3 file named 'hi.mp3' in the '3_Voice' directory.
tts.save(r"3_Voice/hi.mp3")

# Play the saved MP3 file using the 'playsound' library.
playsound(r"3_Voice/hi.mp3")
