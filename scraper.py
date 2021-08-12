from instagramy import InstagramUser

# Connect to profile
user = InstagramUser("raad.aldakhil")

print(user.biography())

posts = user.posts()

print('\n\nLikes', 'Comments')
for post in posts:
    likes = post["likes"]
    comments = post["comment"]
    print(likes,comment)
