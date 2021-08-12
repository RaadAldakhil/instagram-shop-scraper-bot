from instagramy import InstagramUser
import requests

# Connect to profile
user = InstagramUser("raad.aldakhil",from_cache=True)

print(user.biography)
posts = user.posts
for index, post in enumerate(posts):
    r = requests.get(post[8],allow_redirects=True)
    open('post#'+str(index),'wb').write(r.content)
