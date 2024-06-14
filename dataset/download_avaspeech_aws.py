import os
ava_speech_file = open('ava_speech_file_names_v1.txt', 'r')
Lines = ava_speech_file.readlines()
os.chdir("./ava-speech-aws")
for line in Lines:
    line = str("https://s3.amazonaws.com/ava-dataset/trainval/" + str(line))
    cmd = "curl -O " + line
    os.system(cmd)

