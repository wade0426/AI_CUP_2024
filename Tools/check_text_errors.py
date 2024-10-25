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


# 檢查相似度 輸入字串和文件內容
def check_similarity(input_string, file_content):
    # 將輸入字串和文件內容放入列表中
    documents = [input_string, file_content]
    
    # 使用CountVectorizer進行文本向量化
    vectorizer = CountVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    
    # 計算餘弦相似度
    cosine_sim = cosine_similarity(vectors)
    
    # 找出文本中分數最高的字串
    file_content_lines = file_content.splitlines()
    max_similarity = 0
    max_similarity_string = ""
    
    for line in file_content_lines:
        if line.strip():  # 忽略空行
            line_vectorizer = CountVectorizer()
            line_similarity = cosine_similarity(
                line_vectorizer.fit_transform([input_string, line])
            )[0][1]
            if line_similarity > max_similarity:
                max_similarity = line_similarity
                max_similarity_string = line
    
    # 返回相似度值（第一個與第二個的相似度）和分數最高的字串
    return cosine_sim[0][1], max_similarity_string


# 檢查相似度 輸入字串和文件內容 返回相似度
def check_similarity_return_similarity(input_string, file_content):
    
    # 將輸入字串和文件內容放入列表中
    documents = [input_string, file_content]
    
    # 使用CountVectorizer進行文本向量化
    vectorizer = CountVectorizer().fit_transform(documents)
    vectors = vectorizer.toarray()
    
    # 計算餘弦相似度
    cosine_sim = cosine_similarity(vectors)
    
    # 返回相似度值（第一個與第二個的相似度）
    return cosine_sim[0][1]


# 查看正確率 傳入 可能壞檔案 和 人工檢驗的錯誤資料
def check_correct_rate(bad_text_list=[], error_comparison_list=[]):

    # 定義錯誤對比資料
    # error_comparison_list = [
    #     "301_15.txt", "301_25.txt", "325_1.txt", "327_36.txt", "328_1.txt", "340_1.txt", "340_1.txt", "351_1.txt", 
    #     "359_15.txt", "359_5.txt", "360_1.txt", "361_2.txt", "362_2.txt", "363_2.txt", "363_3.txt", "364_2.txt", 
    #     "366_1.txt", "367_2.txt", "372_1.txt", "375_2.txt", "377_1.txt", "378_1.txt", "382_1.txt", "383_8.txt", 
    #     "384_1.txt", "385_1.txt", "387_1.txt", "387_1.txt", "387_2.txt", "392_1.txt", "393_2.txt", "394_2.txt", 
    #     "396_1.txt", "396_3.txt", "398_10.txt", "398_2.txt", "398_21.txt", "398_21.txt", "398_26.txt", "398_27.txt", 
    #     "398_28.txt", "398_37.txt", "398_38.txt", "398_39.txt", "398_4.txt", "398_40.txt", "398_41.txt", "398_42.txt", 
    #     "398_6.txt", "400_1.txt"
    # ]

    # similar_bad_text_list 和 error_comparison_list 比較 看正確率
    # correct = 0
    # for i in similar_bad_text_list:
    #     if i in error_comparison_list:
    #         correct += 1
    # print(f"\n相似文本閥值，可能壞檔案正確率: {correct/len(similar_bad_text_list)}")

    correct = 0
    for i in bad_text_list:
        if i in error_comparison_list:
            correct += 1
    return correct/len(bad_text_list)


def main():
    # 用來計算平均值
    n_newline_list = []
    n_space_list = []
    # 基於文本相似度的檢查
    similar_text_list = []
    return_All_bad_text_list = []
    
    folder_list = ["finance_0-100", "finance_101-200", "finance_201-300", "finance_301-400", "finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]

    for folder in folder_list:
        path = f"D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\again_text\\{folder}\\"
        # path = f"D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\{folder}\\text\\v4\\"
        os.chdir(path)

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
        n_space_threshold = space_average*4
        similar_text_threshold = 300
        # similar_text_threshold = similar_text_average*11.6
        # 可能壞檔案 空白
        space_bad_text_list = []
        # 可能壞檔案 相似文本
        similar_bad_text_list = []

        for text_path in os.listdir(path):

            # 開檔
            with open(text_path, 'r', encoding='utf-8') as file:
                text = file.read()

            n_newline, n_space = check_text_errors(text)
            if n_space > n_space_threshold:
                space_bad_text_list.append(text_path)
            
            if len(find_similar_text(text)) > similar_text_threshold:
                similar_bad_text_list.append(text_path)

        # print(f"根據空白閥值，可能壞檔案: {space_bad_text_list}\n")
        # print(f"根據相似文本閥值，可能壞檔案: {similar_bad_text_list}\n")
        # print(f"\n聯集: {space_bad_text_list + similar_bad_text_list}")
        print(f"\n聯集: {similar_bad_text_list}")

        return_All_bad_text_list.extend(similar_bad_text_list)
    
    # 將聯集 list 使用 py 存檔
    output_path = "D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024"
    with open(f"{output_path}\\All_bad_text_list.py", 'w', encoding='utf-8') as file:
        file.write(f"bad_text_list = {return_All_bad_text_list}")


if __name__ == "__main__":

    main()

    

#     path = "D:\\NTCUST\\Project\\Competition\\AI_CUP\\AI_CUP_2024\\finance_0-100\\text\\v2\\"
#     os.chdir(path)

#     # 0.21高
#     with open("4_1.txt", 'r', encoding='utf-8') as file:
#         file_content = file.read()

#     print()
#     print(check_similarity_return_similarity("""| 项目 | 112年3月31日 | 111年12月31日 | 111年3月31日 |
# |------|--------------|---------------|--------------|
# | 庫存现金 | $ 1,777 | $ 1,750 | $ 2,137 |
# | 活期存款 | 25,699,639 | 33,243,220 | 39,578,483 |
# | 总计 | $ 77,674,551 | $ 91,065,529 | $ 68,517,225 |""", file_content))
#     print()
    
    # 0.159
    # similarity, max_similarity_string = check_similarity("""输入图像描述：财务报告页面的图像，包含""", file_content)
    # print(f"\n相似度: {similarity}")
    # print(f"最高相似文本: {max_similarity_string}\n")
