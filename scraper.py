from instagramy import InstagramUser

# Connect to profile
user = InstagramUser("raad.aldakhil",from_cache=True)

print(user.biography)
print(user.posts)
