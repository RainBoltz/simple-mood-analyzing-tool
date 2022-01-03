# ettoday-crawler-analyze-tool
 此工具用來簡單計算 ETTODAY 爬蟲結果之詞頻。

## Requirements
 - ETTODAY 爬蟲：[ethan.chen927 的 MEDIUM](https://medium.com/@ethan.chen927/python%E7%B6%B2%E8%B7%AF%E7%88%AC%E8%9F%B2-etoday%E6%96%B0%E8%81%9E-%E6%8A%93%E5%8F%96%E7%89%B9%E5%AE%9A%E5%8D%80%E9%96%93%E6%96%87%E7%AB%A0-%E6%8A%93%E5%88%B0%E9%87%8D%E8%A4%87%E6%96%87%E7%AB%A0%E8%87%AA%E5%8B%95%E8%B7%B3%E9%81%8E-%E5%81%9C%E6%AD%A2-%E4%BD%BF%E7%94%A8selenium-8910a61fddc7)
 - python >= 3.8

## Usage
### command & input
 ```cmd
 python analyze.py <text_file> <positive_dict> <negative_dict>
 ```
 - text_file: 所有新聞內文或標題的單一文字檔路徑
 - positive_dict: 正面情緒實詞彙字典檔路徑
 - negative_dict: 負面情緒實詞彙字典檔路徑
### result & output
 - 會得到 positive_count.csv 和 negative_count.csv 兩檔案，內有詞頻計算結果
