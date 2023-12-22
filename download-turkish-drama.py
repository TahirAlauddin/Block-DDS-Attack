from pytube import YouTube
import schedule
import time
import youtube_dl

downloaded = []
playlist = 'https://youtube.com/playlist?list=PLNm0LhCuArzRqdynqkw3mJti0RKVMbmEr'

def get_playlist_urls(playlist_url):
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(playlist_url, download=False)
    urls = []
    if 'entries' in result:
        for entry in result['entries']:
            urls.append(entry['webpage_url'])
    return urls


def progress_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Downloading")


def complete_func(*args, **kwargs):
    print(args)
    print(kwargs)
    print("Downloaded successfully")


def my_daily_function():
    urls = get_playlist_urls(playlist)
    print(urls)
    for url in urls:
        if url not in downloaded:
            ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
            with ydl:
                result = ydl.extract_info(url)
        downloaded.append(url)
    # Perform any other desired actions here

# schedule.every().day.at("21:00").do(my_daily_function)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


my_daily_function()
