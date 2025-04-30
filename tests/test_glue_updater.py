from unittest.mock import patch, MagicMock
import pytest
from dq.glue_updater import update_glue_table_dq_metrics

def test_update_glue_table_dq_metrics():
    # Simulated DQ metrics
    dq_metrics = {
        'row_count': 1000,
        'null_counts': {'id': 5, 'name': 3},
        'duplicate_count': 10
    }

    # Mock the boto3 Glue client
    mock_glue_client = MagicMock()
    
    with patch("boto3.client", return_value=mock_glue_client):
        # Call the method to update Glue table properties
        update_glue_table_dq_metrics("my_database", "my_table", dq_metrics)
        
        # Check if Glue update method was called with correct parameters
        mock_glue_client.update_table.assert_called_once_with(
            DatabaseName="my_database",
            TableName="my_table",
            TableInput={
                'Parameters': {
                    'dq_row_count': '1000',
                    'dq_nulls_id': '5',
                    'dq_nulls_name': '3',
                    'dq_duplicates': '10'
                }
            }
        )
