import requests

# Facebook Access Token
token = 'EAABwzLixnjYBOyJuGlKIwVC0e8mB9IrYfsLfqtXQugr3HSBnAAUMuk4DA8frwHCrlIX7PXKrBU3rBGD2tfLAktVTzkqJhf0rCnnmP53v2IzkjhF9AJi13TfLEQzkr3mkynkoUeuint5IFdODeqLXjkUnXZANZChey274lLsNZBy4cn9YF4NZAMVl8gy5torvFeEyNBLpCnNS'

# Post ID
post_id = '61559728229012'

# Comment text
comment = 'Rocky Roy Roy here lihk do 😒'

# API URL to post comment
url = f"https://graph.facebook.com/v12.0/{post_id}/comments"

# Parameters for the API call
params = {
    'access_token': token,
    'message': comment
}

# Sending POST request to Facebook API
response = requests.post(url, params=params)

# Handling the response
if response.status_code == 200:
    print("Comment posted successfully!")
else:
    print(f"Failed to post comment: {response.status_code}, {response.text}")
