import os
from PIL import Image

def image_slicer(input_path, output_path, cut_length):
    # 打開圖像
    img = Image.open(input_path)
    width, height = img.size

    # 如果圖像高度小于等于切割長度，不需要切割
    if height <= cut_length:
        img.save(os.path.join(output_path, os.path.basename(input_path)))
        return

    # 切割圖像為兩半
    top_half = img.crop((0, 0, width, cut_length))
    bottom_half = img.crop((0, cut_length, width, height))
    
    # 生成輸出文件名
    base_name, ext = os.path.splitext(os.path.basename(input_path))
    top_output_file = f"{base_name}_top{ext}"
    bottom_output_file = f"{base_name}_bottom{ext}"
    
    # 保存兩半圖像
    top_half.save(os.path.join(output_path, top_output_file))
    bottom_half.save(os.path.join(output_path, bottom_output_file))

if __name__ == "__main__":
    input_path = "D:/NTCUST/Project/Competition/AI_CUP/AI_CUP_2024/finance_301-400/png/387_1.png"  # 替换为实际的输入图像路径
    output_path = "D:/NTCUST/Project/Competition/AI_CUP/AI_CUP_2024/finance_301-400/png/"   # 替换为实际的输出文件夹路径
    cut_length = 1450

    image_slicer(input_path, output_path, cut_length)