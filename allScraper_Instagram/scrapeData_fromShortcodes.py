from instaloader import Instaloader, Post

L = Instaloader()
SHORTCODE = 'CoL7-iQDHIm'

post = Post.from_shortcode(L.context, SHORTCODE)
L.download_post(post, target='abc')

#for post in L.get_hashtag_posts(HASHTAG):
 #   L.download_post(post, target='#'+HASHTAG)
