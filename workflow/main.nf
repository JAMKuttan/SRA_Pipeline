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
process download_sra{
  queue '32GB'
  module 'sra_toolkit/2.8.2-1'
  tag "SRA_${sra_number}_download"
  publishDir "${runDir}/Samples", mode: 'copy'
//  afterScript "rm ${runDir}/temp/sra/${sra_number}*"

  input:

  set sample_id, sra_number from sraList

  output:

  file "*.fastq.gz" into qccheck mode flatten

  script:
  """
  path=`srapath ${sra_number}`;
  sample=`basename \${path}`;
  wget \${path};
  fastq-dump --gzip --split-3 `readlink -e \${sample}`;
  rm \${sample};
  for i in `ls | grep ${sra_number}`;
  do name=`echo \${i} | sed -e "s:\${sample}:${sample_id}:g"`;
  mv \${i} \${name};
  done;
  """
}

//Run FastQC on the SRA data
process rawFastQC {
  queue '32GB'
  publishDir "${runDir}/QC/Raw", mode: 'copy'
  tag "${fq}_fastqc"
  module 'fastqc/0.11.5'

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
  queue '32GB'
  publishDir "${runDir}/QC/Raw", mode: 'copy'
  module 'multiqc/1.7'

  input:
  
  file multiqclist from sraMultiQC.collect()

  script:
//  perl $baseDir/scripts/downloadDesignOut.pl --designFile ${designFile} --samples ${runDir}/Samples --output ${runDir}/Samples/design.tsv;
  """
  multiqc -f -n 'SRADownload.MultiQC.Report' ${multiqclist} -o ${runDir}/QC/Raw;
  """
}
