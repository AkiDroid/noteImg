from PIL import Image

# %%-------------------------------
name = 'test.jpg'

img = Image.open(name)

# %%-------------------------------
size = img.size
opt_width = 1200
opt_size = (opt_width, int(opt_width/size[0] * size[1]))
img = img.resize(opt_size, Image.ANTIALIAS)
n = 5
img.save('test-{}.jpg'.format(n), optimize=True, quality=50)
