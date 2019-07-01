#!/usr/bin/env nextflow

// Default parameter values to run tests
params.input = "$baseDir"
params.designFile = "$baseDir/../test.design.tsv"
params.pairedEnd = false

runDir = params.input
designFile = params.designFile
paired = params.pairedEnd

//Define the SRAs to download from the design file
sraList = Channel
  .fromPath(designFile)
  .flatten()
  .splitCsv(sep: '\t', header: true)
  .map { row -> [row.sample_id, row.sra_number ] }

//Download the SRA files
process downloadSRA {
  tag "${sra_number}_download"
  publishDir "${runDir}/Samples", mode: 'copy'

  input:
    set sample_id, sra_number from sraList

  output:
    file "*.fastq.gz" into qccheck mode flatten

  script:
    """
    bash ${baseDir}/scripts/downloadSRA.sh ${sra_number} ${sample_id};
    """
}

//Run FastQC on the SRA data
process rawFastQC {
  publishDir "${runDir}/QC/Raw", mode: 'copy'
  tag "${fq}_fastqc"

  input:
    file (fq) from qccheck

  output:
    file ("*_fastqc.zip") into sraMultiQC

  script:
    """
    fastqc ${fq} -t \$SLURM_CPUS_ON_NODE -q -o `pwd -P`;
    """
}

sampleList = Channel
  .fromFilePairs( ["${runDir}/Samples/*_{1,2}.fastq.gz", "${runDir}/Samples/*_R{1,2}_001.fastq.gz"], size: -1 )

//Run MultiQC on the data and create the updated design file to be pushed to the next process
process rawMultiQC{
  publishDir "${runDir}/QC/Raw", mode: 'copy'

  input:
    file multiqclist from sraMultiQC.collect()

  script:
    """
    multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${runDir}/QC/Raw;
    """
}
