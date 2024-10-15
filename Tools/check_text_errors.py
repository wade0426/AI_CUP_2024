import os
import difflib

# 使用最大相同子串（Longest Common Substring, LCS）
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


# 基於哈希檢查重複行
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


# 檢查換行和空白的數量
def check_text_errors(text):

    # 檢查有多少個 \n 和 " "
    n_newline = text.count("\n")
    n_space = text.count(" ")
    return n_newline, n_space


# pip install scikit-learn
# 基於文本相似度的檢查
from sklearn.feature_extraction.text import CountVectorizer # type: ignore
from sklearn.metrics.pairwise import cosine_similarity # type: ignore

def find_similar_text(text):
    lines = text.splitlines()
    
    # 計算每行文本的餘弦相似度
    vectorizer = CountVectorizer().fit_transform(lines)
    cosine_sim = cosine_similarity(vectorizer)
    
    duplicates = []
    
    # 檢查相似度超過某個閾值（例如0.9）
    for i in range(len(cosine_sim)):
        for j in range(i + 1, len(cosine_sim)):
            if cosine_sim[i, j] > 0.9:
                duplicates.append((i, j, cosine_sim[i, j]))
    
    return duplicates


if __name__ == "__main__":

    path = "D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\finance_301-400\\text\\"
    os.chdir(path)

    # 用來計算平均值
    n_newline_list = []
    n_space_list = []
    # 基於文本相似度的檢查
    similar_text_list = []

    for text_path in os.listdir(path):

        # 開檔
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # print(os.getcwd())

        n_newline, n_space = check_text_errors(text)
        n_newline_list.append(n_newline)
        n_space_list.append(n_space)

        similar_text_list.append(len(find_similar_text(text)))
        print(f"{text_path},換行: {n_newline}, 空白: {n_space}, 相似文本: {len(find_similar_text(text))}")

    newline_average = sum(n_newline_list) / len(n_newline_list)
    space_average = sum(n_space_list) / len(n_space_list)
    similar_text_average = sum(similar_text_list) / len(similar_text_list)

    print(f"\n\n換行平均: {newline_average}")
    print(f"空白平均: {space_average}")
    print(f"相似文本平均: {similar_text_average}")
    # 設定閥值
    n_newline_threshold = newline_average*1.7
    n_space_threshold = space_average*1.8
    similar_text_threshold = similar_text_average*1.8
    bad_text_list = []

    for text_path in os.listdir(path):

        # 開檔
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()

        n_newline, n_space = check_text_errors(text)
        if n_space > n_space_threshold:
            bad_text_list.append(text_path)

    print(f"根據空白閥值，可能壞檔案: {bad_text_list}")

    bad_text_list = []

    for text_path in os.listdir(path):

        # 開檔
        with open(text_path, 'r', encoding='utf-8') as file:
            text = file.read()

        if len(find_similar_text(text)) > similar_text_threshold:
            bad_text_list.append(text_path)

    print(f"根據相似文本閥值，可能壞檔案: {bad_text_list}")
