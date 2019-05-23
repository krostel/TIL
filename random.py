
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
def print_skew(rdd):
    """Prints out the index and the number of elements in the largest and smallest partitions of an RDD

    Args:
        rdd (RDD):
    """
    skew = rdd.mapPartitionsWithIndex(lambda ind, x: (ind, itertoolz.count(x))).collect()
    by_size = sorted(skew, key=operator.itemgetter(1))
    print("Largest partition (index, size)")
    print(by_size[-1])
    print("Smallest partition (index, size)")
    print(by_size[0])
def is_date_in_cron_schedule(schedule, date):
    """Returns a bool as to whether the crontab schedule for a step matches the provided date.

    croniter expects full crontab like schedules:
        * * 2 1 2 => minute hour day(month) month day(week)
    Steps in our pipeline do not need to run > 1 a day, so the minute and hour values will always be ignored but are expected
    Schedules that are None are automatically considered valid as we assume that something without a schedule should
    be run all of the time.

    Args:
        schedule (str): Job config from pipeline_config.yaml
        date (datetime.date):
    Returns:
        bool
    """
    # import is here because it can cause issue with PySpark
    from croniter import croniter

    datetime_ = datetime.datetime.combine(date, datetime.datetime.min.time())

    if schedule is not None:
        try:
            seconds_to_next_run = croniter(schedule, datetime_).get_next()

            next_valid_run_date = datetime.datetime.fromtimestamp(seconds_to_next_run)
            if next_valid_run_date.date() == date:
                return True
            else:
                return False
        except:
            ValueError("Could not parse schedule {}".format(schedule))
    else:
        return True
