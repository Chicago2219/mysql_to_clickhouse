from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


spark = SparkSession.builder \
    .appName("KafkaToClickhouse") \
    .getOrCreate()

schema = StructType([
    StructField("id", IntegerType()),
    StructField("name", StringType()),
    StructField("email", StringType())
])

df_raw = spark.read.format("kafka") \
    .option("kafka.bootstrap.servers", "host.docker.internal:9092") \
    .option("subscribe", "dbserver1.bank.customers") \
    .load()

df_json = df_raw.selectExpr("CAST(value AS STRING) as json_str") \
    .select(from_json(col("json_str"), StructType([
        StructField("payload", StructType([
            StructField("id", IntegerType()),
            StructField("name", StringType()),
            StructField("email", StringType())
        ]))
    ])).alias("data"))


df_final = df_json.select("data.payload.*")


df_final.write \
    .format("jdbc") \
    .option("driver", "com.clickhouse.jdbc.ClickHouseDriver") \
    .option("url", "jdbc:clickhouse://localhost:8123/default") \
    .option("dbtable", "kafka_data") \
    .option("user", "custom_user") \
    .option("password", "0000") \
    .option("createTableOptions", "ENGINE = MergeTree ORDER BY id") \
    .mode("overwrite") \
    .save()
