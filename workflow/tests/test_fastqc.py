import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../Samples/QC/Raw/'

@pytest.mark.fastqcs
def test_fastq_se():
	assert  os.path.exists(os.path.join(test_output_path, "Test5_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_fastqc.zip")) >= 355000

	assert  os.path.exists(os.path.join(test_output_path, "Test6_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_fastqc.zip")) >= 505420

	assert  os.path.exists(os.path.join(test_output_path, "Test7_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_fastqc.zip")) >= 513760

	assert  os.path.exists(os.path.join(test_output_path, "Test8_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_fastqc.zip")) >= 512520

	assert  os.path.exists(os.path.join(test_output_path, "Test1_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_1_fastqc.zip")) >= 450000
	assert  os.path.exists(os.path.join(test_output_path, "Test1_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_2_fastqc.zip"))>= 450000

	assert  os.path.exists(os.path.join(test_output_path, "Test2_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_1_fastqc.zip")) >= 404490
	assert  os.path.exists(os.path.join(test_output_path, "Test2_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_2_fastqc.zip")) >= 450580

	assert  os.path.exists(os.path.join(test_output_path, "Test3_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_1_fastqc.zip")) >= 448420
	assert  os.path.exists(os.path.join(test_output_path, "Test3_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_2_fastqc.zip")) >= 484220

	assert  os.path.exists(os.path.join(test_output_path, "Test4_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_1_fastqc.zip")) >= 415260
	assert  os.path.exists(os.path.join(test_output_path, "Test4_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_2_fastqc.zip")) >= 377050
