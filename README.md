#  YouTube Downloader

A Python-based YouTube Downloader built using `yt-dlp`.

This project allows users to download YouTube videos with both **video + audio** or download **audio only**. It also provides video and audio information before downloading.

---

##  Features

-  Download YouTube videos with audio
-  Download audio only
-  Choose video quality:
  - 360p
  - 480p
  - 720p
  - 1080p
-  Display video information before downloading
-  Display audio information before downloading
-  Automatically organize downloaded files into separate folders
-  Save extracted YouTube metadata as JSON
-  Uses FFmpeg for audio extraction and video/audio merging
-  Built completely with Python

---

##  Technologies Used

- **Python**
- **yt-dlp**
- **FFmpeg**
- **JSON**
- **OS module**

---
## 📁 Download Folder Setup

Before running the program, you need to provide your own download paths.

Open `youtube_downloader.py` and change:

```python
video_audio_folder = ""
audio_only_folder = ""
```
##  Project Structure

```text
YOUTUBE_DOWNLOAD/
│
├── youtube/
│   ├── video_audio/
│   │   └── downloaded videos
│   │
│   └── audio/
│       └── downloaded audio
│
├── main.py
└── video_info.json
```
##  Requirements
Put your folder path in the 
This project was developed and tested with the following environment:

| Software | Version |
|---|---|
|  yt-dlp | 2026.08.19 |
|  FFmpeg | 8.1.2 |

###  Python

Python **3.14.7** is recommended.

Check your Python version:

```bash
python3 --version
