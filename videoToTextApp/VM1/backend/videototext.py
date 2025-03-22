import speech_recognition as sr
import moviepy.editor as mp

def process_video(path):
    clip = mp.VideoFileClip(path)
    clip.audio.write_audiofile("converted.wav")
    recognizer = sr.Recognizer()
    with sr.AudioFile("converted.wav") as source:
        audio = recognizer.record(source)
    return recognizer.recognize_google(audio)