import requests
from bs4 import BeautifulSoup

def get_video_tags(video_url):
    response = requests.get(video_url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # YouTube tags are stored in meta tags
    tags = []
    for meta_tag in soup.find_all("meta"):
        if meta_tag.get("name", None) == "keywords":
            tags = meta_tag.get("content", "").split(",")

    print(tags)

    return tags

def main():
    # Example YouTube video URLs
    video_urls = [
        "https://www.youtube.com/watch?v=hOHKltAiKXQ&list=RDhOHKltAiKXQ&start_radio=1"

    ]

    for url in video_urls:
        tags = get_video_tags(url)
        print(f"URL: {url}\nTags: {tags}\n")

if __name__ == "__main__":
    main()

