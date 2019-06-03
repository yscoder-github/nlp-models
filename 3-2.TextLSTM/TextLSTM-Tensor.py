"""
code by yinshuai
#### 3. RNN(Recurrent Neural Network) -- Many To One Generation network

- 3-2. [TextLSTM](https://github.com/graykode/nlp-tutorial/tree/master/3-2.TextLSTM) - **Autocomplete**
  - Paper - [LONG SHORT-TERM MEMORY(1997)](https://www.bioinf.jku.at/publications/older/2604.pdf)
  - Colab - [TextLSTM_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-2.TextLSTM/TextLSTM_Tensor.ipynb), [TextLSTM_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/3-2.TextLSTM/TextLSTM_Torch.ipynb)


要注意 char-RNN
      char-LSTM(with or without attention)
      char-DNN


      泛化到各种类型的字符级别的序列模型,其训练样本示例如下:
        例如当前输入的单词为beijing

        input             target
        b<padxxx>          e
        be                 i
        bei                j
        beij               i
        beiji              n
        beijin             g

"""
import numpy as np
import tensorflow as tf

tf.reset_default_graph()

char_arr = [c for c in 'abcdefghijklmnopqrstuvwxyz']
word_dict = {n: i for i, n in enumerate(char_arr)}
number_dict = {i: w for i, w in enumerate(char_arr)}
n_class = len(word_dict)  # number of class(=number of vocab)  26 here

seq_data = ['make', 'need', 'coal', 'word', 'love', 'hate', 'live', 'home', 'hash', 'star']

# TextLSTM Parameters
n_step = 3
n_hidden = 128


def make_batch(seq_data):
    """
    @author: yinshuai make one-hot train-data batch
    :param seq_data:
    :return:
    """
    input_batch, target_batch = [], []

    for seq in seq_data:
        input = [word_dict[n] for n in seq[:-1]]  # 'm', 'a' , 'k' is input  (truncate the first three alpha)
        target = word_dict[seq[-1]]  # 'e' is target (the last alpha of the word is the target
        input_batch.append(np.eye(n_class)[input])
        target_batch.append(np.eye(n_class)[target])

    return input_batch, target_batch


# Model
X = tf.placeholder(tf.float32, [None, n_step, n_class])  # [batch_size, n_step, n_class]
Y = tf.placeholder(tf.float32, [None, n_class])  # [batch_size, n_class]

# for output, means Y
W = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

cell = tf.nn.rnn_cell.BasicLSTMCell(n_hidden)
outputs, states = tf.nn.dynamic_rnn(cell, X, dtype=tf.float32)  # dynamic rnn will  unroll automatic when execute

# outputs : [batch_size, n_step, n_hidden]
outputs = tf.transpose(outputs, [1, 0, 2])  # [n_step, batch_size, n_hidden]
outputs = outputs[-1]  # [batch_size, n_hidden]
model = tf.matmul(outputs, W) + b  # model : [batch_size, n_class]

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)

prediction = tf.cast(tf.argmax(model, 1), tf.int32)

# Training
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

input_batch, target_batch = make_batch(seq_data)

for epoch in range(1000):
    _, loss = sess.run([optimizer, cost], feed_dict={X: input_batch, Y: target_batch})
    if (epoch + 1) % 100 == 0:
        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(loss))

inputs = [sen[:3] for sen in seq_data]

predict = sess.run([prediction], feed_dict={X: input_batch})
print(inputs, '->', [number_dict[n] for n in predict[0]])