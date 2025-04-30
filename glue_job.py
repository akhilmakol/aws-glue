from extract.s3_reader import read_s3_data
from transform.data_cleaning import clean_data
from transform.data_enrichment import enrich_data
from load.s3_writer import write_to_s3

from awsglue.context import GlueContext
from pyspark.context import SparkContext

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session

def main():
    # Step 1: Extract
    df_raw = read_s3_data(glueContext, "s3://my-bucket/input-data/")

    # Step 2: Transform
    df_clean = clean_data(df_raw)
    df_final = enrich_data(df_clean)

    # Step 3: Load
    write_to_s3(df_final, "s3://my-bucket/output-data/")

if __name__ == "__main__":
    main()
