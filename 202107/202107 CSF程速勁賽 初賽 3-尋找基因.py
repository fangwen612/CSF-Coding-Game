
START = ['ATG']
END = ['TAG', 'TAA', 'TGA']

dna = input()
gene_lst = []  # 存放基因


def 檢查是否基因片段(string):
    for e in START + END:  #
        if string.find(e) != -1:
            return False

    if len(string) % 3 != 0:
        return False

    return True


i = 0
while True:
    if i > len(dna):
        break

    if dna[i:i+3] in START:  # 檢查是否為基因開頭
        for e in END:
            # 取出以 e 結尾的片段來檢查
            tmp = dna[i+3:].split(e)[0]

            if tmp and 檢查是否基因片段(tmp):
                gene_lst.append(tmp)
                # 設定下一次檢查的起始位置
                i = (i+2) + len(tmp) + 2
                break

    i += 1

if len(gene_lst) > 0:
    for g in gene_lst:
        print(g)
else:
    print('沒有基因')
