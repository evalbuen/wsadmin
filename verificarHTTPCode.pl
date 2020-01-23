#!/usr/bin/env perl

use strict;
use warnings;
use feature 'say';

use HTTP::Tiny;

my $Client = HTTP::Tiny->new();

my @urls = (
    'http://www.yahoo.com',
    'https://www.google.com',
    'http://nosuchsiteexists.com',
);

for my $url (@urls) {
    my $response = $Client->get($url);
    say $url, ": ", $response->{status};
}