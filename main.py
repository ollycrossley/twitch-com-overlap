import requests

url = "https://api.twitch.tv/helix/users/follows"

params = {
    "to_id": "123456"  # Replace with the channel ID
}

headers = {
    "Client-ID": "your_client_id",
    "Authorization": "Bearer your_access_token"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    data = response.json()
    followers = data["data"]
    for follower in followers:
        print(follower["from_name"])
else:
    print("Error:", response.status_code)
