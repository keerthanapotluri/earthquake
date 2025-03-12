from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("EarthquakeData").getOrCreate()

storage_account_name = "projectazurekp450"
container_name = "earthquakedata"
file_name = "earthquake_data.csv"

storage_account_key = ""
spark.conf.set(f"fs.azure.account.key.{storage_account_name}.blob.core.windows.net", storage_account_key)

file_path = f"wasbs://{container_name}@{storage_account_name}.blob.core.windows.net/{file_name}"

df = spark.read.option("header", True).csv(file_path)

df.show(5)

df.write.format("parquet").mode("overwrite").save("dbfs:/mnt/earthquake-data-parquet")

print("✅ Data successfully loaded into Databricks and saved as Parquet!")
