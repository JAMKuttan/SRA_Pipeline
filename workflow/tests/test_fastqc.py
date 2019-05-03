import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../QC/Raw/'

@pytest.mark.fastqcse
def test_fastq_se():
	assert  os.path.exists(os.path.join(test_output_path, "Test1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_fastqc.zip")) == 359397

	assert  os.path.exists(os.path.join(test_output_path, "Test2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_fastqc.zip")) == 505423

	assert  os.path.exists(os.path.join(test_output_path, "Test3_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_fastqc.zip")) == 513766

	assert  os.path.exists(os.path.join(test_output_path, "Test4_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_fastqc.zip")) == 512527

@pytest.mark.fastqcpe
def test_fastqc_pe():
	assert  os.path.exists(os.path.join(test_output_path, "Test5_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_1_fastqc.zip")) == 391452
	assert  os.path.exists(os.path.join(test_output_path, "Test5_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_2_fastqc.zip")) == 406623

	assert  os.path.exists(os.path.join(test_output_path, "Test6_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_1_fastqc.zip")) == 291458
	assert  os.path.exists(os.path.join(test_output_path, "Test6_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_2_fastqc.zip")) == 453684

	assert  os.path.exists(os.path.join(test_output_path, "Test7_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_1_fastqc.zip")) == 403960
	assert  os.path.exists(os.path.join(test_output_path, "Test7_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_2_fastqc.zip")) == 399679

	assert  os.path.exists(os.path.join(test_output_path, "Test8_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_1_fastqc.zip")) == 448358
	assert  os.path.exists(os.path.join(test_output_path, "Test8_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_2_fastqc.zip")) == 339385

	assert  os.path.exists(os.path.join(test_output_path, "Test9_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test9_1_fastqc.zip")) == 331225
	assert  os.path.exists(os.path.join(test_output_path, "Test9_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test9_2_fastqc.zip")) == 399042

	assert  os.path.exists(os.path.join(test_output_path, "Test10_1_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test10_1_fastqc.zip")) == 300672
	assert  os.path.exists(os.path.join(test_output_path, "Test10_2_fastqc.zip"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test10_2_fastqc.zip")) == 300246
