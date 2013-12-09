## AOTY

This is a small script I threw together to prettify a list of albums
using information from EchoNest and Last.fm.

The script takes as an arguement a textfile containing a list of albums, in the
format 'artist - album', 1 per line. It gets some simple tags from echonest
and artwork and listener counts from last.fm, then outputs a sortable
grid of album covers using the isotope jquery library.

It is not robust in the slightest, and I don't know if I intend to make it more so,
it was just a quick weekend project. If you want to use it, you need API
keys for echonest and last.fm, and you need to be careful about typos when
making your list of albums.

I also have very little idea what I am doing in python, I just decided to
try out a bunch of different things, so sorry if the organization or syntax
makes me look dumb.
