import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../Samples/'

@pytest.mark.downloadse
def test_download_sefastq():
	assert  os.path.exists(os.path.join(test_output_path, "Test5.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5.fastq.gz")) == 228317277

	assert  os.path.exists(os.path.join(test_output_path, "Test6.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6.fastq.gz")) == 115030000

	assert  os.path.exists(os.path.join(test_output_path, "Test7.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7.fastq.gz")) == 197268189

	assert  os.path.exists(os.path.join(test_output_path, "Test8.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8.fastq.gz")) == 113240035

@pytest.mark.downloadpe
def test_download_pefastq():
	assert  os.path.exists(os.path.join(test_output_path, "Test1_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_1.fastq.gz")) == 420568841 
	assert  os.path.exists(os.path.join(test_output_path, "Test1_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_2.fastq.gz")) == 429490444

	assert  os.path.exists(os.path.join(test_output_path, "Test2_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_1.fastq.gz")) == 180441860
	assert  os.path.exists(os.path.join(test_output_path, "Test2_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_2.fastq.gz")) == 182791001

	assert  os.path.exists(os.path.join(test_output_path, "Test3_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_1.fastq.gz")) == 420245128
	assert  os.path.exists(os.path.join(test_output_path, "Test3_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_2.fastq.gz")) == 429777352

	assert  os.path.exists(os.path.join(test_output_path, "Test4_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_1.fastq.gz")) == 139474358
	assert  os.path.exists(os.path.join(test_output_path, "Test4_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_2.fastq.gz")) == 142930243
