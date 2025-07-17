import requests

class TiktTokApiClient():
    def __init__(self, tiktok_key , tiktok_secret_key):
        self.tiktok_key = tiktok_key
        self.tiktok_secret_key = tiktok_secret_key
        self.urltoken = 'https://open.tiktokapis.com/v2/oauth/token/'
        self.url = 'https://open.tiktokapis.com/v2/research/adlib/ad/query/?fields=ad.id,ad.first_shown_date,ad.last_shown_date,ad.videos,ad.reach'

    
    def get_video_tiktok(self, product:str):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cache-Control': 'no-cache',
        }

        data = {
            'client_key': f'{self.tiktok_key}',
            'client_secret': f'{self.tiktok_secret_key}',
            'grant_type': 'client_credentials',
        }
        response = requests.post(self.urltoken, headers=headers, data=data)

        if response.status_code == 200:
            access_token = response.json().get('access_token')

        
        headers = {
            'Authorization': 'Bearer '+ access_token,
            'Content-Type': 'application/json',
        }

        payload = {
            "filters": {
                "ad_published_date_range": {
                    "min": "20230101",
                    "max": "20231231"
                },
                "country_code": "ES",
                "unique_users_seen_size_range": {
                    "min": "1K",
                    "max": "1M"
                },
            },
            "search_term": product
        }

        # Realiza la solicitud POST
        response = requests.post(self.url, headers=headers, json=payload)

        return response