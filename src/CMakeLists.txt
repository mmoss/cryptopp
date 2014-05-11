#########################
# Crypto++ Library
#########################

CONFIGURE_FILE(adhoc.cpp.proto ${CMAKE_CURRENT_SOURCE_DIR}/adhoc.cpp)

SET(CRYPTOPP_SRCS_FIPS
	algebra.cpp 
	algparam.cpp 
	asn.cpp 
	authenc.cpp 
	basecode.cpp 
	cbcmac.cpp 
	ccm.cpp 
	channels.cpp 
	cmac.cpp 
	cpu.cpp 
	cryptlib.cpp 
	des.cpp 
	dessp.cpp 
	dh.cpp 
	dll.cpp 
	dsa.cpp 
	ec2n.cpp 
	eccrypto.cpp 
	ecp.cpp 
	emsa2.cpp 
	eprecomp.cpp 
	files.cpp 
	filters.cpp 
	fips140.cpp 
	gcm.cpp 
	gf2n.cpp 
	gfpcrypt.cpp 
	hex.cpp 
	hmac.cpp 
	hrtimer.cpp 
	integer.cpp 
	iterhash.cpp 
	misc.cpp 
	modes.cpp 
	mqueue.cpp 
	nbtheory.cpp 
	oaep.cpp 
	osrng.cpp 
	pch.cpp 
	pkcspad.cpp 
	pssr.cpp 
	pubkey.cpp 
	queue.cpp 
	randpool.cpp 
	rdtables.cpp 
	rijndael.cpp 
	rng.cpp 
	rsa.cpp 
	rw.cpp 
	sha.cpp 
	simple.cpp 
	skipjack.cpp 
	strciphr.cpp 
	trdlocal.cpp
)

SET(CRYPTOPP_SRCS 
	3way.cpp 
	adhoc.cpp.proto 
	adler32.cpp 
	arc4.cpp 
	base32.cpp 
	base64.cpp 
	bfinit.cpp 
	blowfish.cpp 
	blumshub.cpp 
	camellia.cpp 
	cast.cpp 
	casts.cpp 
	crc.cpp 
	default.cpp 
	dh2.cpp 
	eax.cpp 
	elgamal.cpp 
	esign.cpp 
	gf256.cpp 
	gf2_32.cpp 
	gost.cpp 
	gzip.cpp 
	ida.cpp 
	idea.cpp 
	luc.cpp 
	mars.cpp 
	marss.cpp 
	md2.cpp 
	md4.cpp 
	md5.cpp 
	mqv.cpp 
	network.cpp 
	panama.cpp 
	polynomi.cpp 
	rabin.cpp 
	rc2.cpp 
	rc5.cpp 
	rc6.cpp 
	ripemd.cpp 
	safer.cpp 
	salsa.cpp 
	seal.cpp 
	seed.cpp 
	serpent.cpp 
	sha3.cpp 
	shacal2.cpp 
	shark.cpp 
	sharkbox.cpp 
	socketft.cpp 
	sosemanuk.cpp 
	square.cpp 
	squaretb.cpp 
	tea.cpp 
	tftables.cpp 
	tiger.cpp 
	tigertab.cpp 
	ttmac.cpp 
	twofish.cpp 
	vmac.cpp 
	wait.cpp 
	wake.cpp 
	whrlpool.cpp 
	winpipes.cpp 
	xtr.cpp 
	xtrcrypt.cpp 
	zdeflate.cpp 
	zinflate.cpp 
	zlib.cpp 
)
SET(CRYPTOPP_HDRS
		3way.h 
		adler32.h 
		aes.h 
		algebra.h 
		algparam.h 
		arc4.h 
		argnames.h 
		asn.h 
		authenc.h 
		base32.h 
		base64.h 
		basecode.h 
		blowfish.h 
		blumshub.h 
		camellia.h 
		cast.h 
		cbcmac.h 
		ccm.h 
		channels.h 
		cmac.h 
		config.h 
		cpu.h 
		crc.h 
		cryptlib.h 
		default.h 
		des.h 
		dh.h 
		dh2.h 
		dmac.h 
		dsa.h 
		eax.h 
		ec2n.h 
		eccrypto.h 
		ecp.h 
		elgamal.h 
		emsa2.h 
		eprecomp.h 
		esign.h 
		files.h 
		filters.h 
		fips140.h 
		fltrimpl.h 
		gcm.h 
		gf256.h 
		gf2_32.h 
		gf2n.h 
		gfpcrypt.h 
		gost.h 
		gzip.h 
		hex.h 
		hmac.h 
		hrtimer.h 
		ida.h 
		idea.h 
		integer.h 
		iterhash.h 
		lubyrack.h 
		luc.h 
		mars.h 
		md2.h 
		md4.h 
		md5.h 
		mdc.h 
		misc.h 
		modarith.h 
		modes.h 
		modexppc.h 
		mqueue.h 
		mqv.h 
		nbtheory.h 
		network.h 
		nr.h 
		oaep.h 
		oids.h 
		osrng.h 
		panama.h 
		pch.h 
		pkcspad.h 
		polynomi.h 
		pssr.h 
		pubkey.h 
		pwdbased.h 
		queue.h 
		rabin.h 
		randpool.h 
		rc2.h 
		rc5.h 
		rc6.h 
		rijndael.h 
		ripemd.h 
		rng.h 
		rsa.h 
		rw.h 
		safer.h 
		salsa.h 
		seal.h 
		secblock.h 
		seckey.h 
		seed.h 
		serpent.h 
		sha.h 
		sha3.h 
		shacal2.h 
		shark.h 
		simple.h 
		skipjack.h 
		smartptr.h 
		socketft.h 
		sosemanuk.h 
		square.h 
		stdcpp.h 
		strciphr.h 
		tea.h 
		tiger.h 
		trdlocal.h 
		trunhash.h 
		ttmac.h 
		twofish.h 
		vmac.h 
		wait.h 
		wake.h 
		whrlpool.h 
		winpipes.h 
		words.h 
		xtr.h 
		xtrcrypt.h 
		zdeflate.h 
		zinflate.h 
		zlib.h 

)

SET(CRYPTOPP_SRCS ${CRYPTOPP_SRCS} ${CRYPTOPP_SRCS_FIPS})

IF(WIN32)
	SET(CRYPTOPP_SRCS ${CRYPTOPP_SRCS} ${CRYPTOPP_HDRS} cryptopp.rc)
	IF(CMAKE_CL_64)
		ENABLE_LANGUAGE(ASM_MASM)
		ADD_CUSTOM_COMMAND(
			OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/x64dll.obj
			MAIN_DEPENDENCY x64dll.asm
			COMMAND ${CMAKE_ASM_MASM_COMPILER} /Fo ${CMAKE_CURRENT_BINARY_DIR}/x64dll.obj /c ${CMAKE_CURRENT_SOURCE_DIR}/x64dll.asm
		)
		ADD_CUSTOM_COMMAND(
			OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/x64masm.obj
			MAIN_DEPENDENCY x64masm.asm
			COMMAND ${CMAKE_ASM_MASM_COMPILER} /Fo ${CMAKE_CURRENT_BINARY_DIR}/x64masm.obj /c ${CMAKE_CURRENT_SOURCE_DIR}/x64masm.asm
		)
	ENDIF()
ENDIF()

#########################
# Crypto++ Static library
#########################
IF(CRYPTOPP_STATIC)
	IF(CMAKE_CL_64)
	SET(CRYPTOPP_SRCS ${CRYPTOPP_SRCS}
		${CMAKE_CURRENT_BINARY_DIR}/x64dll.obj
		${CMAKE_CURRENT_BINARY_DIR}/x64masm.obj
	)
	ENDIF()
	ADD_LIBRARY(cryptlib STATIC 
		${CRYPTOPP_SRCS}
		)
	SET_TARGET_PROPERTIES(cryptlib PROPERTIES ${CRYPTOPP_COMPILE_DEFS_OPT} COMPILE_DEFINITIONS CRYPTOPP_LIBRARY_BUILD)
	IF(CRYPTOPP_LDFLAGS)
	  SET_TARGET_PROPERTIES(cryptlib PROPERTIES LINK_FLAGS ${CRYPTOPP_LDFLAGS})
	ENDIF()
	TARGET_LINK_LIBRARIES(cryptlib)
ENDIF()

#########################
# Crypto++ Shared library
#########################
IF(CRYPTOPP_SHARED)
	ADD_LIBRARY(cryptopp SHARED 
		${CRYPTOPP_SRCS_FIPS}
		)
	SET_TARGET_PROPERTIES(cryptopp PROPERTIES ${CRYPTOPP_COMPILE_DEFS_OPT} COMPILE_DEFINITIONS CRYPTOPP_LIBRARY_BUILD)
	IF(CRYPTOPP_LDFLAGS)
		SET_TARGET_PROPERTIES(cryptopp PROPERTIES LINK_FLAGS ${CRYPTOPP_LDFLAGS})
	ENDIF()
	TARGET_LINK_LIBRARIES(cryptopp)

	INSTALL(
		TARGETS cryptopp
		PERMISSIONS ${EXEC_PERMS}
		RUNTIME DESTINATION bin
		LIBRARY DESTINATION lib
		ARCHIVE DESTINATION lib
	)
	INSTALL(FILES 
		${CRYPTOPP_HDRS}/
		DESTINATION include
	)
ENDIF()

#########################
# Crypto++ Test
#########################
IF(CRYPTOPP_BUILD_TESTS AND CRYPTOPP_STATIC)
	SET(TEST_SRCS
		adhoc.cpp
		bench.cpp
		bench2.cpp
		datatest.cpp
		dlltest.cpp
		fipsalgt.cpp
		regtest.cpp
		test.cpp
		validat1.cpp  
		validat2.cpp  
		validat3.cpp
		fipstest.cpp 
	)
	IF(WIN32)
		SET(TEST_SRCS ${TEST_SRCS}
			bench.h
			factory.h
			validate.h
		)
	ENDIF()
	ADD_EXECUTABLE(cryptest ${TEST_SRCS})
	TARGET_LINK_LIBRARIES(cryptest ws2_32.lib cryptlib)
	FILE(COPY TestData DESTINATION . FILES_MATCHING PATTERN TestData/*)
	SET_TARGET_PROPERTIES(cryptest PROPERTIES ${CRYPTOPP_COMPILE_DEFS_OPT})
	IF(CRYPTOPP_LDFLAGS)
		SET_TARGET_PROPERTIES(cryptest PROPERTIES LINK_FLAGS ${CRYPTOPP_LDFLAGS})
	ENDIF()
ENDIF()
