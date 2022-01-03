import sys


# 載入正負情緒字典檔
def load_dict_data(positive_dict_file, negative_dict_file):
    print("load data")
    p = []
    n = []
    with open(positive_dict_file, encoding="utf-8-sig") as f:
        for line in f:
            p.append(line.strip())
    with open(negative_dict_file, encoding="utf-8-sig") as f:
        for line in f:
            n.append(line.strip())
    return p, n


# 計算詞頻
def count_words(p, n, data_string):
    p_count = {}
    n_count = {}
    for w in p:
        p_count[w] = data_string.count(w)
    for w in n:
        n_count[w] = data_string.count(w)
    return p_count, n_count


# 輸出結果至Excel檔
def output_results(p_count, n_count):
    with open("positive_count.csv", "w", encoding="utf-8-sig") as f:
        for k, v in p_count.items():
            f.write(f"{k},{v}\n")
    with open("negative_count.csv", "w", encoding="utf-8-sig") as f:
        for k, v in n_count.items():
            f.write(f"{k},{v}\n")


# 執行程式
if __name__ == "__main__":
    text_file = sys.argv[1]
    positive_dict_file = sys.argv[2]
    negative_dict_file = sys.argv[3]

    p, n = load_dict_data(positive_dict_file, negative_dict_file)
    data_string = open(text_file, encoding="utf-8-sig").read()
    p_count, n_count = count_words(p, n, data_string)
    output_results(p_count, n_count)
