from pyspark.sql import SparSession
from pyspark.sql import functions as F
from pyspark.sql.types import FloatType

spark = SparSession \
    .builder \
    .appName("Name it here") \
    .getOrCreate()


def to_value(v): return float(v.replace(",", "."))


udf_to_value = F.udf(to_value, FloatType())

df = spark.read.csv("file.csv", header=True)

df2 = df.withColumn("New Column Name", udf_to_value(df["Column Name"])) \
    .withColumn("Another New Column Name", F.to_date(df["Another Column Name"], format="dd/MM/yy"))

df3 = df2.select(df2["Column Name"].alias("Rename Column"),
                 df2["Column Name"].alias("Rename Column"),
                 df2["Column Name"].alias("Rename Column"),
                 df2["Column Name"])

df3.write.parquet("folder/name/yy/mm/dd")
