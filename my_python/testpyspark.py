from pyspark.sql import SparkSession, SQLContext
from pyspark.sql.types import *
from pyspark.sql import functions as F

spark = SparkSession.builder.appName('company').getOrCreate()
sqlContext = SQLContext(spark)
data = sqlContext.createDataFrame([(1.449015065E9, 1.449015065E9), (0.0,1.449015065E9),(1.449015065E9,0.0),(0.0,0.0)],
                                  ["modified", "created"])
data.show()
data.printSchema()

test_df = data.select(data.modified).show()

test_df = data.select(data.created).show()

data = [1, 2, 3, 4, 5]
distData = spark.parallelize(data)


distFile = spark.textFile("data.txt")