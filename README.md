## Introduction
This pipeline is a simple method for downloading bulk SRA data, and renaming it, and having it ready to use in our other Astrocyte pipelines [BICF](http://www.utsouthwestern.edu/labs/bioinformatics/) at [UT Southwestern Dept. of Bioinformatics](http://www.utsouthwestern.edu/departments/bioinformatics/).

The pipeline uses [Nextflow](https://www.nextflow.io), a bioinformatics workflow tool, to download multiple files simultaneously, speeding up the process.  Once the files have been downloaded, it runs [FastQC](https://www.bioinformatics.babraham.ac.uk/projects/fastqc/) to check the individual file quality metrics, and [MultiQC](https://multiqc.info/) on the entire data set, once the downloads have finished.

This pipeline was designed to use a SLURM setup, as used by the [BioHPC Cluster](https://biohpc.swmed.edu/), however should be adaptable to run on nearly any system using and supported by Nextflow.

Eventually, we should be able to integrate this pipeline into the [Astrocyte Workflow System](https://astrocyte-test.biohpc.swmed.edu/static/docs/index.html) as part of both a stand-alone script, or as part of additional scripts.

## Prerequisite Files
This pipeline requires a very simple design, tab delimited file:
Line 1 must be the following header: "#sample_id	sra_number"
Each subsequent line should then contain, in order the sample ID (whatever you wish to call the sample), and the SRA number from NCBI.