#!/usr/bin/perl

while (<>) {

	chomp;

    if($_ =~ m/[0-9].[0-9]{2};[0-9].[0-9]{2};[0-9].[0-9]{2};[0-9].[0-9]{2};[0-9].[0-9]{2};[0-9].[0-9]{2};[0-9].[0-9]{2}/){
        @points = split /;/;
    } elsif ($_ =~ m/[0-9]{10};/){
        @student = split /;/;
        $marks = 0;

        for($i=0;$i<@points;$i++) {
			if($student[$i+3] ne '-') {
				$marks += $student[$i+3] * $points[$i];
			}
		}
        $position{$student[0]} = sprintf("%.2f",$marks);
		$identity{$student[0]} = $student[1].", ".$student[2];
    }
}
$i = 0;
print "Lista po rangu:\n-------------------\n";
foreach $key (sort { $position{$b} <=> $position{$a} } keys %position) {
    $i++;
	print "$i. $identity{$key} ($key) : $position{$key}\n";
}