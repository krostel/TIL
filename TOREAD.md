# practice
### Bookmarks

[How to add a constant column in a Spark DataFrame?](https://stackoverflow.com/questions/32788322/how-to-add-a-constant-column-in-a-spark-dataframe)

[apachesparkoptimization](http://airisdata.com/apachesparkoptimization/)

[Distribution of Executors, Cores and Memory for a Spark Application running in Yarn:](https://spoddutur.github.io/spark-notes/distribution_of_executors_cores_and_memory_for_spark_application.html)

[Insights into the troubles of using filesystem (S3/HDFS) as data source in spark…](https://spoddutur.github.io/spark-notes/s3-filesystem-as-datasource-in-spark)

[AWS CloudWatch Monitoring with Grafana](https://hackernoon.com/aws-cloudwatch-monitoring-with-grafana-ace63e1ab507)

[https://coolbackgrounds.io/](https://coolbackgrounds.io/)
[SQL Server Query to Tableau Data Extract LIKE A BOSS – Some more TDE API fun with Python & Tableau 8](http://ryrobes.com/python/sql-server-query-to-tableau-data-extract-more-tde-api-fun-with-python-tableau-8/)

[Functional scala examples?](https://github.com/hablapps/gist/blob/master/src/test/scala/ChurchEncodings.scala)

[What is the standard Python docstring format?](https://stackoverflow.com/questions/3898572/what-is-the-standard-python-docstring-format)

[PEP 3113 -- Removal of Tuple Parameter Unpacking](https://www.python.org/dev/peps/pep-3113/)
[Example Google Style Python Docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)
[Visualizing Algorithms](https://bost.ocks.org/mike/algorithms/)
[Rear Double Underscore (Name Mangling)/ From the Python Docs](https://stackoverflow.com/questions/8689964/why-do-some-functions-have-underscores-before-and-after-the-function-name)
[Bash Brackets Mindset](https://stackoverflow.com/questions/13617843/unary-operator-expected)
[https://docs.pytest.org/en/latest/fixture.html](https://docs.pytest.org/en/latest/fixture.html)
[]()
[]()
[]()

[random open spark server](http://gw03.itversity.com:18080/)

### Scrap TODO

The Imposter's Handbook
The Professional Chef by the Culinary Institute of America
The Flavor Bible by Karen Page and Andrew Dornenburg


 https://www.amazon.co.uk/How-Talk-Anyone-Success-Relationships/dp/0722538073/ref=pd_sim_14_2?_encoding=UTF8&pd_rd_i=0722538073&pd_rd_r=03db6c05-f7ab-11e8-856b-098c58fae340&pd_rd_w=yCsfH&pd_rd_wg=tfqA5&pf_rd_i=desktop-dp-sims&pf_rd_m=A3P5ROKL5A1OLE&pf_rd_p=1e3b4162-429b-4ea8-80b8-75d978d3d89e&pf_rd_r=X0AQV5MB76DYGG77BN23&pf_rd_s=desktop-dp-sims&pf_rd_t=40701&psc=1&refRID=X0AQV5MB76DYGG77BN23

https://www.amazon.co.uk/Never-Eat-Alone-Relationship-Portfolio/dp/0241004950


How to access Spark UI of the EMR cluster:
1. `ssh -i ~/.ssh/emr.pem -N -L 4040:{internal master ip address}:4040  hadoop@{external master address}`
2. Go to `localhost:4040`

Bulk rename files s3

aws s3 cp s3://data.api.compressed/events/page_impressions/year=2018/month=09/day=24/ s3://audience-data-store-qa/joana/tests/out-`date +%Y%M%d%H%m%S`.gz --recursive --exclude "*" --include "*windowed*" --dryrun


for f in $(aws s3api list-objects --bucket data.api.compressed --prefix=events/link_impressions/year=2018/month=09/day=24 --output text  | grep windowed | cut  -f 3);
 do aws s3 mv s3://data.api.compressed/$f s3://data.api.compressed/out-`date +%Y%M%d%H%m%S`.gz --dryrun
done


aws s3api list-objects --bucket data.api.compressed --prefix=events/link_impressions/year=2018/month=09/day=24 --output text  | grep windowed | cut  -f 3


for f in $(aws s3api list-objects --bucket data.api.compressed --prefix=events/link_impressions/year=2018/month=09/day=24 --output text  | grep windowed | cut  -f 3);
 do aws s3 mv s3://data.api.compressed/$f s3://data.api.compressed/${f//:/_}
done


### A
https://jaceklaskowski.gitbooks.io/mastering-apache-spark/spark-dynamic-allocation.html
http://antirez.com/news/75 hll
https://en.wikipedia.org/wiki/G%C3%B6del,_Escher,_Bach
https://www.goodreads.com/book/show/28815.Influence
http://www.hpmor.com/


### Slack
http://www.ted.com/talks/dan_pink_on_motivation.html
hive, avro/orc, beeline, elasticsearch, kibana, zeppelin, oozie, hue, ambari
https://use-the-index-luke.com/sql/anatomy/slow-indexes
https://www.essentialsql.com/what-are-the-major-parts-of-a-database/

https://news.ycombinator.com/item?id=19900955

https://in4maniac.wordpress.com/2016/10/09/spark-tutorial/
