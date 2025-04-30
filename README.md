Project Overview
-----------------

This project implements a scalable, modular ETL pipeline using AWS Glue and PySpark. It is designed to perform three key tasks—Extract, Transform, and Load—with each step modularized into separate Python scripts for better maintainability, readability, and flexibility.

Extract: The extraction process reads data from an S3 bucket and converts it into a format that can be processed (e.g., converting data to DataFrames).

Transform: The transformation step applies data cleaning and enrichment techniques, ensuring the data is in the right format and enhanced with any required additional information.

Load: Finally, the processed data is loaded back into an S3 bucket in a specified output location.

The modular structure of the project allows for easy customization, testing, and scaling, making it ideal for large datasets or future integrations with other tools or data sources. This pipeline can run both locally using PySpark or within AWS Glue as a managed service, providing flexibility for various environments. It also integrates with AWS CloudFormation and Terraform to simplify the deployment process in the cloud.

Project Structure
------------------
glue_etl_project/ ├── config.py # Configuration settings (input/output paths) ├── glue_job.py # Main entry point for running the ETL job ├── extract/ │ └── s3_reader.py # Extraction module (reads data from S3) ├── transform/ │ ├── data_cleaning.py # Transformation module (cleans data) │ └── data_enrichment.py # Transformation module (enriches data) ├── load/ │ └── s3_writer.py # Loading module (writes data to S3) ├── tests/ │ ├── test_transform.py # Unit tests for transformation logic │ └── test_dq_evaluator.py # Tests for data quality and validation ├── conftest.py # Pytest configuration and fixtures ├── .gitignore # Git ignore file for unnecessary files ├── LICENSE # Project License ├── requirements.txt # Python dependencies ├── README.md # Project documentation ├── cfn_glue_etl.yml # AWS CloudFormation template for deployment └── terraform/ └── main.tf # Terraform configuration for AWS infrastructure

Running the ETL job locally
----------------------------
You can run the ETL job on your local machine using PySpark. Make sure to configure the input and output paths in your environment variables. This will execute the extraction, transformation, and loading process locally.

export INPUT_PATH="s3://your-bucket/input/"
export OUTPUT_PATH="s3://your-bucket/output/"
python glue_job.py

Run the Unit Tests
-------------------
The project includes unit tests for the transformation logic. Use pytest to run the tests:
pytest tests/

Deploying with AWS CloudFormation
----------------------------------
You can deploy the Glue ETL job and necessary AWS resources using CloudFormation. First, deploy the stack with the following command:

aws cloudformation deploy \
  --template-file cfn_glue_etl.yml \
  --stack-name glue-etl-stack \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    InputS3Path=s3://your-bucket/input/ \
    OutputS3Path=s3://your-bucket/output/ \
    ScriptLocation=s3://your-bucket/glue_etl_project/glue_job.py

Deploying with Terraform
-------------------------
cd terraform
terraform init
terraform apply -var input_s3_path="s3://your-bucket/input/" \
                -var output_s3_path="s3://your-bucket/output/" \
                -var script_location="s3://your-bucket/glue_etl_project/glue_job.py"

Key Features
-------------
1. Modular Architecture: Clear separation between extract, transform, and load logic.
2. Unit Tests: Written using pytest for validating transformation logic and ensuring data quality.
3. AWS Glue Compatibility: The ETL pipeline is designed for AWS Glue jobs but can also be run locally with PySpark.
4. CloudFormation & Terraform Deployment: Deploy the entire ETL pipeline and supporting resources through CloudFormation or Terraform.
5. Data Quality and Validation: Includes integration with a data quality evaluator to ensure clean and accurate data processing.

 Requirements
 -------------
1.Python 3.x
2. PySpark
3. AWS Glue
4. AWS CLI (for CloudFormation deployment)

License
-------
MIT License © 2025 Akhil Makol

