from pyspark.sql import SparkSession

class SparkControl:
     """Handles ..."""
     def __init__(self):
          """Constructor"""
          global spark 
          spark = SparkSession.builder \
               .appName('SparkByExamples.com') \
               .getOrCreate()

     def __del__(self):
          """Destructor"""
          self.spark.stop()