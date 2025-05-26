
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("KafkaToClickHouse")     .getOrCreate()

df = spark.read     .format("kafka")     .option("subscribe", "dbserver1.bank.orders")     .option("kafka.bootstrap.servers", "localhost:9092")     .load()

from pyspark.sql.functions import col
df_parsed = df.selectExpr("CAST(value AS STRING)")

# Можно здесь добавить from_json + schema, фильтрацию и запись
df_parsed.write     .format("jdbc")     .option("url", "jdbc:clickhouse://localhost:8123")     .option("dbtable", "orders_raw")     .option("user", "default")     .save()
