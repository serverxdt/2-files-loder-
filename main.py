import requests
import time

# Facebook Access Tokens
tokens = [
    'EAAD6V7os0gcBOz9iLK8rxkKXTfBvtgByYS82RwFwLFtIpVUacWI3thVuxIVGB40uhy4dZBemZAGOeGl1zrCRBgJlD9KoZAJLdQDY3LPnMYUd6ofjidteKjo880xmnb1PZCTIXvBHrzxb9M3Ct6UMT8L4K5EoTaF3fcVv4uRPAkuWRjdlcZAUveN9S82hZBxNZB7nAZDZD'
]

# Post ID
post_id = '61559728229012'

# Comment text
comment = 'Rocky Roy Roy'

# API URL to post comment
url = f"https://graph.facebook.com/v12.0/{post_id}/comments"

# Loop over each token and post the comment with a 10-second delay
for token in tokens:
    # Parameters for the API call
    params = {
        'access_token': token,
        'message': comment
    }

    # Sending POST request to Facebook API
    response = requests.post(url, params=params)

    # Handling the response
    if response.status_code == 200:
        print(f"Comment posted successfully with token: {token[:15]}...!")
    else:
        print(f"Failed to post comment with token: {token[:15]}..., Status Code: {response.status_code}, Error: {response.text}")
    
    # Wait for 10 seconds before posting the next comment
    time.sleep(10)
