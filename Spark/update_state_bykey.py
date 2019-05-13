from pyspark import SparkContext
from pyspark.streaming import StreamingContext


# add the new values with the previous running count to get the new count
def updateFunc(new_values, prev_running_count):
    return sum(new_values) + (prev_running_count or 0)


# Create a local StreamingContext with as many working processors as possible and a batch interval of 10 seconds
batch_interval = 10

# We add this line to avoid an error : "Cannot run multiple SparkContexts at once". If there is an existing spark context, we will reuse it instead of creating a new context.
sc = SparkContext.getOrCreate()

# If there is no existing spark context, we now create a new context
if (sc is None):
    sc = SparkContext(master="local[*]", appName="WordCountApp")
ssc = StreamingContext(sc, batch_interval)

# streaming application must run 24 hours a day. Thus, it needs to be resilient to failures caused by some unexpected errors such as system failures, driver failure, JVM crashes, etc. Checkpointing saves the generated RDDs to a reliable storate and performs receovery from an error.
#To summarise, checkpoints provide a way of recovering to a safe stable application snapshot.
# Using the ssc.checkpoint() method, we can tell the Spark engine where to store the checkpoint files.
ssc.checkpoint("checkpoint")

host = "localhost"
port = 9999

lines = ssc.socketTextStream(host, int(port))

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.updateStateByKey(updateFunc)

# Print the result
wordCounts.pprint()

ssc.start()
try:
    ssc.awaitTermination(timeout=60)
except KeyboardInterrupt:
    ssc.stop()
    sc.stop()

ssc.stop()
sc.stop()