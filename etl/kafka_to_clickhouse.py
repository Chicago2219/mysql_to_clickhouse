
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.appName("KafkaToClickHouse").getOrCreate()

df = spark.read.format("kafka") \
                .option("subscribe", "dbserver1.bank.orders") \
                .option("kafka.bootstrap.servers", "localhost:9092") \
                .load()


df_parsed = df.selectExpr("CAST(value AS STRING)")

# Можно здесь добавить from_json + schema, фильтрацию и запись
df_parsed.write.format("jdbc") \
                .option("url", "jdbc:clickhouse://localhost:8123/default") \
                .option("dbtable", "orders_raw") \
                .option("user", "custom_user") \
                .option("password", "0000") \
                .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
                .save()

