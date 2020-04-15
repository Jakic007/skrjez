#!/usr/bin/perl -w

$flag=0;
while(<>){
    # Matched regex put into date and hour variable
    ($date) = $ARGV =~ m/([\d]{4}-[\d]{2}-[\d]{2})/;
    $_ =~ m/[\d]{4}:([\d]{2}):[\d]{2}:[\d]{2}/;
    # Test if it is first entry of that day
    if(!($flag)){
        print "\nDatum: $date\n";
        print "sat : broj pristupa\n";
        print "-------------------------------\n";
        $count{$1}++;
        $flag=1;
    } else {
        $count{$1}++;
    }
    if( eof ) {
        # Sorting keys based on ASCII table
        foreach $time (sort keys %count){
            printf "%3d : %d\n",$time,$count{$time};
        }
        $flag=0;
        %count=();
    }
}
