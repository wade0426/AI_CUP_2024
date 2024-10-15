import os
import difflib

def find_duplicates(text):
    # 分行處理文本
    lines = text.splitlines()
    # 找到行之間的相似度
    d = difflib.Differ()
    diff = d.compare(lines, lines)
    
    # 檢查行與行之間的重複
    duplicates = []
    for i, line in enumerate(diff):
        if line.startswith("  "):  # 相同的行
            duplicates.append((i, lines[i]))
    
    return duplicates


def find_duplicate_lines(text):
    lines = text.splitlines()
    seen = set()  # 用來存儲哈希值
    duplicates = []
    
    for i, line in enumerate(lines):
        line_hash = hash(line)
        if line_hash in seen:
            duplicates.append((i, line))
        else:
            seen.add(line_hash)
    
    return duplicates


def check_text_errors(text):

    # 檢查有多少個 \n 和 " "
    n_newline = text.count("\n")
    n_space = text.count(" ")
    return n_newline, n_space


if __name__ == "__main__":

    path = "D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\finance_301-400\\text\\"
    os.chdir(path)

    # 用來計算平均值
    n_newline_list = []
    n_space_list = []

    for text_path in os.listdir(path):

        # 開檔
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # print(os.getcwd())

        n_newline, n_space = check_text_errors(text)
        n_newline_list.append(n_newline)
        n_space_list.append(n_space)

        print(f"n_newline: {n_newline}, n_space: {n_space}")

        # print(len(find_duplicates(text)))
    newline_average = sum(n_newline_list) / len(n_newline_list)
    space_average = sum(n_space_list) / len(n_space_list)
    print(f"換行平均: {newline_average}")
    print(f"空白平均: {space_average}")

    # 設定閥值
    # n_newline_threshold = newline_average*1.7
    n_space_threshold = space_average*1.8

    bad_text_list = []

    for text_path in os.listdir(path):

        # 開檔
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()

        n_newline, n_space = check_text_errors(text)
        if n_space > n_space_threshold:
            bad_text_list.append(text_path)

    print(f"根據空白閥值，可能壞檔案: {bad_text_list}")