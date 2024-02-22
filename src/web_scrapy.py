import requests
from bs4 import BeautifulSoup


def get_champion_urls():    
    champion = []
    with open('../data/raw/champion.txt','r') as f:
        for line in f:
            cleaned_line = ''.join(e for e in line.strip() if e.isalnum())
            champion.append(cleaned_line.lower())
    champion_urls = []
    for c in champion:
        c = c.replace(" ", "").replace("'", "").replace("’","")
        if c == 'renataglasc':
            c = 'renata'
        
        champion_urls.append('https://universe.leagueoflegends.com/en_US/story/champion/'+c)
    return champion_urls

def get_thumbnail_links(champion_urls):
    for url in champion_urls:
        # Send HTTP request
        
        response = requests.get(url)
        webpage = response.text
        champion_name = url.split('/')[-1]
        print(champion_name)
        # Parse the webpage
        soup = BeautifulSoup(webpage, 'html.parser')
        # Find the thumbnail links
        # Note: 'thumbnail_class' should be replaced with the actual HTML class name of the thumbnail links
        thumbnails = soup.find_all('div', class_="styles_grid__4dc4K")
        thumbnails = thumbnails[0].find_all('a')
        # Get the thumbnail page links
        thumbnail_urls = []
        thumbnail_urls = ['https://www.skinexplorer.lol'+thumb['href'] for thumb in thumbnails]
         
            
