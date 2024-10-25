import os

def merge_files(folder_path):
    # 獲取當前目錄下所有文件
    all_files = os.listdir(folder_path)
    # 排序
    all_files = sorted(all_files, key=lambda x: int(x.split('_')[0]))
    
    # 用於存儲合併後的文件內容
    merged_contents = {}
    
    for file in all_files:
        if file.endswith('.txt'):
            file_number = file.split('_')[0]
            with open(os.path.join(folder_path, file), 'r', encoding='utf-8') as f:
                content = f.read()
                if file_number in merged_contents:
                    merged_contents[file_number] += '\n' + content
                else:
                    merged_contents[file_number] = content
    
    # 寫入合併後的文件
    for file_number, content in merged_contents.items():
        with open(os.path.join(folder_path, f"{file_number}.txt"), 'w', encoding='utf-8') as f:
            f.write(content)

    # 刪除合併前的文件
    for file in all_files:
        if file.endswith('.txt'):
            os.remove(os.path.join(folder_path, file))
    
    print("文件合併完成")

if __name__ == "__main__":
    folder_path = "D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\done\\txt"
    merge_files(folder_path)