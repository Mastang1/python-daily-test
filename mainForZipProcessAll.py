import os
import zipfile
 
def zip_folder(folder_path, output_path):
    # 创建一个 ZipFile 对象，并指定压缩文件的路径和模式（写模式）
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        # os.walk() 生成文件夹中的文件名和子文件夹名
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                # 获取文件相对路径
                file_path = os.path.join(root, file)
                # 在 ZIP 文件中添加文件，并将路径设置为相对路径
                zipf.write(file_path, os.path.relpath(file_path, folder_path))
 
# 使用方法示例

zip_folder('./', 'aaaa.zip')