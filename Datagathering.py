from __future__ import unicode_literals
import os
import shutil
import pytube
import subprocess
import torch

def download_channel_audio(channel_url):
    channel = pytube.Playlist(channel_url)
    for video in channel.videos:
        print(f"Downloading {video.title}")
        video.streams.filter(only_audio=True).first().download(output_path='./audioFiles/raw_files')
        print(f"Downloaded {video.title}")
    print("Finished downloading audio files")

def processAudioFiles(path: str):
    process = subprocess.Popen(f"whisperer_ml transcribe {path} data", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    result = []
    errcode = process.returncode
    for line in process.stdout:
        result.append(line.decode("utf-8").strip())
    for line in result:
        print(line)
    if errcode is not None:
        raise Exception("Error Converting audio file")
    # process = subprocess.Popen(f"whisperer_ml transcribe {path} dataset", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # errcode = process.returncode
    # if errcode is not None:
    #     raise Exception("Error labelling audio file")
    
def main():
    download_channel_audio('https://www.youtube.com/playlist?list=PL5NqZ9VtoOg5gBSAI4XlPFDKwAS7u8YXP')
    processAudioFiles('./audioFiles')

if __name__ == "__main__":
    main()