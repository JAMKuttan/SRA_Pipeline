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

design = Channel.fromPath(designFile)

//Check Design File
process checkDesignFile {
  publishDir "${output}/Design", mode: 'copy'
  tag "Design"

  input:
    file design

  output:
    file "checkedDesignFile.tsv" into checkedDesign mode flatten

  script:
    """
    perl ${baseDir}/scripts/checkDesignFile.pl --d ${design};
    """
}

//Define the SRAs to download from the design file
sraList = checkedDesign
  .splitCsv(sep: '\t', header: true)
  .map { row -> [row.sample_id, row.sra_number ] }

//Download the SRA files
process downloadSRA {
  tag "${sraNumber}_download"
  publishDir "${output}", mode: 'copy'

  input:
    set sampleID, sraNumber from sraList

  output:
    file "*.fastq.gz" into qccheck mode flatten

  script:
    if (params.astrocyte == true) {
      """
      module load singularity/3.0.2;
      singularity run /project/shared/bicf_workflow_ref/singularity_images/sratoolkit.sif bash ${baseDir}/scripts/downloadSRA.sh ${sraNumber} ${sampleID};
      """
    } else {

      """
      bash ${baseDir}/scripts/downloadSRA.sh ${sraNumber} ${sampleID};
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
      singularity run /project/shared/bicf_workflow_ref/singularity_images/fastqc.sif fastqc ${fq} -q -o `pwd -P`;
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
      singularity run /project/shared/bicf_workflow_ref/singularity_images/multiqc.sif multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${output}/QC/Raw;
      """
    } else {
      """
      multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${output}/QC/Raw;
      """
    }
}
