import cairosvg
import os
from PIL import Image


def svg_to_jpg(svg_path, jpg_path, scale=1.0):
    # 首先，将SVG转换为PNG（cairosvg不直接支持JPG）
    # scale参数可以用来调整输出图片的大小
    cairosvg.svg2png(url=svg_path, write_to=svg_path.replace('.svg', '.png'), scale=scale)

    # 接着，使用Pillow将PNG转换为JPG
    png_path = svg_path.replace('.svg', '.png')
    img = Image.open(png_path)
    rgb_img = img.convert('RGB')  # 转换为RGB，因为JPG不支持透明度
    rgb_img.save(jpg_path, 'JPEG', quality=95)  # quality参数控制JPG的质量

    # 清理：删除生成的PNG文件（如果你不需要它的话）
    os.remove(png_path)


# 使用示例
svg_path = '小米.svg'  # 你的SVG文件路径
jpg_path = '小米.jpg'  # 你想要生成的JPG文件路径
svg_to_jpg(svg_path, jpg_path)
