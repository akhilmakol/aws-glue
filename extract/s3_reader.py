def read_s3_data(glueContext, path):
    return glueContext.create_dynamic_frame.from_options(
        connection_type="s3",
        connection_options={"paths": [path]},
        format="parquet"
    ).toDF()
