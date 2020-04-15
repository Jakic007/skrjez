#!/usr/bin/perl
print "Upiši neki niz znakova:\n";
chomp($line= <STDIN>);
if ($line eq "\n") {
    print "To je samo prazni redak!\n";
}
else {
    print "Ucitani redak je: $line\nSada unesi neki broj ponavljanja:\n";
}
chomp($rep= <STDIN>);
if ($rep eq "\n") {
    print "To je samo prazni redak!\n";
} elsif ($rep <= 0){
    print "Potreban je pozitivan broj!\n"
}
else{
    while ($rep > 0){
        $rep -= 1;
        print "$line\n";
    }
}