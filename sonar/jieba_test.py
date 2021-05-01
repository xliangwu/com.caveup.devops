import jieba

text = "招商银行客户身份识别和客户身份资料及交易记录保存管理办法"
seg = jieba.cut(text)
print(" ".join(seg))

input_file = 'words.csv'
word_freq = {}
with open(input_file, encoding="utf-8") as fp:
    for cnt, line in enumerate(fp):
        fields = line.rstrip('\n').split(',')
        seg = jieba.lcut(fields[0])

        for word in seg:
            if word in word_freq:
                freq = word_freq[word]
                word_freq[word] = int(freq) + int(fields[1])
            else:
                word_freq[word] = int(fields[1])

print("-----" * 30)
for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
    if len(k) >= 2:
        print(k, ",", v)
