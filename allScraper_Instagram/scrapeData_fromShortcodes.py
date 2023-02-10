from instaloader import Instaloader, Post

L = Instaloader()
# code to strip shortcodes from csv files in post_links
# store in scrapedData by folders
SHORTCODE = 'CoL7-iQDHIm'

post = Post.from_shortcode(L.context, SHORTCODE)
L.download_post(post, target='abc')

#for post in L.get_hashtag_posts(HASHTAG):
 #   L.download_post(post, target='#'+HASHTAG)
