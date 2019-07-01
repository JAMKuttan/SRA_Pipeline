#!/bin/bash

sraNum=$1;
path=`srapath ${sraNum}`;
sample=`basename ${path}`;
sampleID=$2;
wget ${path};
fastq-dump --gzip --split-3 `readlink -e ${sample}`;
rm ${sample};
for i in `ls | grep ${sraNum}`;
  do name=`echo ${i} | sed -e "s:${sample}:${sampleID}:g"`;
  mv ${i} ${name};
done;
