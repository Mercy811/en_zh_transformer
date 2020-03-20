## File Introduction


[data.py](data.py): preprocess datasets including loading, embedding, padding, and batch

[model.py](model.py): implementation of Transformer 

[train.py](train.py): several training methods

[loadData.ipynb](loadData.ipynb): use torchtext to load dataset from disk, numericalize words, generate voacb, and batch them


## Training Example

[characterCopy.py](characterCopy.py): a simple copying experiment to test model 

[IWSLTGeEnTranslation.py](IWSLTGeEnTranslation.py): IWSLTG Ge-En experiment


## Pretrained Chinese Word Embedding

Although there are several pretrained word embeddings, the segmentation methods can hugely affect the performance of embedding and downstream tasks. 

| Name                                 | Format             | Algorithm   | Dimension |
|--------------------------------------|--------------------|-------------|-----------|
| [Tencent AI Lab Embedding Corpus for Chinese Words and Phrases](https://ai.tencent.com/ailab/nlp/embedding.html) | text (.txt) | DSG (directional skip-gram) | 200 |
| [fastText](https://fasttext.cc/docs/en/crawl-vectors.html) | text (.txt) & binary (.bin) | CBOW <br>(n=5, window=5, negative=10) | 300 |
| [Wikipedia2Vec](https://wikipedia2vec.github.io/wikipedia2vec/pretrained/#chinese) | text (.txt) & binary (.bin) | skip-gram<br>word-based<br>(window=5, iteration=10, negative=15) | 100 & 300 |


fastText uses [Stanford Word Segmenter](https://nlp.stanford.edu/software/segmenter.html) for Chinese, the same toolkit I used to tokenize infoq corpus. Also fastText provides a easy to use tool (both skip-gram and CBOW are available) to generate your own embedding.




## Web Development

[Machine Translation Web Interface for OpenNMT](https://blog.machinetranslation.io/opennmt-web-interface/)

First start server: 

> cd website

> /bin/bash start_server.sh path/to/OpenNMT-tf

Then start this website 

