# aws-glue
Modularize AWS Glue ETL Project Structure

glue_etl_project/
├── config.py
├── glue_job.py
├── extract/
│   └── s3_reader.py
├── transform/
│   ├── data_cleaning.py
│   └── data_enrichment.py
├── load/
│   └── s3_writer.py
├── dq/
│   ├── evaluator.py        # Data Quality evaluation logic
│   └── glue_updater.py     # Update Glue table properties with DQ metrics
├── tests/
│   ├── test_transform.py
│   ├── test_dq_evaluator.py  # New test file for dq.evaluator.py
│   └── test_glue_updater.py  # New test file for dq.glue_updater.py
├── conftest.py
├── requirements.txt
├── README.md
├── cfn_glue_etl.yml
└── terraform/
    └── main.tf
