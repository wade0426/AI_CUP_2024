import os
import zipfile

# 傳入 資料夾名稱   輸出 zip 檔案路徑
def zip_files(folder_name, output_path):
    
    folder_list = ["finance_0-100", "finance_101-200", "finance_201-300", "finance_301-400", "finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]
    
    # 這行程式碼用於創建壓縮檔案的完整路徑
    # os.path.join() 函數用於組合路徑
    # output_path 是指定的輸出目錄
    # f"{folder_name}.zip" 是使用 f-string 創建的檔案名稱，其中 folder_name 是傳入的資料夾名稱
    # 最終生成的 zip_filename 將是完整的壓縮檔案路徑，例如 "/path/to/output/folder_name.zip"
    zip_filename = os.path.join(output_path, f"{folder_name}.zip")
    
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for folder in folder_list:
            path = f"/home/s1110932038/AI_CUP_2024/{folder}/{folder_name}/"
            
            if not os.path.exists(path):
                print(f"資料夾不存在: {path}")
                continue
            
            file_list = os.listdir(path)
            for file in file_list:
                if file.endswith('.txt'):
                    file_path = os.path.join(path, file)
                    arcname = os.path.join(folder, file)
                    zipf.write(file_path, arcname)
    
    print(f"已將所有txt檔案壓縮到: {zip_filename}")
    return zip_filename

if __name__ == "__main__":
    # /home/s1110932038/AI_CUP_2024/finance_0-100/again_text/
    zip_files("again_text", "/home/s1110932038/AI_CUP_2024/")