from instagramy import InstagramUser

# Connect to profile
user = InstagramUser("raad.aldakhil",from_cache=True)

print(user.biography)
posts = user.posts
for post in posts:
    print(post[8])
