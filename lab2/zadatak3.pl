#!/usr/bin/perl -w

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
            $format = sprintf "%02d : %d\n",$time,$count{$time};
            print $format;
        }
        $flag=0;
        %count=();
    }
}
