from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("FraudDetection") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.2.0") \
    .getOrCreate()

# Define Schema
schema = StructType() \
    .add("transaction_id", StringType()) \
    .add("user_id", IntegerType()) \
    .add("amount", DoubleType()) \
    .add("timestamp", DoubleType()) \
    .add("location", StringType()) \
    .add("device", StringType()) \
    .add("status", StringType())

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "transactions") \
    .option("startingOffsets", "earliest") \
    .load()

# Convert Kafka value to JSON
df = df.selectExpr("CAST(value AS STRING)")
df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# Print Streaming Data
query = df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
