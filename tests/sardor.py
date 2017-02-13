from wand.image import Image
from wand.display import display


with Image(filename='sardor.jpg') as bg_img:
    with Image(filename='footer.png') as fg_img:
        bg_img.composite(
            fg_img,
            left=(bg_img.height - fg_img.height) - 100,
            top=bg_img.width - fg_img.width)
        bg_img.save(filename='aaaaaaaaaaa.jpg')
    fg.close()
    # display(bg_img)
bg.close()
