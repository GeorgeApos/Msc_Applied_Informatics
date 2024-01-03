from pyspark.sql import SparkSession
from pyspark.sql.functions import col

from first_assignment import execute_first_assignment
from second_assignment import execute_second_assignment

if __name__ == '__main__':
    spark = SparkSession.builder.appName("VolleyballProcessing").getOrCreate()

    file_path = "volleyball.csv"
    volleyball_data = spark.read.option("header", "true").csv(file_path)

    execute_first_assignment(volleyball_data)
    execute_second_assignment(volleyball_data)

    spark.stop()
