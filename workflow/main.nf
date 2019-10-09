#!/usr/bin/env nextflow

// Default parameter values to run tests
params.input = "$baseDir"
params.designFile = "$baseDir/../test.design.tsv"
params.pairedEnd = false
params.output = "$params.input/output/Samples"
params.astrocyte = false

runDir = params.output
designFile = params.designFile
paired = params.pairedEnd
output = params.output
scriptDir = params.scriptDir

designFile = Channel.fromPath(designFile)

//Define channels for the scripts in the scripts directory
checkDesignScript = Channel
  .fromPath("$baseDir/scripts/checkDesignFile.pl")
downloadSRAsScript = Channel
  .fromPath("$baseDir/scripts/downloadSRA.sh")

//Check Design File
process checkDesignFile {
  publishDir "${output}/Design", mode: 'copy'
  tag "Design"

  input:
    file designFile
    file checkDesign from checkDesignScript.first()

  output:
    file "checkedDesignFile.tsv" into checkedDesign mode flatten

  script:
    if (params.astrocyte == true) {
      """
      module load singularity/3.0.2;
      singularity run 'docker://bicf/perlcheckdesign:1.0' perl checkDesignFile.pl --d ${designFile};
      """
    } else {
      """
      perl checkDesignFile.pl --d ${designFile};
      """
    }
}

//Define the SRAs to download from the design file
sraList = checkedDesign
  .splitCsv(sep: '\t', header: true)
  .map { row -> [row.sample_id, row.sra_number ] }

//Download the SRA files, note that this bypasses the creation of the NCBI temp directory in their home directory by using wget
process downloadSRA {
  tag "${sraNumber}_download"
  publishDir "${output}", mode: 'copy'

  input:
    set sampleID, sraNumber from sraList
    file downloadSRA from downloadSRAsScript.first()

  output:
    file "*.fastq.gz" into qccheck mode flatten

  script:
    if (params.astrocyte == true) {
      """
      module load singularity/3.0.2;
      singularity run 'docker://bicf/sratoolkit:1.2' bash downloadSRA.sh ${sraNumber} ${sampleID};
      """
    } else {
      """
      bash downloadSRA.sh ${sraNumber} ${sampleID};
      """
    }
}

//Run FastQC on the SRA data
process rawFastQC {
  publishDir "${output}/QC/Raw", mode: 'copy'
  tag "${fq}_fastqc"

  input:
    file (fq) from qccheck

  output:
    file ("*_fastqc.zip") into sraMultiQC

  script:
    if (params.astrocyte == true) {
      """
      module load singularity/3.0.2;
      singularity run 'docker://bicf/fastqc:1.3' fastqc ${fq} -q -o `pwd -P`;
      """
    } else {
      """
      fastqc ${fq} -q -o `pwd -P`;
      """
    }
}

sampleList = Channel
  .fromFilePairs( ["${output}/*_{1,2}.fastq.gz", "${output}/*_R{1,2}_001.fastq.gz"], size: -1 )

//Run MultiQC on the data and create the updated design file to be pushed to the next process
process rawMultiQC{
  publishDir "${output}/QC/Raw", mode: 'copy'

  input:
    file multiqclist from sraMultiQC.collect()

  script:
    if (params.astrocyte == true) {
      """
      module load singularity/3.0.2;
      singularity run 'docker://bicf/multiqc:1.3' multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${output}/QC/Raw;
      """
    } else {
      """
      multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${output}/QC/Raw;
      """
    }
}