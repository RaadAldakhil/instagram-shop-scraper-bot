from instagramy import Instagram

# Connect to profile
user = Instagram("raad.aldakhil")

print(user.popularity())
print(user.get_biography())

posts = user.get_posts_details()

print('\n\nLikes', 'Comments')
for post in posts:
    likes = post["likes"]
    comments = post["comment"]
    print(likes,comment)
