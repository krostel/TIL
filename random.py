
from pyspark import SparkContext, SQLContext
from pyspark.sql import Row
from pyspark.sql.functions import col, size, udf, when, array

sc = SparkContext.getOrCreate()
sqc = SQLContext.getOrCreate(sc)


