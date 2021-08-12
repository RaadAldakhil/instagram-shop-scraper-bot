from instagramy import InstagramUser

# Connect to profile
user = InstagramUser("raad.aldakhil")

print(user.popularity())
print(user.get_biography())

posts = user.get_posts_details()

print('\n\nLikes', 'Comments')
for post in posts:
    likes = post["likes"]
    comments = post["comment"]
    print(likes,comment)
