#!/usr/bin/perl -w

%poruke=();
$header=0;
$linenum=0;
while ($redak=<>) {
    $linenum++;
	chomp($redak);
    
    if($redak =~ m/From nobody/){
        $header=$linenum;
        $poruke{$header}=0;
    } else {
        $poruke{$header}++;
    }
	
}

%rporuke = reverse %poruke;
$cnt=0;
foreach $key (reverse sort {$a <=> $b} (keys(%rporuke))) {
   $cnt++;
   last if($cnt==39);
   print "$rporuke{$key}: $key\n";
}

