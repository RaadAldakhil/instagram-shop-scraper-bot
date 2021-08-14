#to download all the posts of a profile 
import instaloader
#creating object
d = instaloader.Instaloader()
#sepcifying the profile name
profile_Name = 'enter the instagram_handle'
#do profile_pic_only = True, to download the profile picture
d.download_profile(profile_Name, profile_pic_only = False)
#you will notice a folder of this profile's name, under which all the posts will get downloaded
