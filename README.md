---

**2024/10/15 更新**  
發現 `finance_304-400` 資料夾中存在錯誤檔案。
[304_28.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/304_28.txt>)

[331_2.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/331_2.txt>)

[375_2.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/375_2.txt>)

[366_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/366_1.txt>)

[301_21.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/301_21.txt>)

[359_5.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/359_5.txt>)

[333_8.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/333_8.txt>)

[304_2.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/304_2.txt>)

[345_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/345_1.txt>)

[325_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/325_1.txt>)

[303_2.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/303_2.txt>)

[383_8.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/383_8.txt>)

[387_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/387_1.txt>)

[318_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/318_1.txt>)

[340_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/340_1.txt>)

[306_1.txt](<https://github.com/wade0426/AI_CUP_2024/blob/main/finance_301-400/text/306_1.txt>)

---


# 10/9 進度報告

## 資料夾定義
finance(裡面存放文字的PDF)/  
├──text(裡面存放文字的PDF提取的TXT檔案)/  
├──table(裡面存放表格的PDF)/  
└──images(裡面存放表格PDF轉換的圖片)/  

## 數據格式分佈：
- **檔案總數：** 1035 份 PDF
  - **表格（難以提取）：** 818 份檔案 (79.02%)
  - **文字：** 217 份 PDF (20.98%)
  - **圖片：** 已將包含表格的 PDF 轉換為 4177 張圖片以便提取。

※資料可能有miss需要二次檢查

## 資料分類定義：

### 文字
- **Finace:** 包含 217 份 PDF，主要為文字內容，較易處理。
- **Finace/text:** 從 212 份較易處理的 PDF 中提取的文字。

### 表格
- **Finace/table:** 包含 818 份包含表格的 PDF，這些檔案較難提取，需要使用 AI 技術提取。
- **Finace/image:** 從包含表格的 PDF 轉換的 4177 張圖片，以便 AI 提取。

## 提取格式：
提取共有四種格式。以下以 [6_1.png](https://github.com/wade0426/AI_CUP_2024/blob/main/finance/images/6_1.png) 為例：

- **版本 1**：佔位符標籤，參見範例結果：  
  [6-r1.txt](https://github.com/wade0426/AI_CUP_2024/blob/main/finance/text/6-r1.txt)
  
- **版本 2**：使用 JSON（資源需求較高），參見範例結果：  
  [6-r2.txt](https://github.com/wade0426/AI_CUP_2024/blob/main/finance/text/6-r2.txt)
  
- **版本 3**：使用 CSV 標記，參見範例結果：  
  [6-Q-r1.txt](https://github.com/wade0426/AI_CUP_2024/blob/main/finance/table/demo/6-Q-r1.txt)
  
- **版本 4**：無 CSV 標記（使用換行符），參見範例結果：  
  [6-Q-r2.txt](https://github.com/wade0426/AI_CUP_2024/blob/main/finance/table/demo/6-Q-r2.txt)
