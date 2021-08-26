import tensorflow as tf
graph1 = tf.Graph()

with graph1.as_default():
    a = tf.constant([2], name = 'contant_a')
    b = tf.constant([3], name = 'contant_b')

#Printing the value of a
sess = tf.Session(graph = graph1)
result = sess.run(a)
sess.close()

with graph1.as_default():
    c = tf.add(a, b)

sess = tf.Session(graph = graph1)
result = sess.run(c)
print(result)
sess.close()