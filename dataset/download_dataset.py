# importing packages
from numpy import unique
from pytube import YouTube
import os
import pandas as pd

def download_youtube_video(video_url):
    print("Downloading video..." + str(video_url))
    yt = YouTube(video_url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path="./ava-speech")
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)


if __name__ == '__main__':

    data = pd.read_csv("./ava_speech_labels_v1.csv", names=["video_id","start","end","label"])
    for i in unique(data["video_id"]):
        try:
            download_youtube_video(str("https://www.youtube.com/"+ i))
        except Exception as e:
            print(e)
