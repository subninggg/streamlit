from PIL import Image
import os

imgs = ['ge_out21.png', 'ge_safe2.png', 'ge_safe20.png', 'ge_safe24.png', 'ge_safe28.png', 'jy_out4.png', 'sb_out4.png', 'sb_out5.png', 'sb_out24.png', 'sb_safe15.png']

for i in imgs:
    img = Image.open(i)

    img_cropped = img.crop((35,50,2453,1373))

    img_cropped.save(os.path.splitext(os.path.basename(i))[0] + '_crop.png')