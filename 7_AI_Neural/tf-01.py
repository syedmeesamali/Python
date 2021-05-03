# import tensorflow.compat.v1 as tf
# in_a = tf.placeholder(dtype = tf.float32, shape=(2))
# def model(x):
#     with tf.variable_scope("matmul"):
#         w = tf.get_variable("w", initializer = tf.ones(shape = (2,2)))
#         b = tf.get_variable("b", initializer = tf.ones(shape = (2)))
#         return x * w + b
# out_a = model(in_a)
# with tf.Session() as sess:
#     sess.run(tf.global_variables_initializer())
#     outs = sess.run([out_a], feed_dict = {in_a: [1, 0]})
import tensorflow as tf

w = tf.Variable(tf.ones(shape=(2,2)), name = "w")
b = tf.Variable(tf.ones(shape=(2,2)), name = "b")
@tf.function

def model(x):
    return w * x + b
out_a = model([1, 0])
print(out_a)
