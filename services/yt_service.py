import yt_dlp

class YTService:
    def __init__(self):
        self.ydl_opts = {
            'format': 'bestaudio/best',
            'noplaylist': True,
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True
        }

    def search(self, query: str):
        with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
            info = ydl.extract_info(f"ytsearch15:{query}", download=False)
            return [
                {
                    "id": entry.get("id"),
                    "title": entry.get("title"),
                    "thumbnail": f"https://i.ytimg.com/vi/{entry.get('id')}/hqdefault.jpg",
                    "duration": entry.get("duration")
                } for entry in info.get("entries", [])
            ]

    def get_stream(self, video_id: str):
        with yt_dlp.YoutubeDL({'format': 'bestaudio/best', 'quiet': True}) as ydl:
            info = ydl.extract_info(f"https://www.youtube.com/watch?v={video_id}", download=False)
            return {"url": info.get("url"), "title": info.get("title")}
