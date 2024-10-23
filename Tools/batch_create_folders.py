import os

if __name__ == "__main__":

    folder_list = ["finance_0-100", "finance_101-200", "finance_201-300", "finance_301-400", "finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]
    # "D:\NTCUST\Project\Competition\AI_CUP\AI_CUP_2024\{folder}\text"
    os.chdir(f"D:/NTCUST/Project/Competition/AI_CUP/AI_CUP_2024")

    print(f"目前路徑: {os.getcwd()}")
    folder_name = input("請輸入資料夾名稱: ")
    count = 0

    for folder in folder_list:
        if not os.path.exists(f"{folder}/text/{folder_name}"):
            os.mkdir(f"{folder}/text/{folder_name}")
            print(f"已創建資料夾: {folder}/text/{folder_name}")
            count += 1
        else:
            print(f"已存在: {folder}/text/{folder_name}")
    print(f"完成，共創建了 {count} 個資料夾")