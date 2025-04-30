def enrich_data(df):
    from pyspark.sql.functions import current_timestamp
    return df.withColumn("processed_time", current_timestamp())
