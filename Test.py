import jieba

text = "h3c专卖服务器，比如说机架服务器r4900G3系列，内存32g，硬盘至少在500G"
# jieba.cut直接得到generator形式的分词结果
seg = jieba.cut(text)
print(' '.join(seg))

# 也可以使用jieba.lcut得到list的分词结果
seg = jieba.lcut(text)
print(seg)