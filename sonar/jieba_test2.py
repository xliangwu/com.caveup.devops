import jieba

input_file = 'words.csv'
word_freq = {}
with open(input_file, encoding="utf-8") as fp:
    for cnt, line in enumerate(fp):
        fields = line.rstrip('\n').split(',')
        word = fields[0]
        if word in word_freq:
            freq = word_freq[word]
            word_freq[word] = int(freq) + int(fields[1])
        else:
            word_freq[word] = int(fields[1])

print("-----" * 30)
for k, v in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
    if len(k) >= 2 and len(k) <= 8:
        print(k, ",", v)
