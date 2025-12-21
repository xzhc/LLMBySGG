"""
This case demonstrates file copying
"""
import shutil


# def file_copy(source_file_path, dest_file_path):
#     #Open source file
#     source_file = open(source_file_path, 'rb')
#     #open target file
#     target_file = open(dest_file_path, 'wb')
#
#     #Read data from source file
#     content = source_file.read()
#
#     #Write the content file to target file
#     target_file.write(content)
#
#     #Close the source file
#     source_file.close()
#     #Close the target file
#     target_file.close()
#

#Optimization:Do not read all file content at once, read data of specified byte size
def file_copy(source_file_path, target_file_path):
    source_file = open(source_file_path, 'rb')
    target_file = open(target_file_path, 'wb')

    content = source_file.read(1024)

    while content:
        target_file.write(content)
        content = source_file.read(1024)

    source_file.close()
    target_file.close()

file_copy("G:\\图片\\【哲风壁纸】刘浩存2-女明星.png", "F:\\Tech\\SoftwareEnginner\\LLMBySGG\\python\\day08\\lhc.png")


