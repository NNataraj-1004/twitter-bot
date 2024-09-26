import tweepy

# Replace these with your own credentials
API_KEY = 'K9RuLLA9jzpED9DbHWwhx1xnc'
API_SECRET_KEY = '18awZ9QpjhahLu9yu3Ig1Ma0crkJvo9BmoUproEqe7CGXMJlrc'
ACCESS_TOKEN = '1736252270202007552-0GhhFhSAHCD5EDlMSTz3aLpH7HKuK8'
ACCESS_TOKEN_SECRET = 'QS80sdTy2lvImdBF9ke9v2DLeIdUC2fj2ThxMAZ6rXlO7'

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Test the connection
try:
    api.verify_credentials()
    print("Authentication OK")
except Exception as e:
    print("Error during authentication:", e)

# List your followers
followers = api.followers_ids()

# Example logic to unfollow users
for follower in followers:
    user = api.get_user(follower)
    # Add your logic to determine if the user is a spam account
    if user.followers_count < 10:  # Example condition
        print(f"Unfollowing {user.screen_name}")
        api.destroy_friendship(user.id)  # Unfollow the user
