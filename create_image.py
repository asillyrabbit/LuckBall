import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import config

# 生成彩票
def create_image(luck_ball):
    # 图片上写数字的字体(自定义的手写风)
    font = ImageFont.truetype(config.project_dir + 'ziti.ttf', 11)

    # 打开模板图片
    imageFile = config.project_dir + 'moban.png'
    im1 = Image.open(imageFile)

    # 把号码写到模板图片上
    draw = ImageDraw.Draw(im1)
    draw.text((14, 63), luck_ball,'black',font=font)    #设置文字位置/内容/颜色/字体
    draw = ImageDraw.Draw(im1)   

    # 保存图片
    im1.save(config.project_dir + 'luckball.png')