from stanfordcorenlp import StanfordCoreNLP
from graphviz import Digraph

def dependency(sentence, language='zh'):
    """
    使用Stanfordcorenlp构建依存树
    :param sentence: 需要构建树的句子
    :param language: 支持的语言
    :return: 依存序列
    """
    nlp_zh = StanfordCoreNLP(r'/Users/baiyue/Oracle/tools/stanford-corenlp-4.4.0')  # 导入解压之后的路径
    words = list(nlp_zh.word_tokenize(sentence))  # 分词
    depend = list(nlp_zh.dependency_parse(sentence))  # 依存关系
    return depend, words


def Dependency_tree_visualization(dependency_tree, words):
    """
    将依存序列与对应的单词进行匹配，并将依存树可视化，最终将依存树图片保存为jpg
    :param dependency_tree: 依存树序列
    :param words: 经过
    :return:
    """
    dependency_tree.sort(key=lambda x: x[2])  # 排序
    words = [w + "-" + str(idx) for idx, w in enumerate(words)]
    rely_id = [arc[1] for arc in dependency_tree]  # 依存ID
    relation = [arc[0] for arc in dependency_tree]  # 依存语法
    heads = ['Root' if id == 0 else words[id - 1] for id in rely_id]
    # 输出匹配单词的依存树
    for i in range(len(words)):
        print(relation[i] + '(' + words[i] + ', ' + heads[i] + ')')
    # 将依存树保存为jpg图片
    g = Digraph("Dependency_tree", format="jpg")
    # 节点定义
    g.node(name='Root', fontname="SimSun", shape='doublecircle')
    for word in words:
        g.node(name=word, fontname="SimSun", label=word.split("-")[0])
    # 设置图节点
    for i in range(len(words)):
        if relation[i] not in ['HED']:
            g.edge(heads[i], words[i], label=relation[i])
        else:
            if heads[i] == 'Root':
                g.edge('Root', words[i], label=relation[i])
            else:
                g.edge('Root', heads[i], label=relation[i])

    g.render(cleanup=True)


if __name__ == ("__main__"):
    sentence = "Can you make the phone a little bit cheaper?"
    de_line, word = dependency(sentence)
    Dependency_tree_visualization(de_line, word)
    print(de_line)
    print(word)