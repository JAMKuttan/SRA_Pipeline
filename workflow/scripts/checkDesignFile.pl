#!/usr/bin/perl

use warnings;
use strict;
use Getopt::Long qw(:config no_ignore_case no_auto_abbrev);

my ${designFile} = '';
my ${fail} = 0;
my %{failed};

GetOptions ("d=s" => \${designFile});

open (OUT,">>checkedDesignFile.tsv") or die "Error: Unable to print to validated design file.";
open (IN,"${designFile}");

print OUT "sample_id\tsra_number";

while (my ${line} = <IN>){
	chomp ${line};
	${line} =~ s/\r\n$//g;
	${line} =~ s/[\s]+/\t/g;
	next if (lc ${line} =~ m/^sample_id\tsra_number/);
	my @parts = split (/\t/, ${line});
	my ${sraCheck} = ${parts[1]};
	${sraCheck} = substr ${parts[1]}, 1, 2;
	if (${sraCheck} =~ m/RP/){
		${fail} = 1;
		${failed}{${parts[1]}} = "SRP, ERP, DRP are project numbers and contain multiple files. Please list each SRA in these projects individually. This feature will be included in later versions.";
	} elsif (${sraCheck} =~ m/[RA,RR,RX,RS]/){
		print OUT "\n${parts[0]}\t${parts[1]}";
	} else {
		${fail} = 1;
		${failed}{${parts[1]}} = "Error: Invalid SRA number format found:\t${parts[1]}\nTerminating.\n";
	}
}

if (${fail} != 0){
	my ${errorMessage} = "The following problems were found:";
	for my ${failure} (keys %{failed}){
		my ${code} = ${failed}{${failure}};
		${errorMessage} .= "\n${failure}\t${code}";
	}
	die "${errorMessage}";
}

close IN;
close OUT;
