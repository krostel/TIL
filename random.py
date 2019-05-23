
from pyspark import SparkContext, SQLContext
from pyspark.sql import Row
from pyspark.sql.functions import col, size, udf, when, array

sc = SparkContext.getOrCreate()
sqc = SQLContext.getOrCreate(sc)


# When configuring a new Spark installation, sometimes we can run on errors like this:
# `java.io.IOException: No FileSystem for scheme: s3n`
# (or s3, or s3a... the exact protocol does not matter)

# If this happens, it is most likely because there are dependencies missing from the Spark distribution, so installing them should fix the problem (a handy way is just to drop the missing JARs into the `<spark_installation>/jars/` folder)  

# At the time of writing this, in Spark 2.2.0 with Hadoop 2.7 the are two libraries missing:
# *  aws-java-sdk-XXXX    (1.11.207 seems to work fine)
# *  hadoop-aws-XXXX     (2.8.1 seems to work fine)

# More info here (don't look at the specific versions of the libraries, they are outdated already):

# https://sparkour.urizone.net/recipes/using-s3/
@contextmanager
def cached(rdd):
    """used with a 'with" will make sure that rdds are unpersisted when done
    Args:
        rdd: to cache

    Returns:
        rdd

    """
    rdd.cache()
    yield rdd
    rdd.unpersist()
