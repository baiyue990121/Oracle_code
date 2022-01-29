from stanfordcorenlp import StanfordCoreNLP
from nltk.tree import Tree

nlp = StanfordCoreNLP(r'/Users/baiyue/Oracle/tools/stanford-corenlp-4.4.0')

# sentence = 'Guangdong University of Foreign Studies is located in Guangzhou.'
sentence = 'How long does it take to get to the zoo by taxi?'
# print("Tokenize:", nlp.word_tokenize(sentence))
# print('Part of Speech:', nlp.pos_tag(sentence))
# print('Named Entities:', nlp.ner(sentence))
# print('Constituency Parsing:', nlp.parse(sentence))
# tree=Tree.fromstring(nlp.dependency_parse(sentence))
# tree.draw()
print('Dependency Parsing:', nlp.dependency_parse(sentence))

nlp.close()
# Do not forget to close!

# sentence = '清华大学位于北京。'
# with StanfordCoreNLP(r'D:\stanfordNLP\stanford-corenlp-4.4.0', lang='zh') as nlp:
#     print(nlp.word_tokenize(sentence))
#     print(nlp.pos_tag(sentence))
#     print(nlp.ner(sentence))
#     print(nlp.parse(sentence))
#     print(nlp.dependency_parse(sentence))

# Tokenize: ['Guangdong', 'University', 'of', 'Foreign', 'Studies', 'is', 'located', 'in', 'Guangzhou', '.']
# Part of Speech: [('Guangdong', 'NNP'), ('University', 'NNP'), ('of', 'IN'), ('Foreign', 'NNP'), ('Studies', 'NNPS'),
# ('is', 'VBZ'), ('located', 'JJ'), ('in', 'IN'), ('Guangzhou', 'NNP'), ('.', '.')]
# Named Entities: [('Guangdong', 'ORGANIZATION'), ('University', 'ORGANIZATION'), ('of', 'ORGANIZATION'),
# ('Foreign', 'ORGANIZATION'), ('Studies', 'ORGANIZATION'), ('is', 'O'), ('located', 'O'), ('in', 'O'),
# ('Guangzhou', 'CITY'), ('.', 'O')]
# Constituency Parsing: (ROOT
#   (S
#     (NP
#       (NP (NNP Guangdong) (NNP University))
#       (PP (IN of)
#         (NP (NNP Foreign) (NNPS Studies))))
#     (VP (VBZ is)
#       (ADJP (JJ located)
#         (PP (IN in)
#           (NP (NNP Guangzhou)))))
#     (. .)))
# Dependency Parsing: [('ROOT', 0, 7), ('compound', 2, 1), ('nsubjpass', 7, 2), ('case', 5, 3),
# ('compound', 5, 4), ('nmod', 2, 5), ('auxpass', 7, 6), ('case', 9, 8), ('nmod', 7, 9), ('punct', 7, 10)]
# ['清华', '大学', '位于', '北京', '。']
# [('清华', 'NR'), ('大学', 'NN'), ('位于', 'VV'), ('北京', 'NR'), ('。', 'PU')]
# [('清华', 'ORGANIZATION'), ('大学', 'ORGANIZATION'), ('位于', 'O'), ('北京', 'STATE_OR_PROVINCE'), ('。', 'O')]
# (ROOT
#   (IP
#     (NP (NR 清华) (NN 大学))
#     (VP (VV 位于)
#       (NP (NR 北京)))
#     (PU 。)))
# [('ROOT', 0, 3), ('compound:nn', 2, 1), ('nsubj', 3, 2), ('dobj', 3, 4), ('punct', 3, 5)]

# import jieba
# import os
# from nltk.parse import stanford
# from nltk.parse import corenlp
# from stanfordcorenlp import StanfordCoreNLP
# import nltk.parse.corenlp
#
# if __name__ == "__main__":
#     string = '他骑自行车去了菜市场'
#     string2 = "小明早上刷了牙洗完脸之后就在客厅里吃着妈妈做的早餐"
#     seg_list = jieba.cut(string, cut_all=False, HMM=True)
#     set_str = " ".join(seg_list)
#     print(set_str)
#     seg_list1 = jieba.cut(string2, cut_all=False, HMM=True)
#     set_str1 = " ".join(seg_list1)
#     print(set_str1)
#
#     # 指定java_home路径
#     if not os.environ.get('JAVA_HOME'):
#         JAVA_HOME = 'C:\\Program Files\\Java\\jdk1.8.0_251'
#         os.environ['JAVA_HOME'] = JAVA_HOME
#
#     # PCFG模型路径
#     pcfg_path = 'edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz'
#
#     # parser = StanfordCoreNLP.
#
#     # parser = corenlp.CoreNLPParser('D:\\yangyang\\stanford\\standfordnlp\\stanfordcorenlp2018',
#     #                               'D:\\yangyang\\stanford\\stanford-chinese-corenlp-2018-10-05-models.jar', pcfg_path,
#     #                               'pos')
#
#     # sentence = parser.parse(set_str)
#
#     # PCFG模型路径
#     pcfg_path = 'edu/stanford/nlp/models/lexparser/chinesePCFG.ser.gz'
#
#     # parser = stanford.StanfordParser(
#     #    path_to_jar="D:\\yangyang\\stanford\\standfordnlp\\stanfordcorenlp2018\\stanford-corenlp-3.9.2.jar",
#     #    path_to_models_jar="D:\\yangyang\\stanford\\stanford-chinese-corenlp-2018-10-05-models.jar",
#     #    model_path=pcfg_path
#     # )
#
#     parser = corenlp.CoreNLPParser()
#     sentence = parser.parse(set_str)
#
#     for line in sentence:
#         print(line.leaves())
#         line.draw()


# from nltk.parse.stanford import StanfordParser
#
# eng_parser = StanfordParser(model_path=u'edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz')
# print(list(eng_parser.parse("the quick brown fox jumps over the lazy dog".split())))