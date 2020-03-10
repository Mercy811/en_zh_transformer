### file introduction

[data.py](data.py): preprocess datasets including loading, embedding, padding, and batch

[model.py](model.py): implementation of Transformer 

[train.py](train.py): several training methods

[loadData.ipynb](loadData.ipynb): use torchtext to load dataset from disk, numericalize words, generate voacb, and batch them

---

### training example

[characterCopy.py](characterCopy.py): a simple copying experiment to test model 

[IWSLTGeEnTranslation.py](IWSLTGeEnTranslation.py): IWSLTG Ge-En experiment


---

### Chinese word embedding

Although there are several pretrained word embeddings, the segmentation methods can hugely affect the performance of embedding and downstream tasks. 

| Name                                 | Format             | Algorithm   | Dimension |
|--------------------------------------|--------------------|-------------|-----------|
| [Tencent AI Lab Embedding Corpus for Chinese Words and Phrases](https://ai.tencent.com/ailab/nlp/embedding.html) | text (.txt) | DSG (directional skip-gram) | 200 |
| [fastText](https://fasttext.cc/docs/en/crawl-vectors.html) | text (.txt) & binary (.bin) | skip-gram <br>(n=5, window=5, negative=10) | 300 |
| [Wikipedia2Vec](https://wikipedia2vec.github.io/wikipedia2vec/pretrained/#chinese) | text (.txt) & binary (.bin) | skip-gram<br>(window=5, iteration=10, negative=15) | 100 & 300 |