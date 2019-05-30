## nlp-models 
<p align="center">
<img width="100" src="https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1559145755227&di=eac73643be2de89cc8d0b8d03e79c4f2&imgtype=0&src=http%3A%2F%2Fimg.91jm.com%2F2016%2F08%2F1565A358901.jpg" />
<img width="100" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/TensorFlowLogo.svg/225px-TensorFlowLogo.svg.png" />  <img width="100" src="https://avatars1.githubusercontent.com/u/26200681?s=400&u=678028f046e903873ea38f04d23a397dc0d475d8&v=4" /></p>


This [nlp-models](https://github.com/yscoder-github/nlp-models) project  is modified on existing repositorie [nlp-tutorial](https://github.com/graykode/nlp-tutorial), which is a tutorial for who is studying NLP(Natural Language Processing) using **TensorFlow** , **Pytorch** and **keras** ,Most of the models in NLP were implemented with less than **100 lines** of code.(except comments or blank lines)base on this repositorie. 

To do: 
1. Add some new  model 

2. Add keras version 

3. Adding more English annotations

4. Enriching training examples

5. Adding larger data sets to measure model effectiveness




## Curriculum - (Example Purpose)

#### 1. Basic Embedding Model

- 1-1. [NNLM(Neural Network Language Model)](https://github.com/graykode/nlp-tutorial/tree/master/1-1.NNLM) - **Predict Next Word**
  - Paper -  [A Neural Probabilistic Language Model(2003)](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
  - Colab - [NNLM_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-1.NNLM/NNLM_Tensor.ipynb), [NNLM_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-1.NNLM/NNLM_Torch.ipynb)
- 1-2. [Word2Vec(Skip-gram)](https://github.com/graykode/nlp-tutorial/tree/master/1-2.Word2Vec) - **Embedding Words and Show Graph**
  - Paper - [Distributed Representations of Words and Phrases
    and their Compositionality(2013)](https://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf)
  - Colab - [Word2Vec_Tensor(NCE_loss).ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-2.Word2Vec/Word2Vec_Tensor(NCE_loss).ipynb), [Word2Vec_Tensor(Softmax).ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-2.Word2Vec/Word2Vec_Tensor(Softmax).ipynb), [Word2Vec_Torch(Softmax).ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-2.Word2Vec/Word2Vec_Torch(Softmax).ipynb)
- 1-3. [FastText(Application Level)](https://github.com/graykode/nlp-tutorial/tree/master/1-3.FastText) - **Sentence Classification**
  - Paper - [Bag of Tricks for Efficient Text Classification(2016)](https://arxiv.org/pdf/1607.01759.pdf)
  - Colab - [FastText.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-3.FastText/FastText.ipynb)



#### 2. CNN(Convolutional Neural Network)

- 2-1. [TextCNN](https://github.com/graykode/nlp-tutorial/tree/master/2-1.TextCNN) - **Binary Sentiment Classification**
  - Paper - [Convolutional Neural Networks for Sentence Classification(2014)](http://www.aclweb.org/anthology/D14-1181)
  - Colab - [TextCNN_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/2-1.TextCNN/TextCNN_Tensor.ipynb), [TextCNN_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/2-1.TextCNN/TextCNN_Torch.ipynb)
- 2-2. DCNN(Dynamic Convolutional Neural Network)



#### 3. RNN(Recurrent Neural Network)

- 3-1. [TextRNN](https://github.com/graykode/nlp-tutorial/tree/master/3-1.TextRNN) - **Predict Next Step**
  - Paper - [Finding Structure in Time(1990)](http://psych.colorado.edu/~kimlab/Elman1990.pdf)
  - Colab - [TextRNN_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-1.TextRNN/TextRNN_Tensor.ipynb), [TextRNN_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-1.TextRNN/TextRNN_Torch.ipynb)
- 3-2. [TextLSTM](https://github.com/graykode/nlp-tutorial/tree/master/3-2.TextLSTM) - **Autocomplete**
  - Paper - [LONG SHORT-TERM MEMORY(1997)](https://www.bioinf.jku.at/publications/older/2604.pdf)
  - Colab - [TextLSTM_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-2.TextLSTM/TextLSTM_Tensor.ipynb), [TextLSTM_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-2.TextLSTM/TextLSTM_Torch.ipynb)
- 3-3. [Bi-LSTM](https://github.com/graykode/nlp-tutorial/tree/master/3-3.Bi-LSTM) - **Predict Next Word in Long Sentence**
  - Colab - [Bi_LSTM_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-3.Bi-LSTM/Bi_LSTM_Tensor.ipynb), [Bi_LSTM_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-3.Bi-LSTM/Bi_LSTM_Torch.ipynb)



#### 4. Attention Mechanism

- 4-1. [Seq2Seq](https://github.com/graykode/nlp-tutorial/tree/master/4-1.Seq2Seq) - **Change Word**
  - Paper - [Learning Phrase Representations using RNN Encoder–Decoder
    for Statistical Machine Translation(2014)](https://arxiv.org/pdf/1406.1078.pdf)
  - Colab - [Seq2Seq_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-1.Seq2Seq/Seq2Seq_Tensor.ipynb), [Seq2Seq_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-1.Seq2Seq/Seq2Seq_Torch.ipynb)
- 4-2. [Seq2Seq with Attention](https://github.com/graykode/nlp-tutorial/tree/master/4-2.Seq2Seq(Attention)) - **Translate**
  - Paper - [Neural Machine Translation by Jointly Learning to Align and Translate(2014)](https://arxiv.org/abs/1409.0473)
  - Colab - [Seq2Seq(Attention)_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-2.Seq2Seq(Attention)/Seq2Seq(Attention)_Tensor.ipynb), [Seq2Seq(Attention)_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-2.Seq2Seq(Attention)/Seq2Seq(Attention)_Torch.ipynb)
- 4-3. [Bi-LSTM with Attention](https://github.com/graykode/nlp-tutorial/tree/master/4-3.Bi-LSTM(Attention)) - **Binary Sentiment Classification**
  - Colab - [Bi_LSTM(Attention)_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-3.Bi-LSTM(Attention)/Bi_LSTM(Attention)_Tensor.ipynb), [Bi_LSTM(Attention)_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/4-3.Bi-LSTM(Attention)/Bi_LSTM(Attention)_Torch.ipynb)



#### 5. Model based on Transformer

- 5-1.  [The Transformer](https://github.com/graykode/nlp-tutorial/tree/master/5-1.Transformer) - **Translate**
  - Paper - [Attention Is All You Need(2017)](https://arxiv.org/abs/1810.04805)
  - Colab - [Transformer_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/5-1.Transformer/Transformer_Torch.ipynb), [Transformer(Greedy_decoder)_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/5-1.Transformer/Transformer(Greedy_decoder)_Torch.ipynb)
- 5-2. [BERT](https://github.com/graykode/nlp-tutorial/tree/master/5-2.BERT) - **Classification Next Sentence & Predict Masked Tokens**
  - Paper - [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding(2018)](https://arxiv.org/abs/1810.04805)
  - Colab - [BERT_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/5-2.BERT/BERT_Torch.ipynb)




## Dependencies

- Python 3.5+
- Tensorflow 1.12.0+
- Pytorch 0.4.1+
- Plan to add Keras Version   **TO DO**  



## Author

- yinshuai 
- Author Email : yscoder@foxmail.com 
- Acknowledgements to my colleagues and friends
