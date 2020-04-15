#!/usr/bin/perl
print "Upiši neki niz brojeva:\nKraj upisivanja ctrl+D\n";
chomp(@lines=<STDIN>);
$sum=0;
foreach $line (@lines) {
    $sum += $line;
}
$result= $sum / scalar @lines;
print "Aritmetička sredina je: " . $result . "\n";