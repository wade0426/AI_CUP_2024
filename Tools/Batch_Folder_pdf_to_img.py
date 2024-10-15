import os


# 定義資料夾 list
folder_list = ["finance_401-500", "finance_501-600", "finance_601-700", "finance_701-800", "finance_801-900", "finance_901-1034"]

for i in folder_list:

    # /home/s1110932038/AI_CUP_2024/finance_401-500/pdf
    pdf_path = "/home/s1110932038/AI_CUP_2024/" + i + "/pdf"

    # 輸入 pdf 檔案路徑
    # pdf_path = input("輸入 pdf 檔案路徑:")
    # pdf_path = pdf_path.replace("\\", "/")
    # pdf_path = pdf_path.replace("\"", "")

    os.chdir(pdf_path)
    print("當前路徑:", os.getcwd())

    import pdfplumber # type: ignore

    # 獲取當前目錄下所有文件
    all_files = os.listdir(pdf_path)
    # 過濾 只保留 .pdf 的檔案
    all_files = [file for file in all_files if file.endswith(".pdf")]

    # 讀取當前路徑的 i.pdf 檔案。
    for i in all_files:
        with pdfplumber.open(i) as pdf:
            for page in pdf.pages:
                image = page.to_image(resolution=300) # 最高應該是300dpi
                image.save(f"../png/{i.replace('.pdf', '')}_{page.page_number}.png", format="PNG", quality=100)
            print(f"{i}的圖片已存檔完成")

    print("done")

print("已經完成所有資料夾的轉換")