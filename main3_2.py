# Import necessary libraries
# Import the gTTS module for text-to-speech conversion
from gtts import gTTS

# Import the playsound module for playing audio          
from playsound import playsound 

# Define the path to the input text file
file_path = r"3_Voice/my_text.txt"

# Open the input text file for reading with UTF-8 encoding
# 'with' can open and close files
with open(file_path, encoding='UTF8') as f:
    # Read the content of the text file
    read_file = f.read()  

# Convert the read text to speech using gTTS with English language
tts = gTTS(text=read_file, lang='en')

# Save the generated speech as an MP3 file
tts.save(r"3_Voice/my_text.mp3")

# Play the saved MP3 file using the playsound library
playsound(r"3_Voice/my_text.mp3")
