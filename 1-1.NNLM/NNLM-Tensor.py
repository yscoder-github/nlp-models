"""
code by yinshaui
#### 1. Basic Embedding Model
- 1-1. [NNLM(Neural Network Language Model)](https://github.com/graykode/nlp-tutorial/tree/master/1-1.NNLM) - **Predict Next Word**
  - Paper -  [A Neural Probabilistic Language Model(2003)](http://www.jmlr.org/papers/volume3/bengio03a/bengio03a.pdf)
  - Colab - [NNLM_Tensor.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-1.NNLM/NNLM_Tensor.ipynb), [NNLM_Torch.ipynb](https://colab.research.google.com/github/graykode/nlp-tutorial/blob/master/1-1.NNLM/NNLM_Torch.ipynb)
# # tranning embedding wordvector, the size of the embedding is 2
"""

import numpy as np
import tensorflow as tf

tf.reset_default_graph()

sentences = ["i like dog", "i love coffee", "i hate milk"]

word_list = " ".join(sentences).split()
word_list = list(set(word_list))
word_dict = {w: i for i, w in enumerate(word_list)}  # word: index
number_dict = {i: w for i, w in enumerate(word_list)} # index: word
n_class = len(word_dict)  # number of Vocabulary

# NNLM Parameter
n_step = 2  # number of steps ['i like', 'i love', 'i hate']
n_hidden = 2  # number of hidden units


def make_batch(sentences):
    """
    create batch data from sentences (list)
    """
    input_batch = []
    target_batch = []

    for sen in sentences:
        word = sen.split()
        input = [word_dict[n] for n in word[:-1]]  # word_dict is word: index
        print(input)
        target = word_dict[word[-1]]

        input_batch.append(np.eye(n_class)[input]) # one-hot
        target_batch.append(np.eye(n_class)[target])# one -hot

    return input_batch, target_batch



# Model -- the input is one-hot
X = tf.placeholder(tf.float32, [None, n_step, n_class])  # [batch_size, number of steps, number of Vocabulary]
Y = tf.placeholder(tf.float32, [None, n_class])

input = tf.reshape(X, shape=[-1, n_step * n_class])  # [batch_size, n_step * n_class]
H = tf.Variable(tf.random_normal([n_step * n_class, n_hidden]))
d = tf.Variable(tf.random_normal([n_hidden]))
U = tf.Variable(tf.random_normal([n_hidden, n_class]))
b = tf.Variable(tf.random_normal([n_class]))

tanh = tf.nn.tanh(d + tf.matmul(input, H))  # [batch_size, n_hidden]  # tanh is the  hidden status of the current cell
model = tf.matmul(tanh, U) + b  # [batch_size, n_class] # model is the output of the current cell

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=model, labels=Y))
optimizer = tf.train.AdamOptimizer(0.001).minimize(cost)
prediction = tf.argmax(model, 1)

# Training
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
        
input_batch, target_batch = make_batch(sentences)

print(input_batch)

for epoch in range(5000):
    _, loss = sess.run([optimizer, cost], feed_dict={X: input_batch, Y: target_batch})
    if (epoch + 1) % 1000 == 0:
        print('Epoch:', '%04d' % (epoch + 1), 'cost =', '{:.6f}'.format(loss))

# Predict
predict = sess.run([prediction], feed_dict={X: input_batch})

# Test
input = [sen.split()[:2] for sen in sentences]
print([sen.split()[:2] for sen in sentences], '->', [number_dict[n] for n in predict[0]])



# write graph to file for show 
logs_path = "/tmp/tensorflow_logs/1-1-graph"
summary_writer = tf.summary.FileWriter(
        logs_path, graph=tf.get_default_graph())


print("Run the command line:\n"
        "--> tensorboard --logdir=/tmp/tensorflow_logs/1-1"
        "\nThen open http://0.0.0.0:6006/ into your web browser")



