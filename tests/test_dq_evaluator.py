import pytest
from dq.evaluator import evaluate_dq_metrics
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

@pytest.fixture(scope="session")
def spark_session():
    return SparkSession.builder \
        .appName("DQTest") \
        .master("local[1]") \
        .getOrCreate()

def test_evaluate_dq_metrics(spark_session):
    # Sample data with some nulls and duplicates
    data = [
        (1, "Alice"),
        (2, "Bob"),
        (3, "Charlie"),
        (None, "David"),
        (1, "Alice"),  # Duplicate
        (None, "Eve")
    ]
    df = spark_session.createDataFrame(data, ["id", "name"])

    # Evaluate DQ metrics
    dq_metrics = evaluate_dq_metrics(df)

    assert dq_metrics["row_count"] == 6
    assert dq_metrics["null_counts"]["id"] == 2
    assert dq_metrics["duplicate_count"] == 1
