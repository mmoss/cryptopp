# Crypto++
## C++ Cryptographic Schemes

This is a github hosted version of the Crypto++ library source from the [Crypto++ download link](http://www.cryptopp.com/#download).

I've added [scons](http://www.scons.org/) build files to build the source as either a shared or static library with or without debug information.

By default the code builds as a static library. To build the code as a shared library:

	scons --shared

To include debug flags when compiling pass an --enable-debug parameter like so:

	scons --enable-debug
