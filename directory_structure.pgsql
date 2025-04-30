glue_etl_project/
│
├── glue_job.py                  # Main ETL job script
├── config.py                    # Configuration (e.g., table names, paths)
│
├── extract/
│   └── s3_reader.py             # Reads from S3
│   └── jdbc_reader.py           # Reads from JDBC sources
│
├── transform/
│   └── data_cleaning.py         # Cleansing, filtering
│   └── data_enrichment.py       # Joins, derives columns
│
├── load/
│   └── s3_writer.py             # Write to S3
│   └── redshift_writer.py       # Write to Redshift


