import os
import shutil

# 輸入新的檔案 和 舊的檔案資料夾
# 取代舊的檔案資料夾中的檔案
def replace_old_files():

    
    folder_list = ["finance_0-100", "finance_101-200", "finance_201-300", "finance_301-400", "finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]
    
    for folder in folder_list:
        # 新的檔案資料夾
        new_folder = f"D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\again_text\\{folder}\\"
        # 要取代的檔案資料夾
        old_folder = f"D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\{folder}\\text\\v4\\"

        new_folder_list = os.listdir(new_folder)
        old_folder_list = os.listdir(old_folder)

        for new_file in new_folder_list:
            if new_file in old_folder_list:
                # 这行代码使用 shutil.copy2() 函数将新文件复制到旧文件夹中
                # shutil.copy2() 不仅复制文件内容，还保留文件的元数据（如创建时间、修改时间等）
                # f"{new_folder}{new_file}" 是源文件路径，f"{old_folder}{new_file}" 是目标文件路径
                shutil.copy2(f"{new_folder}{new_file}", f"{old_folder}{new_file}")
                print(f"已替換: {old_folder}{new_file}")
            else:
                print(f"舊檔案不存在，無法替換: {old_folder}{new_file}")

if __name__ == "__main__":
    replace_old_files()
    print("完成")