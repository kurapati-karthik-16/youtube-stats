import requests
from config import YOUTUBE_API_KEY, BASE_URL

def get_channel_statistics(channel_id):
    url = f"{BASE_URL}/channels?part=snippet,statistics&id={channel_id}&key={YOUTUBE_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "items" in data and len(data["items"]) > 0:
            snippet = data["items"][0]["snippet"]
            statistics = data["items"][0]["statistics"]
            return {
                "title": snippet.get("title"),
                "thumbnail": snippet.get("thumbnails", {}).get("default", {}).get("url"),
                "subscribers": int(statistics.get("subscriberCount", 0)),
                "views": int(statistics.get("viewCount", 0)),
                "videos": int(statistics.get("videoCount", 0)),
            }
    return None
