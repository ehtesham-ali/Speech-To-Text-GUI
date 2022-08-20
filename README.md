### Introduction

Speech To Text is another small project that enables users to upload an audio file and derive text with it. This is quite useful if you need the captions of a video or all the text in a lecture being recorded. Features include:

- The ability to upload a .wav audio file to extract text from it
- The option to record yourself and extract text from your recording
- You can choose to download the file as a .txt file currently
- All packaged into a neat and straightforward GUI interface

---

### How to Use YT Video Downloader

Using this app is super simple:

1. If you are uploading an audio file (only .wav files are supported), simply press the "open file dialogue" button and pick the file you want to extract text from. 

    If you want to record your own voice, you can set a timer towards the right side and hit the "start" button. This will record you using the system default mic for said amount of time.

2. Next, you will see the text extracted in the box to the lower-left side. If you are happy with the result, you should enter a file name ending in .txt in the rectangular box on the lower-right side and press the "download" button. This will download the .txt file in the parent directory of the python file.

---

### Dependencies

This project only has 2 dependencies; the rest are native to Python:

- PyQt5 and its dependencies (`pip install PyQt5`)
- SpeechRecognition and its dependencies (`pip install SpeechRecognition pydub`)
- PyAudio (`pip install pyaudio`)

Please note that the authors of PyAudio have forgotten to update the .whl file that PyPi provides so you should follow [this short tutorial](https://www.youtube.com/watch?v=AKymlea8sYM) if you want to use the microphone:

---

### Future Updates

At this moment no future updates are being considered.

---

**[Notion](https://ehtesham-ali.notion.site/Speech-To-Text-GUI-168f55a30db247438ea162abd1d7f61b) | [Website](https://ali-ehtesham.carrd.co/)**
