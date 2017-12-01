my %test = (
  '1212'     => 6,
  '1221'     => 0,
  '123425'   => 4,
  '123123'   => 12,
  '12131415' => 4,
);

sub c {
    my $s = 0; my $l = length($_);
    for my $i (0 .. $l-1) {
        $s += substr($_, $i, 1) if substr($_, $i, 1) == substr($_.$_, $i+$l/2, 1);
    }
    return $s;
}

sub c {
    my $s = 0; my @a = split('', $_[0]);
    for my $i (0 .. $#a) {
        print $i, " ", $a[$i], " ", (@a, @a)[$i+($#a+1)/2], "\n";
        $s += $a[$i] if $a[$i] == (@a, @a)[$i+($#a+1)/2];
    };
    return $s;
}

sub c{$s=0;@a=split('',$_[0]);for$i(0 ..$#a){$s+=$a[$i]if$a[$i]==(@a,@a)[$i+($#a+1)/2]};$s;}

for(keys %test) {
    printf("%s => %s == %s => %s\n", $_, c($_), $test{$_}, c($_) == $test{$_});
}

open my $fh, '<', '01.txt' or die "nope!";
read $fh, my $d, -s $fh;
chomp($d);
printf("%s\n", c($d));
close($fh);
