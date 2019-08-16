#!/bin/bash
#checkDesignFile.sh

usage() {
  echo "-d  --design file"
  exit 1
}

OPTIND=1
while getopts :d: opt
do
  case ${opt} in
    d) ref=${OPTARG};;
  esac
done 

shift $((${OPTIND} -1))

echo "sample_id	sra_number" > checkedDesignFile.tsv
sed -i '/^$/d' ${ref}
sed -e 's/\r$//g' ${ref}
sed -e 's///g' ${ref}

#Check SRA Number Prefix
while read -r line
do
  if [[ ${line} = $(head -n 1 ${ref}) ]]
  then
    continue
  fi

  line_pre=$(echo ${line} | awk '{print $2}' | sed 's/[0-9]*//g' )

  if [[ ${line_pre} = SRP || ${line_pre} = ERP || ${line_pre} = DRP ]]
  then
    echo "SRP, ERP, DRP are project numbers and contain multiple files. Please list each SRA in these projects individually. This feature will be included in later versions."
    echo ${line}
    exit 5
  fi

  if [[ ${line_pre} = SRA || ${line_pre} = ERA || ${line_pre} = DRA || ${line_pre} = SRR || ${line_pre} = ERR || ${line_pre} = DRR || ${line_pre} = SRX || ${line_pre} = ERX || ${line_pre} = DRX || ${line_pre} = SRS || ${line_pre} = ERS || ${line_pre} = DRS ]]
  then
    echo ${line} | tr -s ' ' '\t'>> checkedDesignFile.tsv
  else
    echo "Please input valid SRA Number"
    echo ${line}
    exit 5
  fi
done < ${ref}
