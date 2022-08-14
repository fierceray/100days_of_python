import requests
from bs4 import BeautifulSoup
from spotify_handler import SpotifyHandler

if __name__ == '__main__':
    back_date = input("What date you want back to? Format 'yyyy-mm-dd' ")
    url = f"https://www.billboard.com/charts/hot-100/{back_date}/"

    response = requests.get(url)
    # title-of-a-story
    soup = BeautifulSoup(response.text, "html.parser")
    # // *[ @ id = "title-of-a-story"]
    h3 = soup.select("li ul li h3")  # title-of-a-story")
    for each in h3:
        name = each.getText().strip()
        sp = SpotifyHandler()


        try:
            track = sp.search(query=f'track:{name}')
            sp.add_item_to_playlist(track)
        except IndexError:
            print(f"Cannot find this song: {name}, skip")
