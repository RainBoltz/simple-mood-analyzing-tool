# Simple 'Mood Analyzing' Tool
 此小工具可用來簡單計算文字檔內之正負情緒詞彙詞頻。

## Requirements
 - python >= 3.8

## Usage
### command & input
 ```cmd
 python analyze.py <text_file> <positive_dict> <negative_dict>
 ```
 - text_file: 所有單一文字檔路徑
 - positive_dict: 正面情緒實詞彙字典檔路徑
 - negative_dict: 負面情緒實詞彙字典檔路徑
### result & output
 - 會得到 positive_count.csv 和 negative_count.csv 兩檔案，內有詞頻計算結果
