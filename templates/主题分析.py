import pandas as pd
import numpy as np
import gensim
from gensim import corpora
from gensim.models import LdaModel
from gensim.models import CoherenceModel
import pyLDAvis.gensim

# 读取数据
data = pd.read_csv('维吾尔词云.csv')  # 替换为实际数据文件路径

# 数据预处理
# ...

# 构建词袋模型
texts = data['text'].apply(lambda x: x.split())  # 替换为实际文本数据列名
dictionary = corpora.Dictionary(texts)
corpus = [dictionary.doc2bow(text) for text in texts]

# 训练LDA模型
lda_model = LdaModel(corpus=corpus, id2word=dictionary, num_topics=10)  # 设置主题数目

# 主题聚类结果
topics = lda_model.print_topics(num_words=10)  # 输出每个主题的前10个关键词
for topic in topics:
    print(topic)

# 计算主题一致性得分
coherence_model = CoherenceModel(model=lda_model, texts=texts, dictionary=dictionary, coherence='c_v')
coherence_score = coherence_model.get_coherence()
print("Coherence Score:", coherence_score)

# 可视化结果
vis_data = pyLDAvis.gensim.prepare(lda_model, corpus, dictionary)
pyLDAvis.display(vis_data)
