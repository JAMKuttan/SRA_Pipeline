import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../QC/Raw/'
test_output_mc_path = os.path.dirname(os.path.abspath(__file__)) + '/../QC/Raw/SRADownload.MultiQC.Report_data'

@pytest.mark.multiqchtml
def test_html():
	assert  os.path.exists(os.path.join(test_output_path, "SRADownload.MultiQC.Report.html"))
	assert  os.path.getsize(os.path.join(test_output_path, "SRADownload.MultiQC.Report.html")) == 1343661

@pytest.mark.multiqcfiles
def test_files():
	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc_data.json"))
	assert  os.path.getsize(os.path.join(test_output_mc_path, "multiqc_data.json")) == 1067025

	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc_fastqc.txt"))
	assert  os.path.getsize(os.path.join(test_output_mc_path, "multiqc_fastqc.txt")) == 3447

	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc_general_stats.txt"))
	assert  os.path.getsize(os.path.join(test_output_mc_path, "multiqc_general_stats.txt")) == 1223

	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc.log"))
	assert  os.path.getsize(os.path.join(test_output_mc_path, "multiqc.log")) == 27237
	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc_sources.txt"))
	assert  os.path.getsize(os.path.join(test_output_mc_path, "multiqc_sources.txt")) == 2366
