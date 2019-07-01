#!/bin/bash

path=`srapath ${sra_number}`;
sample=`basename ${path}`;
samplePath=`readlink -e ${sample}`;
wget ${path};
fastq-dump --gzip --split-3 ${samplePath};
rm ${sample};
for i in `ls | grep ${sra_number}`;
  do name=`echo ${i} | sed -e "s:${sample}:${sample_id}:g"`;
  mv ${i} ${name};
done;
