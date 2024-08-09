import requests
import time

# Facebook Access Tokens
tokens = [
    'EAABwzLixnjYBOyJuGlKIwVC0e8mB9IrYfsLfqtXQugr3HSBnAAUMuk4DA8frwHCrlIX7PXKrBU3rBGD2tfLAktVTzkqJhf0rCnnmP53v2IzkjhF9AJi13TfLEQzkr3mkynkoUeuint5IFdODeqLXjkUnXZANZChey274lLsNZBy4cn9YF4NZAMVl8gy5torvFeEyNBLpCnNS',
    'EAABwzLixnjYBO9eiZBRwxuHa6PLHnHf9xskMmbLq6RKbZCvnE3F6BEBcFZBRhnKdAldzCaskOtjkw4vA7geeJqZBNZAIknukn2Ty37QZC84VekxK42yr7GNQpcZBgmgZAPJpAf4vPHSGbt3B8ii3Txbwu4ZBUYT9ioGSfn7HsMXZCT7sjIHUVkdJLmDZAK9CoOwF5iIeydaREvHpqZAo'
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
