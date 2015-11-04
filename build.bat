rmdir /s/q build
mkdir build
cd build
cmake -G"Visual Studio 14 2015 Win64" ..
msbuild cryptopp.sln /t:cryptlib /p:Configuration=Release;Platform=x64
msbuild cryptopp.sln /t:cryptlib /p:Configuration=Debug;Platform=x64
