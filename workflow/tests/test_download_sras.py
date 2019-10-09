import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../output/Samples/'

@pytest.mark.downloads
def test_download_sefastq():
	assert  os.path.exists(os.path.join(test_output_path, "Test6.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6.fastq.gz")) >= 115000000

	assert  os.path.exists(os.path.join(test_output_path, "Test7.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7.fastq.gz")) >= 197000000

	assert  os.path.exists(os.path.join(test_output_path, "Test8.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8.fastq.gz")) >= 113000000

	assert  os.path.exists(os.path.join(test_output_path, "Test1_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_1.fastq.gz")) >= 420000000 
	assert  os.path.exists(os.path.join(test_output_path, "Test1_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1_2.fastq.gz")) >= 429000000

	assert  os.path.exists(os.path.join(test_output_path, "Test2_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_1.fastq.gz")) >= 180000000
	assert  os.path.exists(os.path.join(test_output_path, "Test2_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2_2.fastq.gz")) >= 182000000

	assert  os.path.exists(os.path.join(test_output_path, "Test3_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_1.fastq.gz")) >= 420000000
	assert  os.path.exists(os.path.join(test_output_path, "Test3_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3_2.fastq.gz")) >= 429000000

	assert  os.path.exists(os.path.join(test_output_path, "Test4_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_1.fastq.gz")) >= 139000000
	assert  os.path.exists(os.path.join(test_output_path, "Test4_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4_2.fastq.gz")) >= 142000000
