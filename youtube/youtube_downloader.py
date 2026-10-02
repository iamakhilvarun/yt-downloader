import os
import yt_dlp
import json

#  Put your folder Path here 
video_audio_folder = ""
audio_only_folder = ""
# making sure the folder exists
os.makedirs(video_audio_folder, exist_ok=True)
os.makedirs(audio_only_folder, exist_ok=True)

BANNER = r"""
██╗   ██╗████████╗   ██████╗ ██╗       ██████╗██╗     ██╗
╚██╗ ██╔╝╚══██╔══╝   ██╔══██╗██║      ██╔════╝██║     ██║
 ╚████╔╝    ██║█████╗██║  ██║██║█████╗██║     ██║     ██║
  ╚██╔╝     ██║╚════╝██║  ██║██║╚════╝██║     ██║     ██║
   ██║      ██║      ██████╔╝███████╗ ╚██████╗███████╗██║
   ╚═╝      ╚═╝      ╚═════╝ ╚══════╝  ╚═════╝╚══════╝╚═╝
"""
print(BANNER)
URL = input("Enter the YouTube URL: ")
info = yt_dlp.YoutubeDL().extract_info(URL, download=False)

output = yt_dlp.YoutubeDL().sanitize_info(info)

with open("video_info.json", "w", encoding="utf-8") as file:
    json.dump(output, file, indent=4, ensure_ascii=False)

print("Video information saved to video_info.json")

with open("video_info.json", "r", encoding="utf-8") as file:
    data = json.load(file)


def Video_with_audio(choice):
    video = None
    audio = None
    for res in data["formats"]:
        if (
            res.get("height") == choice
            and res.get("vcodec") != "none"
            and res.get("ext") == "mp4"
            and res.get("vcodec", "").startswith("avc1")
        ):
            video = res
            break
    if video is None:
        print("requested quality is not available")
        return

    print(video["format_id"])

    for res in data["formats"]:
        if res.get("acodec") != "none" and res.get("vcodec") == "none":
            audio = res
            break
    if audio is None:
        print("Requested audio is not available")
        return
    print(audio["format_id"])

    format_selector = f"{video['format_id']}+{audio['format_id']}"
    ydl_opts = {
        "format": format_selector,
        "outtmpl": os.path.join(video_audio_folder, "%(title)s.%(ext)s"),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])

def get_audio_info():

    for res in data["formats"]:

        if (
            res.get("acodec") != "none"
            and res.get("vcodec") == "none"
        ):
            return res

    return None

def audio_only():
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }
        ],
        "outtmpl": os.path.join(audio_only_folder, "%(title)s.%(ext)s"),
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([URL])


while True:

    print("--------------------------------")
    print("             MENU")
    print("--------------------------------")
    print(
        """
1. Video + Audio
2. Audio Only
3. Exit
"""
    )

    menu_choice = int(input("Enter the choice: "))

    # VIDEO + AUDIO
    if menu_choice == 1:

        print("--------------------------------")
        print("         VIDEO + AUDIO")
        print("--------------------------------\n")
        print("=================================")
        print("         VIDEO INFORAMTION")
        print("=================================\n")
        print("Title    :", data.get("title"))
        print("Uploader :", data.get("uploader"))
        duration = data.get("duration")
        if duration:
            minutes = round(duration / 60, 2)
            print("Duration :", minutes, "minutes")
        print("Views    :", data.get("view_count"))
        print("=================================\n")
        print(

            """
1. 360p
2. 480p
3. 720p
4. 1080p
5. Back
"""
        )
        quality_choice = int(input("Enter the quality: "))
        if quality_choice == 5:
            continue

        qualities = {1: 360, 2: 480, 3: 720, 4: 1080}

        if quality_choice in qualities:
            quality = qualities[quality_choice]
            Video_with_audio(quality)

        else:
            print("Invalid quality choice.")

    # AUDIO ONLY
    elif menu_choice == 2:
        print("--------------------------------")
        print("             AUDIO")
        print("--------------------------------\n") 

        audio = get_audio_info()
        if audio is None:
            print("Audio information is not available.")
            continue

        print("=================================")
        print("         AUDIO INFORAMTION")
        print("=================================\n")
        print("Format      :", audio.get("ext"))
        print("Codec       :", audio.get("acodec"))
        print("Bitrate     :", audio.get("abr"))
        print("Sample Rate :", audio.get("asr"))
        print("=================================\n")
        audio_only()

    elif menu_choice == 3:
        print("Exiting the program...")
        break

    else:
        print("Invalid choice. Please try again.")
