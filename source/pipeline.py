import pandas as pd
import numpy as np
import os
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
import matplotlib.pyplot as plt

# change working directory to capstone home

class pipeline():
    """
    Object for importing and cleaning electrolarynx video feeds prior to prediction
    """
    def __init__(self, data_directory = 'data/'):
        self.data_directory = data_directory
        self.metadata = pd.read_csv(f"{data_directory}metadata.csv")
        

    def get_audio(self, video_path):
        """
        Method for importing a new video given a pat

        :return:
            - sound_array(arr): array of sound
            - uadioclip(obj): AudioFileClip() object
        """
        audio_filename = video_path.split('/')[-1].replace('.mp4','.wav')
        audioclip = AudioFileClip(self.data_directory+video_path)
        sound_array = audioclip.to_soundarray()

        return sound_array, audioclip

    def print_audio(self, video_path, sample_rate = 41000):
        """
        Method for displaying the waveform of a given audio file
        """
        audio, _obj = self.get_audio(video_path)
        #defining a function to normalize the audio
        def normalize_audio(audio):
            audio = audio / np.max(np.abs(audio))
            return audio
        
        #applying the function to the audio
        audio = normalize_audio(audio)
        plt.figure(figsize=(15,4))
        plt.plot(np.linspace(0, len(audio) / sample_rate, num=len(audio)), audio)
        plt.grid(True)

    def feature_engineering(self):
        """
        Method for cleaning audio files into data we can run model.predict() on.

        :return:
            - matrix of features
        """
        #TODO: implement pipeline.feature_engineering()
        return None

