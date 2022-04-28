# Multi Precision Cairo
### Math of 384 bit numbers in pure cairo

As a part of improving [an eliptical curve library](https://github.com/0xNonCents/cairo-bls12-381) I have taken to implementing a reducible math library for 384 bit numbers.
Division is not complete and will only work for numbers of roughly same size (see comments in code). <br>

The library deals with positive whole integers since this will ultimatley be used in finite field math however the subtraction are included here in case someone wants to use this library for a different purpose. 
The edge case behavior ought to be tuned however for your desired use case.


### How to use

git clone git@github.com:0xNonCents/multi-precision_cairo.git </br>
cd multi-precision_cairo

<b> To test </b> </br>
pytest

<b> Directories and files </b> </br>
  /lib/BigInt6.cairo - A struct representing a 384 bit unsigned integer </br>
  /lib/multi_precision.cairo - Math operations pertaining to this struct </br>
  /contracts/multi_precision.cairo - A test harness contract </br>
  /test/test_multi_precision.py - Tests for each multi_precision operation </br>

