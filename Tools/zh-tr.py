import opencc
import os
import time

# def convert_simplified_to_traditional(input_file, output_file):
#     converter = opencc.OpenCC('s2twp.json')  # Use s2twp.json for more accurate conversion
#     with open(input_file, 'r', encoding='utf-8') as f:
#         simplified_text = f.read()
#     traditional_text = converter.convert(simplified_text)
#     with open(output_file, 'w', encoding='utf-8') as f:
#         f.write(traditional_text)


def convert_simplified_to_traditional(input_path, output_path):
    try:
        # 初始化轉換器
        converter = opencc.OpenCC('s2t')  # 簡體到繁體

        # 額外的字符映射字典
        extra_chars = {
            '労': '勞',
            '亜': '亞',
            '届': '屆',
            # ... 其他特殊字符
        }

        # 確認輸入文件存在
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"找不到輸入文件：{input_path}")

        # 讀取輸入文件
        with open(input_path, 'r', encoding='utf-8') as file:
            content = file.read()

        # 進行 OpenCC 轉換
        converted_content = converter.convert(content)
        
        # 處理額外的特殊字符
        for old_char, new_char in extra_chars.items():
            converted_content = converted_content.replace(old_char, new_char)

        # 寫入輸出文件
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(converted_content)

        print(f"轉換完成！結果已保存至 {output_path}")

    except FileNotFoundError as e:
        print(f"錯誤：{e}")
    except Exception as e:
        print(f"發生錯誤：{e}")
   

if __name__ == "__main__":
    
    folder_path = "D:/NTCUST/Project/Competition/AI_CUP/AI_CUP_2024/finance_0-100/text/qwen2vl/"
    os.chdir(folder_path)

    start_time = time.time()  # Start time

    # 獲取當前目錄下所有文件
    all_files = os.listdir(folder_path)
    # 排序
    # 如果文件名包含'_'和'.'，則按照'_'前的數字和'.'前的數字進行排序
    # 否則，將文件名視為0
    # 有資料夾會報錯 用這樣解決
    all_files = sorted(all_files, key=lambda x: (int(x.split('_')[0]), int(x.split('_')[1].split('.')[0])) if '_' in x and '.' in x.split('_')[1] else (0, 0))

    for i in all_files:
        # if i.endswith('.txt'):
        #     input_path = i
        #     output_path = i.replace('.txt', '_t.txt')
        #     convert_simplified_to_traditional(input_path, output_path)

        # Example usage:
        input_path = f"{i}"
        output_path = f'./tr/{i}'

        # Replace backslashes with forward slashes
        input_path = input_path.replace('\\', '/')

        convert_simplified_to_traditional(input_path, output_path)

    end_time = time.time()  # End time
    execution_time = end_time - start_time
    print(f"Done! Execution time: {execution_time} seconds")
