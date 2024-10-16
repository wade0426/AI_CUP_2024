import os


if __name__ == "__main__":

    print("刪除資料夾裡的txt檔案")
    # 確定是否刪除
    confirm = input("是否刪除？(y/n): ")
    if confirm == "y":
        # 定義資料夾 list
        folder_list = ["finance_0-100", "finance_101-200", "finance_201-300", "finance_301-400", "finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]
        # 紀錄刪除的檔案數量
        delete_count = 0

        for folder in folder_list:

            file_path = f"/home/s1110932038/AI_CUP_2024/{folder}/text"
            os.chdir(file_path)
            text_file_list = os.listdir()
            for text_file in text_file_list:
                os.remove(text_file)
                delete_count += 1

            print(f"{folder} 刪除的檔案數量: {delete_count}")
    
        print(f"總共刪除的檔案數量: {delete_count}")

    else:
        print("取消刪除")
