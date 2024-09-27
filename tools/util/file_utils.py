import os
from datetime import datetime
import re
import pandas as pd
import shutil


def get_file_created_time(file_path, format='%Y%m%d-%H%M%S'):
    """
    获取文件的创建时间，并按指定格式返回。
    
    参数:
    - file_path: 文件的路径，用于确定文件位置。
    - format: 时间格式，决定返回的时间表示方式，默认为'%Y%m%d-%H%M%S'。
    
    返回:
    - formatted_time: 按指定格式化后的文件创建时间。
    """
    # 使用os模块的path.getctime方法获取文件的创建时间，以秒为单位
    create_time = os.path.getctime(file_path)
    # 将时间戳转换为datetime对象，以便后续格式化
    create_datetime = datetime.fromtimestamp(create_time)
    # 将datetime对象格式化为指定的字符串格式
    formatted_time = create_datetime.strftime(format)
    return formatted_time


def get_file_extension(file_path):
    """
    获取文件的扩展名。

    通过正则表达式匹配文件路径中的扩展名部分，以确定文件的类型。

    参数:
    file_path (str): 文件的路径。

    返回:
    str: 文件的扩展名，如果文件路径中没有扩展名，则返回空字符串。
    """
    # 使用正则表达式查找文件扩展名。正则表达式解释：从字符串末尾开始找，直到遇到第一个点（.）停止，
    # 并获取点后面的所有字符。这个正则表达式可以匹配诸如 '.txt', '.jpg' 这样的扩展名。
    file_extension = re.search(r'\.(\w+)$', file_path)
    
    # 检查是否找到了文件扩展名
    if file_extension:
        # 如果找到了文件扩展名，返回匹配到的完整字符串（即扩展名部分）
        file_extension = file_extension.group(0)
    else:
        # 如果没有找到文件扩展名，初始化为空字符串
        file_extension = ""
    
    # 返回文件扩展名
    return file_extension

def xls_to_xlsx(file_path):
    """
    将给定的Excel文件（.xls）转换为.xlsx格式。
    如果文件已经是.xlsx格式，则直接返回原文件路径。
    
    参数:
    file_path: str - 要转换的文件的路径。
    
    返回:
    str - 转换后文件的路径。
    """
    # 获取文件的扩展名
    file_extension = get_file_extension(file_path)
    # 检查文件是否已经是.xlsx格式
    if file_extension == ".xlsx":
        return file_path
    # 使用pandas读取Excel文件
    df = pd.read_excel(file_path, engine='xlrd')
    # 准备目标文件路径，通过在原路径后添加'x'来创建
    new_file_path = file_path + "x"
    # 将DataFrame保存为新的.xlsx文件
    try:
        df.to_excel(new_file_path, index=False)
        print(file_path)
    except Exception as e:
        print(f"转换文件 {file_path} 失败：{e}")
    return new_file_path


def rename_file(old_file_path, new_file_name):
    """
    重命名文件，并处理可能的错误。

    :param old_file_name: 旧文件名（或完整路径）
    :param new_file_name: 新文件名（或完整路径）
    """
    new_file_path = os.path.join("D:/0_Excel文件/",  new_file_name)
    old_file_path_xlsx = xls_to_xlsx(old_file_path)
    
    # 是xlsx文件，则拷贝一份
    if old_file_path_xlsx == old_file_path:
        copy_file_to_directory(old_file_path, "D:/0_Excel文件/")
    else:
        move_file_to_directory(old_file_path, "D:/backup/")
    
    if old_file_path_xlsx == new_file_path:
        return

    # 检查新文件名是否已存在
    if os.path.exists(new_file_path):
        print("新文件名已存在，请选择其他名称")
        return

    try:
        # 重命名文件
        os.rename(old_file_path_xlsx, new_file_path)
        print(f"文件已成功重命名为 {new_file_path}")
    except FileNotFoundError:
        print(f"文件 {old_file_path_xlsx} 不存在")
    except PermissionError:
        print(f"没有权限重命名文件 {old_file_path_xlsx}")
    except Exception as e:
        print(f"发生错误: {e}")


def move_file_to_directory(file_path, target_directory):
    """
    移动文件到指定目录。

    参数:
    file_path (str): 要移动的文件的路径。
    target_directory (str): 目标目录的路径。

    无返回值。
    """
    try:
        # 确保目标目录存在
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # 移动文件到目标目录
        shutil.move(file_path, target_directory)
    except PermissionError as e:
        # 处理权限错误
        print(f"移动文件失败: 权限错误 - {e}")
    except FileNotFoundError as e:
        # 处理文件或目录不存在的情况
        print(f"移动文件失败: 文件或目录不存在 - {e}")
    except Exception as e:
        # 处理其他错误
        print(f"移动文件失败: 其他错误 - {e}")


def copy_file_to_directory(file_path, target_directory):
    """
    拷贝文件到指定目录。

    参数:
    file_path (str): 要拷贝的文件的路径。
    target_directory (str): 目标目录的路径。

    无返回值。
    """
    try:
        # 确保目标目录存在
        if not os.path.exists(target_directory):
            os.makedirs(target_directory)

        # 构建目标文件的完整路径
        target_file_path = os.path.join(target_directory, os.path.basename(file_path))

        # 拷贝文件到目标目录
        shutil.copy2(file_path, target_file_path)  # 使用 copy2 保留元数据
        # shutil.copy(file_path, target_file_path)  # 使用 copy 不保留元数据
    except PermissionError as e:
        # 处理权限错误
        print(f"拷贝文件失败: 权限错误 - {e}")
    except FileNotFoundError as e:
        # 处理文件或目录不存在的情况
        print(f"拷贝文件失败: 文件或目录不存在 - {e}")
    except Exception as e:
        # 处理其他错误
        print(f"拷贝文件失败: 其他错误 - {e}")