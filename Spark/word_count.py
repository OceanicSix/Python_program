import sys

from pyspark import SparkContext
from pyspark.streaming import StreamingContext

# We add this line to avoid an error : "Cannot run multiple SparkContexts at once".
# If there is an existing spark context, we will reuse it instead of creating a new context.
sc = SparkContext.getOrCreate()

# Create a local StreamingContext with as many working processors as possible
# and a batch interval of 10 seconds
batch_interval = 10

# If there is no existing spark context, we now create a new context
if (sc is None):
    sc = SparkContext(master="local[*]", appName = "WordCountApp")
ssc = StreamingContext(sc, batch_interval)

host = "localhost"
port = 9999

lines = ssc.socketTextStream(host, int(port))

# Split each line into words
words = lines.flatMap(lambda line: line.split(" "))

# Count each word in each batch
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)

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