#!/usr/bin/perl

while (<>) {

	chomp;

	@line = split /;/,;
	
	$line[3] =~ /([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}):/;
	$startDate = $1;
	$startTime = $2;
	
	$line[4] =~ /([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}):/;
	$endDate = $1;
	$endTime = $2;
	
	if( $startDate ne $endDate or $endTime gt $startTime ) {
		$line[3] =~ s/\ .+$//;
		print "$line[0]; $line[1] $line[2] - PROBLEM: $line[3] --> $line[4]\n";
	}
}