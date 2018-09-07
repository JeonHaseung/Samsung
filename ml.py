import tensorflow as tf
import sqlite3 as lite
import numpy as np
tf.set_random_seed(777)  # for reproducibility

"""
currentPrice, Amount, totalAmout, Time, DifferncePrice, is_up
currentPrice, Amount, totalAmout, Time,  DifferncePrice, WaitingBuy, WaitingSell, is_up
"""


database_filename = 'test.db'
conn = lite.connect(database_filename)
cs = conn.cursor()

coinoneQuery = "SELECT {} from tb_coinone where whichCoin='{}'"
bithumbQuery = "SELECT {} from tb_bithumb where whichCoin='{}'"

coinoneList = [
    "ltc",
    "bch",
    "zrx",
    "qtum",
    "knc",
    "eos",
    "etc",
    "btg",
    "btc",
    "omg",
    "eth",
    "zil",
    "xrp"
]

bithumbList = [
    "LTC",
    "BCH",
    "ZRX",
    "QTUM",
    "KNC",
    "EOS",
    "ETC",
    "BTG",
    "BTC",
    "OMG",
    "ETH",
    "ZIL",
    "XRP"
]

coinone_c = ["currentPrice", "Amount", "totalAmout", "DifferncePrice"]
bithumb_c = ["currentPrice", "Amount", "totalAmout", "DifferncePrice", "WaitingBuy", "WaitingSell"]

coinone_x = []
coinone_y = []
bithumb_x = [[], [], [], [], [], []]
bithumb_y = [[]]

for coin in coinoneList:
    query = coinoneQuery.format("currentPrice, Amount, totalAmout, DifferncePrice", coin)
    cs.execute(query)
    x = cs.fetchall()
    for i in x:
        coinone_x.append(list(i))
    #coinone_x = x
    query = coinoneQuery.format("is_up", coin)
    cs.execute(query)
    y = cs.fetchall()
    k= []
    for a in y:
        if a[0] > 0:
            k.append([1])
        else:
            k.append([0])
    coinone_y = k
    

    x_data = coinone_x
    y_data = coinone_y


    # placeholders for a tensor that will be always fed.
    X = tf.placeholder(tf.float32, shape=[None, 4])
    Y = tf.placeholder(tf.float32, shape=[None, 1])

    W = tf.Variable(tf.random_normal([4, 1]), name='weight')
    b = tf.Variable(tf.random_normal([1]), name='bias')

    # Hypothesis using sigmoid: tf.div(1., 1. + tf.exp(-tf.matmul(X, W)))
    hypothesis = tf.sigmoid(tf.matmul(X, W) + b)

    # cost/loss function
    cost = -tf.reduce_mean(Y * tf.log(hypothesis) + (1 - Y) *
                           tf.log(1 - hypothesis))

    train = tf.train.GradientDescentOptimizer(learning_rate=0.01).minimize(cost)

    # Accuracy computation
    # True if hypothesis>0.5 else False
    predicted = tf.cast(hypothesis > 0.5, dtype=tf.float32)
    accuracy = tf.reduce_mean(tf.cast(tf.equal(predicted, Y), dtype=tf.float32))

    # Launch graph
    with tf.Session() as sess:
        # Initialize TensorFlow variables
        sess.run(tf.global_variables_initializer())

        for step in range(10001):
            cost_val, _ = sess.run([cost, train], feed_dict={X: x_data, Y: y_data})
            if step % 200 == 0:
                print(step, cost_val)

        # Accuracy report
        h, c, a = sess.run([hypothesis, predicted, accuracy],
                           feed_dict={X: x_data, Y: y_data})
        print("\nHypothesis: ", h, "\nCorrect (Y): ", c, "\nAccuracy: ", a)

