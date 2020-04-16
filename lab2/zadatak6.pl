#!/usr/bin/perl

use open ':locale';
use locale;

$len = pop(@ARGV);

while(<>){
	$line = lc;
	@prefs = $line =~ m/\b(\w{$len})/g;
	foreach $pref (@prefs){
		$counter{$pref}++;
	}
}

@prefs = keys %counter;

foreach $pref (sort @prefs){
	print "$pref : $counter{$pref}\n";
}