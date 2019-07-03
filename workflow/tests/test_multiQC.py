import pytest
from io import StringIO
import os

test_output_path = os.path.dirname(os.path.abspath(__file__)) + '/../Samples/QC/Raw/'
test_output_mc_path = os.path.dirname(os.path.abspath(__file__)) + '/../Samples/QC/Raw/SRADownload.MultiQC.Report_data'

@pytest.mark.multiqc
def test_html():
	assert os.path.exists(os.path.join(test_output_path, "SRADownload.MultiQC.Report.html"))
	assert os.path.exists(os.path.join(test_output_mc_path, "multiqc_data.json"))
	assert os.path.exists(os.path.join(test_output_mc_path, "multiqc_fastqc.txt"))
	assert os.path.exists(os.path.join(test_output_mc_path, "multiqc_general_stats.txt"))
	assert os.path.exists(os.path.join(test_output_mc_path, "multiqc.log"))
	assert  os.path.exists(os.path.join(test_output_mc_path, "multiqc_sources.txt"))
