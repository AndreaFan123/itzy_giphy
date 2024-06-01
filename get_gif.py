from dotenv import load_dotenv
import requests
import os

load_dotenv()

GIPHY_API_KEY = os.getenv('GIPHY_API_KEY') 
SEARCH_QUERY = 'itzy'
LIMIT=50

GIPHY_API_URL = f'https://api.giphy.com/v1/gifs/search?api_key={GIPHY_API_KEY}&q={SEARCH_QUERY}&limit={LIMIT}&offset=0&rating=g&lang=en&bundle=messaging_non_clips'


def get_gif():
    try:
        res = requests.get(GIPHY_API_URL)
        if res.status_code == 400:
            print('Error: Bad Request')
        elif res.status_code == 401:
            print('Error: Unauthorized')
        elif res.status_code == 403:
            print('Error: Forbidden')
        elif res.status_code == 404:
            print('Error: Not Found')
        elif res.status_code == 429:
            print('Error: Too Many Requests')
        elif res.status_code == 500:
            print('Error: Internal Server Error')
        elif res.status_code == 503:
            print('Error: Service Unavailable')
        elif res.status_code == 200:
            data = res.json()
            image_url = [image['images']['original']['url'] for image in data['data']]
            return image_url

    except Exception as e:
        print(f'Error: {e}')