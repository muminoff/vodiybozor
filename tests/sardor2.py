try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

from wand.image import Image
from wand.display import display


fg_url = 'http://imgur.com/download/CrGVjV6'
# bg_url = 'http://i.stack.imgur.com/TAcBA.jpg'
bg_url = 'https://api.telegram.org/file/bot319964417:AAFkLUJNM7EQBPsJcD5yxSlgzHPiE6FT048/photo/file_16.jpg'
# bg_url = 'http://buyersguide.caranddriver.com/media/assets/submodel/7671.jpg'

bg = urllib2.urlopen(bg_url)
with Image(file=bg) as bg_img:
    fg = urllib2.urlopen(fg_url)
    with Image(file=fg) as fg_img:
    # with Image(file=fg) as fg_img:
        bg_img.composite(
            fg_img,
            left=int((bg_img.width-fg_img.width) / 2),
            top=bg_img.height-fg_img.height)
    fg.close()
    display(bg_img)
bg.close()
