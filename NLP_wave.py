import wave
import numpy as np
# Create audio file wave object
good_morning = wave.open('good_morning.wav', 'r')

# Read all frames from wave object
signal_gm = good_morning.readframes(-1)

# View first 10
print(signal_gm[:10])
# Finding the time stamps
# We know the frequency of our sound wave is 48 kHz, but what if we didn't? We could find it by dividing the length of our sound wave array by the duration of our sound wave. However, Python's wave module has a better way. Calling getframerate() on a wave object returns the frame rate of that wave object.# We can then use NumPy's linspace() method to find the time stamp of each integer in our sound wave array. This will help us visualize our sound wave in the future.
# The linspace() method takes start, stop and num parameters and returns num evenly spaced values between start and stop.
# In our case, start will be zero, stop will be the length of our sound wave array over the frame rate (or the duration of our audio file) and num will be the length of our sound wave array.
# Read in sound wave and convert from bytes to integers
good_morning = wave.open('good_morning.wav', 'r')
signal_gm = good_morning.readframes(-1)
soundwave_gm = np.frombuffer(signal_gm, dtype='int16')

# Get the sound wave frame rate
framerate_gm = good_morning.getframerate()

# Find the sound wave timestamps
time_gm = np.linspace(start=0,
                      stop=len(soundwave_gm)/framerate_gm,
					  num=len(soundwave_gm))

# Print the first 10 timestamps
print(time_gm[:10])



#Visualizations between 2 tracks
import matplotlib.pyplot as plt
# Setup the title and axis titles
plt.title('Good Afternoon vs. Good Morning')
plt.ylabel('Amplitude')
plt.xlabel('Time (seconds)')

# Add the Good Afternoon data to the plot
plt.plot(time_ga, soundwave_ga, label='Good Afternoon')

# Add the Good Morning data to the plot
plt.plot(time_gm, soundwave_gm, label='Good Morning',
   # Set the alpha variable to 0.5
   alpha=0.5)

plt.legend()
plt.show()


# Importing the speech_recognition library
import speech_recognition as sr

# Create an instance of the Recognizer class
recognizer = sr.Recognizer()

# Set the energy threshold
recognizer.energy_threshold = 300

# Create a recognizer class


# Transcribe the support call audio
text = recognizer.recognize_google(
  audio_data=clean_support_call_audio, #track
  language="en-US")

print(text)

# Instantiate Recognizer
recognizer = sr.Recognizer()

# Convert audio to AudioFile
clean_support_call = sr.AudioFile('clean_support_call.wav') #track

# Convert AudioFile to AudioData
with clean_support_call as source:
    clean_support_call_audio = recognizer.record(source)

# Transcribe AudioData to text
text = recognizer.recognize_google(clean_support_call_audio,
                                   language="en-US")
print(text)