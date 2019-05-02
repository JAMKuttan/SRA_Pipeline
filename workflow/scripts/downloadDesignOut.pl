#!/usr/bin/perl -w

use warnings;
use strict;
use Getopt::Long qw(:config no_ignore_case no_auto_abbrev);

my $oriDesign = '';
my $outDesign = '';
my $sampleDir = '';
my $design = {};

GetOptions("designFile=s" => \$oriDesign,
	"output=s" => \$outDesign,
	"samples=s" => \$sampleDir);

#Read in the original design file, and determine if paired-end or single-end
open (IN,${oriDesign}) or die "Error: Unable to open input design file.  Please make sure the file exists and is user-readable.";
while (my $line = <IN>) {
	chomp ${line};
	next if (${line} =~ m/^#sample_id\t/);
	my @parts = (split /\t/, ${line});
	$design->{$parts[0]}->{SRA} = $parts[1];
	if ( -f "${sampleDir}/$parts[0]_1.fastq.gz" || -f "${sampleDir}/$parts[0]_*_R1_*.fastq.gz" || -f ("${sampleDir}/$parts[0].fastq.gz")){
		$design->{$parts[0]}->{'fq1'} = "$parts[0]_1.fastq.gz" if -e "${sampleDir}\/$parts[0]_1.fastq.gz";
		$design->{$parts[0]}->{'fq1'} = "$parts[0]_*_R1_*.fastq.gz" if -e "${sampleDir}\/$parts[0]_*_R1_*.fastq.gz";
		$design->{$parts[0]}->{'fq1'} = "$parts[0].fastq.gz" if -e "${sampleDir}\/$parts[0].fastq.gz"; 
	} else {
		die "Unable to locate a valid read file for the read \"$parts[0]\".  Please verify that the file downloaded correctly.";
	}
	if ( -f "${sampleDir}/$parts[0]_2.fastq.gz" || -f "${sampleDir}/$parts[0]_*_R2_*.fastq.gz"){
		$design->{$parts[0]}->{'paired'} = "paired";
                $design->{$parts[0]}->{'fq2'} = "$parts[0]_2.fastq.gz" if -e "${sampleDir}/$parts[0]_2.fastq.gz";
                $design->{$parts[0]}->{'fq2'} = "$parts[0]_*_R2_*.fastq.gz" if -e "${sampleDir}/$parts[0]_*_R2_*.fastq.gz";
	} else{
		$design->{$parts[0]}->{'paired'} = "single";
	}
}
close IN;

#Print the updated design file
open(OUT,">${outDesign}") or die "Error: Unable to open the specified output design file.  Please ensure that you have write access to the specified sub-directory.";
print OUT "#sample_id\tsra_number\tpairing\tfq1\tfq2\n";
foreach my $sample (keys %$design){
	print OUT "$sample\t$design->{$sample}->{'SRA'}\t$design->{$sample}->{'paired'}\t$design->{$sample}->{'fq1'}\t$design->{$sample}->{'fq2'}\n"
}
