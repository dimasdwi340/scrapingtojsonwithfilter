from instaloader import Instaloader, Profile

L = Instaloader()

L.login("dim.dimas", "d20m2000")
profile = Profile.from_username(L.context, "dim.dimas")
#print (profile)
#followers = Profile.from_username(L.context, "dim.dimas").get_followers
#print("followers : ".format(profile.username))
#for followers in profile.get_followers():
   #print(followers.username)
#for post in profile.get_posts():
    #L.download_post(post, target=profile.username)
#for simmilar in profile.get_similar_accounts():
 #  print(simmilar.username)
bio = Profile.from_username(L.context, "her_journeys").biography
print (bio)
#jumlahmedia = Profile.from_username(L.context, "dim.dimas").mediacount
#print (jumlahmedia)