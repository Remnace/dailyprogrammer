281: [Easy]Something About Bases
===========================

https://www.reddit.com/r/dailyprogrammer/comments/504rdh/20160829_challenge_281_easy_something_about_bases/

##Description:

Numbers can be written in many kind of bases.
Normally we use base 10, wich is the decimal notation, for our numbers. In modern computerscience we use base 16 (hexadecimal) a lot, and beneath that we have base 2 (binary).
Given a number you can't tell what base it is, but you can tell what base it isn't from. E.g.: 1 exists in all bases, but 2 does not exist in base 2. It does exist in base 3 and so on.

##Input:

Any number in a base 1-16.

##Output:

The smallest possible base that the given number can belong to, and it's equivalent in base 10.

##Example:

Say you were given:
1
21
ab3
ff
Your output would simply be:
base 2 => 1
base 3 => 7
base 12 => 1575
base 16 => 255
