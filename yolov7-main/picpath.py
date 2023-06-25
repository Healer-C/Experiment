import os
import glob

# 指定文件夹路径
# folder_path = r'F:\CXY\WorkPlace\PycharmProjects\yolov7-main\datasets\images\\train'
folder_path = r'F:\CXY\WorkPlace\PycharmProjects\yolov7-main\datasets\images\\val'

# 获取所有图片文件的绝对路径
image_paths = glob.glob(os.path.join(folder_path, '*.jpg')) + \
              glob.glob(os.path.join(folder_path, '*.jpeg')) + \
              glob.glob(os.path.join(folder_path, '*.png')) + \
              glob.glob(os.path.join(folder_path, '*.gif'))

# 将路径存储到txt文件中
with open('./datasets/val_list.txt', 'w') as f:
    for path in image_paths:
        f.write(path + '\n')
