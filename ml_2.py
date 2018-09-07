import tensorflow as tf
import sqlite3 as lite

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

coinone_x = [[], [], [], []]
coinone_y = [[]]
bithumb_x = [[], [], [], [], [], []]
bithumb_y = [[]]

for coin in coinoneList:
    num = 0
    for column in coinone_c:
        query = coinoneQuery.format(column, coin)
        cs.execute(query)
        x = cs.fetchall()
        k = []
        for a in x:
            k.append(a[0])
        coinone_x[num] = k
        num += 1
    query = coinoneQuery.format("is_up", coin)
    cs.execute(query)
    y = cs.fetchall()
    coinone_y[0] = y
    
    x1 = tf.placeholder(tf.float32)
    x2 = tf.placeholder(tf.float32)
    x3 = tf.placeholder(tf.float32)
    #x4 = tf.placeholder(tf.float32)
    
    Y = tf.placeholder(tf.float32)
    
    w1 = tf.Variable(tf.random_normal([1]), name='weight1')
    w2 = tf.Variable(tf.random_normal([1]), name='weight2')
    w3 = tf.Variable(tf.random_normal([1]), name='weight3')
    #w4 = tf.Variable(tf.random_normal([1]), name='weight4')
    b = tf.Variable(tf.random_normal([1]), name='bias')
    
    #hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + x4 * w4 + b
    hypothesis = x1 * w1 + x2 * w2 + x3 * w3 + b
    print(hypothesis)
    
    # cost/loss function
    cost = tf.reduce_mean(tf.square(hypothesis - Y))
    
    # Minimize. Need a very small learning rate for this data set
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1e-5)
    train = optimizer.minimize(cost)
    
    
    # Launch the graph in a session.
    sess = tf.Session()
    # Initializes global variables in the graph.
    sess.run(tf.global_variables_initializer())
    
    while(1):
        #print(coinone_x[1])
        #print(coinone_x[2])
        #print(coinone_y[0])
        #ost_val, hy_val, _ , w1_val, w2_val, w3_val, w4_val = sess.run([cost, hypothesis, train, w1, w2, w3, w4],
         #                         feed_dict={x1: coinone_x[0], x2: coinone_x[1], x3: coinone_x[2], x4: coinone_x[3], Y: coinone_y[0]})
        cost_val, hy_val, _ , w1_val, w2_val, w3_val = sess.run([cost, hypothesis, train, w1, w2, w3],
                                   feed_dict={x1: coinone_x[1], x2: coinone_x[2], x3: coinone_x[3], Y: coinone_x[0]})

                                   #if cost_val < 10000:
        #print(coin, "Cost: ", cost_val, "\nPrediction:\n", hy_val, "w1 : ", w1_val, "w2 : ", w2_val, "w3 : ", w3_val, "w4 : ", w4_val, "\n")
        print(coin, "Cost: ", cost_val, "\nPrediction:\n", hy_val, "w1 : ", w1_val, "w2 : ", w2_val, "w3 : ", w3_val, "\n")
        #    break
        
