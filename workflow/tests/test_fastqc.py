import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../QC/Raw/'

@pytest.mark.fastqcse
def test_fastq_se():
	assert  os.path.exists(os.path.join(test_output_path, "Test5_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_fastqc.zip")) == 359397

	assert  os.path.exists(os.path.join(test_output_path, "Test6_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_fastqc.zip")) == 505423

	assert  os.path.exists(os.path.join(test_output_path, "Test7_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_fastqc.zip")) == 513766

	assert  os.path.exists(os.path.join(test_output_path, "Test8_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_fastqc.zip")) == 512527

@pytest.mark.fastqcpe
def test_fastqc_pe():
	assert  os.path.exists(os.path.join(test_output_path, "Test1_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_1_fastqc.zip")) == 496528
	assert  os.path.exists(os.path.join(test_output_path, "Test1_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_2_fastqc.zip")) == 466430

	assert  os.path.exists(os.path.join(test_output_path, "Test2_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_1_fastqc.zip")) == 404496
	assert  os.path.exists(os.path.join(test_output_path, "Test2_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_2_fastqc.zip")) == 450588

	assert  os.path.exists(os.path.join(test_output_path, "Test3_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_1_fastqc.zip")) == 448430
	assert  os.path.exists(os.path.join(test_output_path, "Test3_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_2_fastqc.zip")) == 484224

	assert  os.path.exists(os.path.join(test_output_path, "Test4_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_1_fastqc.zip")) == 415272
	assert  os.path.exists(os.path.join(test_output_path, "Test4_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_2_fastqc.zip")) == 377054
