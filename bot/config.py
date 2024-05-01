#    Copyright (c) 2021 Danish_00
#    Improved By @Zylern

from decouple import config

try:
    APP_ID = config("APP_ID", cast=int)
    API_HASH = config("API_HASH")
    BOT_TOKEN = config("BOT_TOKEN")
    DEV = 1091408108
    OWNER = config("OWNER")
    ffmpegcode = ["-preset veryfast -vf "subtitles='https\:\/\/mindflayersmirror.xuploads.workers.dev\/1\:\/MFmirror\/logo.ass'" -c:v libx265 -s 854x480 -x265-params 'bframes=8:psy-rd=1:ref=3:aq-mode=3:aq-strength=0.8:deblock=1,1' -metadata 'title=Encoded By JAV STORE' -pix_fmt yuv420p -crf 23 -c:a libopus -b:a 128k -map 0 -ac 2 -vbr 2 -level 4.0 -threads 5"]
    THUMBNAIL = config("THUMBNAIL", default="https://te.legra.ph/file/cc6cb5448aee307c8f16e.jpg")
except Exception as e:
    print("Environment vars Missing! Exiting App.")
    print(str(e))
    exit(1)
