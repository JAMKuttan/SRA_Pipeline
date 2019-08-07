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

#Check for Spaces in Design File
design_ori=$(cat ${ref} | tr -s ' ' '\t')
design_no=$(sed 's/ \+//g' ${ref})
if [[ ${design_ori} != ${design_no} ]]
then
  echo "Spaces found in Design File. Please remove all spaces from columns"
  exit 5
fi

echo "sample_id	sra_number" > checkedDesignFile.tsv
#Check for Correct Headers
line1=$(head -n 1 ${ref})
line1_check="sample_id	sra_number"
if [[ ${line1} != ${line1_check} ]]
then
  echo "First Line of Design File must read: sample_id	sra_number"
  exit 5
fi

#Check SRA Number Prefix
while read -r line
do
  if [[ ${line} = $(head -n 1 ${ref}) ]]
  then
    continue
  fi

  line_pre=$(echo ${line} | awk '{print $2}' | sed 's/[0-9]*//g' )
  if [[ ${line_pre} = SRR || ${line_pre} = ERR || ${line_pre} = DRR || ${line_pre} = SRA ]]
  then
    echo ${line} | tr -s ' ' '\t'>> checkedDesignFile.tsv
  else
    echo "SRA Number must be SRA#, SRR#, ERR#, or DRR#"
    echo ${line}
    exit 5
  fi
done < ${ref}
