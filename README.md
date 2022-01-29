# Oracle_code

## 环境配置

参考教程：https://www.jianshu.com/p/002157665bfd

### 1 Stanford NLP下载
下载链接：https://nlp.stanford.edu/software/stanford-corenlp-latest.zip

解压

如果链接打不开，从官网直接下载：https://stanfordnlp.github.io/CoreNLP/

### 2 jdk下载
测试是否已安装，在命令行输入命令“java -version”,显示jdk版本，>1.8都可。
若未下载，官网：https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html


### 3 python包安装
`pip install stanfordcorenlp -i http://pypi.mirrors.ustc.edu.cn/simple/ --trusted-host pypi.mirrors.ustc.edu.cn`

### 4 把 stanfordDependency.py 和 stanfordParser.py 中的nlp路径改为第一步解压后的文件夹路径

## 文件说明

### stanfordDependency.py
依赖句法分析

### stanfordParser.py
短语句法分析
