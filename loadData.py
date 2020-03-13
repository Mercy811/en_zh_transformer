import torch
from torchtext import data, datasets, vocab
import os

dataDir = '/Users/xinyi.ye/Documents/machine_translate/experiments/train4/'

BOS_WORD = '<s>'
EOS_WORD = '</s>'
BLANK_WORD = "<blank>"

# Field define how to deal with raw data
SRC = data.Field(pad_token=BLANK_WORD) # tokenize, default: string.split
TGT = data.Field(init_token = BOS_WORD,eos_token = EOS_WORD, pad_token=BLANK_WORD)

traindataset = datasets.TranslationDataset(path=dataDir+'train-infoq', exts=('.en','.zh'),fields=(SRC, TGT))

pwd = os.getcwd()

SRC.build_vocab(traindataset, vectors=vocab.Vectors(name='cc.en.300.vec', cache=pwd+'/.vector_cache'))
TGT.build_vocab(traindataset, vectors=vocab.Vectors(name='cc.zh.300.vec', cache=pwd+'/.vector_cache'))

print(SRC.vocab.stoi)
print(TGT.vocab.stoi)