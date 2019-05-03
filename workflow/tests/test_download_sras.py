import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../Samples/'

@pytest.mark.downloadse
def test_download_sefastq():
	assert  os.path.exists(os.path.join(test_output_path, "Test1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test1.fastq.gz")) == 228317277

	assert  os.path.exists(os.path.join(test_output_path, "Test2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test2.fastq.gz")) == 115030000

	assert  os.path.exists(os.path.join(test_output_path, "Test3.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test3.fastq.gz")) == 197268189

	assert  os.path.exists(os.path.join(test_output_path, "Test4.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test4.fastq.gz")) == 113240035

@pytest.mark.downloadpe
def test_download_pefastq():
	assert  os.path.exists(os.path.join(test_output_path, "Test5_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_1.fastq.gz")) == 8658420895
	assert  os.path.exists(os.path.join(test_output_path, "Test5_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test5_2.fastq.gz")) == 8567908319

	assert  os.path.exists(os.path.join(test_output_path, "Test6_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_1.fastq.gz")) == 7339767425
	assert  os.path.exists(os.path.join(test_output_path, "Test6_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test6_2.fastq.gz")) == 7665598069

	assert  os.path.exists(os.path.join(test_output_path, "Test7_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_1.fastq.gz")) == 7100662063
	assert  os.path.exists(os.path.join(test_output_path, "Test7_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test7_2.fastq.gz")) == 7344040117

	assert  os.path.exists(os.path.join(test_output_path, "Test8_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_1.fastq.gz")) == 17932922047
	assert  os.path.exists(os.path.join(test_output_path, "Test8_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test8_2.fastq.gz")) == 17267808761

	assert  os.path.exists(os.path.join(test_output_path, "Test9_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test9_1.fastq.gz")) == 11266320428
	assert  os.path.exists(os.path.join(test_output_path, "Test9_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test9_2.fastq.gz")) == 11232327400

	assert  os.path.exists(os.path.join(test_output_path, "Test10_1.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test10_1.fastq.gz")) == 7243006092
	assert  os.path.exists(os.path.join(test_output_path, "Test10_2.fastq.gz"))
	assert  os.path.getsize(os.path.join(test_output_path, "Test10_2.fastq.gz")) == 7489977238
