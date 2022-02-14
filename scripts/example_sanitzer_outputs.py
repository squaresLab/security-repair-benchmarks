test_1 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 33410 (0x8282) encountered.
TIFFFetchNormalTag: Warning, ASCII value for tag "DocumentName" contains null byte in value; value incorrectly truncated during reading due to implementation limitations.
OJPEGSetupDecode: Warning, Depreciated and troublesome old-style JPEG compression mode, please convert to new-style JPEG compression and notify vendor of writing software.
ASAN:DEADLYSIGNAL
=================================================================
==26424==ERROR: AddressSanitizer: FPE on unknown address 0x7f218b2a4381 (pc 0x7f218b2a4381 bp 0x7ffd4c0fa6d0 sp 0x7ffd4c0fa430 T0)
    #0 0x7f218b2a4380 in OJPEGDecodeRaw /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:816:8
    #1 0x7f218b28965b in OJPEGDecode /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:791:7
    #2 0x7f218b2d1df7 in TIFFReadScanline /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_read.c:304:7
    #3 0x4f2c44 in quant /benchmarks/libtiff/bugzilla_2611/source/tools/tiffmedian.c:771:7
    #4 0x4eca7f in main /benchmarks/libtiff/bugzilla_2611/source/tools/tiffmedian.c:283:3
    #5 0x7f21899c783f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #6 0x418ba8 in _start (/benchmarks/libtiff/bugzilla_2611/source/tools/.libs/lt-tiffmedian+0x418ba8)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: FPE /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:816:8 in OJPEGDecodeRaw
==26424==ABORTING"""

test_1_json = """{
    "num_ubsan": 0,
    "num_addsan": 1,
    "addsans": [
        {
            "type": "FPE",
            "loc": ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 816, 8, "OJPEGDecodeRaw"],
            "trace": [
                ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 816, 8, "OJPEGDecodeRaw"],
                ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 791, 7, "OJPEGDecode"],
                ["tif_read.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 304, 7, "TIFFReadScanline"],
                ["tiffmedian.c", "/benchmarks/libtiff/bugzilla_2611/source/tools", 771, 7, "quant"],
                ["tiffmedian.c", "/benchmarks/libtiff/bugzilla_2611/source/tools", 283, 3, "main"]
            ]
        }
    ]
}"""

test_2 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFFetchNormalTag: Warning, IO error during reading of "YResolution"; tag ignored.
TIFFFetchNormalTag: Warning, IO error during reading of "Software"; tag ignored.
=================================================================
==16188==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60200000ee54 at pc 0x0000004f9264 bp 0x7ffd01c90710 sp 0x7ffd01c90708
READ of size 1 at 0x60200000ee54 thread T0
    #0 0x4f9263 in PSDataColorContig /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:2470:20
    #1 0x4f12a0 in PSpage /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:2347:4
    #2 0x4ed1c7 in TIFF2PS /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:1606:10
    #3 0x4eb74b in main /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:473:9
    #4 0x7fca6646083f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #5 0x4192a8 in _start (/benchmarks/libtiff/bugzilla_2633/source/tools/.libs/lt-tiff2ps+0x4192a8)

0x60200000ee54 is located 0 bytes to the right of 4-byte region [0x60200000ee50,0x60200000ee54)
allocated by thread T0 here:
    #0 0x4b93d8 in malloc (/benchmarks/libtiff/bugzilla_2633/source/tools/.libs/lt-tiff2ps+0x4b93d8)
    #1 0x7fca67d8b29c in _TIFFmalloc /benchmarks/libtiff/bugzilla_2633/source/libtiff/tif_unix.c:316:10
    #2 0x4f913e in PSDataColorContig /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:2443:29
    #3 0x4f12a0 in PSpage /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:2347:4
    #4 0x4ed1c7 in TIFF2PS /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:1606:10
    #5 0x4eb74b in main /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:473:9
    #6 0x7fca6646083f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: heap-buffer-overflow /benchmarks/libtiff/bugzilla_2633/source/tools/tiff2ps.c:2470:20 in PSDataColorContig
Shadow bytes around the buggy address:
  0x0c047fff9d70: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9d80: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9d90: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9da0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9db0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c047fff9dc0: fa fa fa fa fa fa fa fa fa fa[04]fa fa fa 00 07
  0x0c047fff9dd0: fa fa fd fa fa fa fd fa fa fa 00 fa fa fa fd fa
  0x0c047fff9de0: fa fa 00 fa fa fa fd fa fa fa 00 07 fa fa fd fd
  0x0c047fff9df0: fa fa fd fa fa fa 02 fa fa fa fd fa fa fa 00 00
  0x0c047fff9e00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c047fff9e10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==16188==ABORTING

"""

test_2_json = """
{
    "num_ubsan": 0,
    "num_addsan": 1,
    "addsans": [
        {
            "type": "heap-buffer-overflow",
            "loc": ["tiff2ps.c", "/benchmarks/libtiff/bugzilla_2633/source/tools", 2470, 20, "PSDataColorContig"],
            "trace": [
                ["tiff2ps.c", "/benchmarks/libtiff/bugzilla_2633/source/tools", 2470, 20, "PSDataColorContig"],
                ["tiff2ps.c", "/benchmarks/libtiff/bugzilla_2633/source/tools", 2347, 4, "PSpage"],
                ["tiff2ps.c", "/benchmarks/libtiff/bugzilla_2633/source/tools", 1606, 10, "TIFF2PS"],
                ["tiff2ps.c", "/benchmarks/libtiff/bugzilla_2633/source/tools", 473, 9, "main"]
            ]
        }
    ]
}
"""

test_3 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 33410 (0x8282) encountered.
TIFFFetchNormalTag: Warning, ASCII value for tag "DocumentName" contains null byte in value; value incorrectly truncated during reading due to implementation limitations.
OJPEGSetupDecode: Warning, Depreciated and troublesome old-style JPEG compression mode, please convert to new-style JPEG compression and notify vendor of writing software.
tif_ojpeg.c:816:8: runtime error: division by zero
./test: line 8:  1356 Floating point exception(core dumped) ${TEST_EXECUTION_PREFIX:-} "${PATH_BIN}" "${PATH_EXPLOIT}" foo

"""

# NOTE - need to make path thing consistant
test_3_json = """
{
    "num_ubsan": 1,
    "num_addsan": 0,
    "ubsans": [
        {
            "type": "division by zero",
            "loc": ["tif_ojpeg.c", null, 816, 8, null]
        }
    ]
}

"""

test_4 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 33410 (0x8282) encountered.
TIFFFetchNormalTag: Warning, ASCII value for tag "DocumentName" contains null byte in value; value incorrectly truncated during reading due to implementation limitations.
OJPEGSetupDecode: Warning, Depreciated and troublesome old-style JPEG compression mode, please convert to new-style JPEG compression and notify vendor of writing software.
tif_ojpeg.c:816:8: runtime error: division by zero
SUMMARY: AddressSanitizer: undefined-behavior tif_ojpeg.c:816:8 in 
ASAN:DEADLYSIGNAL
=================================================================
==8768==ERROR: AddressSanitizer: FPE on unknown address 0x7f11fea33f2c (pc 0x7f11fea33f2c bp 0x7ffdb6de1cc0 sp 0x7ffdb6de18d0 T0)
    #0 0x7f11fea33f2b in OJPEGDecodeRaw /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:816:8
    #1 0x7f11fe9f03df in OJPEGDecode /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:791:7
    #2 0x7f11fea9ff86 in TIFFReadScanline /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_read.c:304:7
    #3 0x4fe454 in quant /benchmarks/libtiff/bugzilla_2611/source/tools/tiffmedian.c:771:7
    #4 0x4ee800 in main /benchmarks/libtiff/bugzilla_2611/source/tools/tiffmedian.c:283:3
    #5 0x7f11fced383f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #6 0x418ba8 in _start (/benchmarks/libtiff/bugzilla_2611/source/tools/.libs/lt-tiffmedian+0x418ba8)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: FPE /benchmarks/libtiff/bugzilla_2611/source/libtiff/tif_ojpeg.c:816:8 in OJPEGDecodeRaw
==8768==ABORTING
"""

test_4_json = """
{
    "num_ubsan": 1,
    "ubsans": [
        {
            "type": "division by zero",
            "loc": ["tif_ojpeg.c", null, 816, 8, null]
        }
    ],
    "num_addsan": 2,
    "addsans": [
        {
            "type": "undefined-behavior",
            "loc": ["tif_ojpeg.c", null, 816, 8, null],
            "trace": []
        },
        {
            "type": "FPE",
            "loc": ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 816, 8, "OJPEGDecodeRaw"],
            "trace": [
                ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 816, 8, "OJPEGDecodeRaw"],
                ["tif_ojpeg.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 791, 7, "OJPEGDecode"],
                ["tif_read.c", "/benchmarks/libtiff/bugzilla_2611/source/libtiff", 304, 7, "TIFFReadScanline"],
                ["tiffmedian.c", "/benchmarks/libtiff/bugzilla_2611/source/tools", 771, 7, "quant"],
                ["tiffmedian.c", "/benchmarks/libtiff/bugzilla_2611/source/tools", 283, 3, "main"]
            ]
        }
    ]
}
"""

test_5 = """
=================================================================
==22146==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x60b00000accf at pc 0x7fe62c4b789e bp 0x7ffcf6de92d0 sp 0x7ffcf6de92c8
READ of size 1 at 0x60b00000accf thread T0
    #0 0x7fe62c4b789d in xmlParseAttValueComplex /benchmarks/libxml2/cve_2012_5134/source/parser.c:4079:16
    #1 0x7fe62c328fc6 in xmlParseAttValueInternal /benchmarks/libxml2/cve_2012_5134/source/parser.c:9009:12
    #2 0x7fe62c4ba1be in xmlParseAttribute2 /benchmarks/libxml2/cve_2012_5134/source/parser.c:9065:15
    #3 0x7fe62c41aec2 in xmlParseStartTag2 /benchmarks/libxml2/cve_2012_5134/source/parser.c:9223:12
    #4 0x7fe62c40ef12 in xmlParseElement__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:9910:16
    #5 0x7fe62c4487cf in xmlParseDocument__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:10666:2
    #6 0x7fe62c4afc79 in xmlDoRead /benchmarks/libxml2/cve_2012_5134/source/parser.c:15066:5
    #7 0x7fe62c4b02c1 in xmlReadFile__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:15126:13
    #8 0x502e09 in parseAndPrintFile /benchmarks/libxml2/cve_2012_5134/source/xmllint.c:2381:9
    #9 0x4fb03e in main /benchmarks/libxml2/cve_2012_5134/source/xmllint.c:3733:7
    #10 0x7fe62a9b483f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #11 0x41c068 in _start (/benchmarks/libxml2/cve_2012_5134/source/.libs/lt-xmllint+0x41c068)

0x60b00000accf is located 1 bytes to the left of 100-byte region [0x60b00000acd0,0x60b00000ad34)
allocated by thread T0 here:
    #0 0x4bc198 in malloc (/benchmarks/libxml2/cve_2012_5134/source/.libs/lt-xmllint+0x4bc198)
    #1 0x7fe62c4b2a41 in xmlParseAttValueComplex /benchmarks/libxml2/cve_2012_5134/source/parser.c:3921:23
    #2 0x7fe62c328fc6 in xmlParseAttValueInternal /benchmarks/libxml2/cve_2012_5134/source/parser.c:9009:12
    #3 0x7fe62c4ba1be in xmlParseAttribute2 /benchmarks/libxml2/cve_2012_5134/source/parser.c:9065:15
    #4 0x7fe62c41aec2 in xmlParseStartTag2 /benchmarks/libxml2/cve_2012_5134/source/parser.c:9223:12
    #5 0x7fe62c40ef12 in xmlParseElement__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:9910:16
    #6 0x7fe62c4487cf in xmlParseDocument__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:10666:2
    #7 0x7fe62c4afc79 in xmlDoRead /benchmarks/libxml2/cve_2012_5134/source/parser.c:15066:5
    #8 0x7fe62c4b02c1 in xmlReadFile__internal_alias /benchmarks/libxml2/cve_2012_5134/source/parser.c:15126:13
    #9 0x502e09 in parseAndPrintFile /benchmarks/libxml2/cve_2012_5134/source/xmllint.c:2381:9
    #10 0x4fb03e in main /benchmarks/libxml2/cve_2012_5134/source/xmllint.c:3733:7
    #11 0x7fe62a9b483f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: heap-buffer-overflow /benchmarks/libxml2/cve_2012_5134/source/parser.c:4079:16 in xmlParseAttValueComplex
Shadow bytes around the buggy address:
  0x0c167fff9540: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff9550: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff9560: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff9570: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c167fff9580: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c167fff9590: fa fa fa fa fa fa fa fa fa[fa]00 00 00 00 00 00
  0x0c167fff95a0: 00 00 00 00 00 00 04 fa fa fa fa fa fa fa fa fa
  0x0c167fff95b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 fa fa
  0x0c167fff95c0: fa fa fa fa fa fa fd fd fd fd fd fd fd fd fd fd
  0x0c167fff95d0: fd fd fd fd fa fa fa fa fa fa fa fa 00 00 00 00
  0x0c167fff95e0: 00 00 00 00 00 00 00 00 00 fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==22146==ABORTING

"""

test_5_json = """

"""

test_6 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 464 (0x1d0) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 513 (0x201) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 642 (0x282) encountered.
/benchmarks/libtiff/cve_2016_5314/exploit: Warning, Nonstandard tile length 6, convert file.
TIFFFetchNormalTag: Warning, Incompatible type for "DocumentName"; tag ignored.
PixarLogDecode: Decoding error at scanline 0, incorrect header check.
PixarLogDecode: Decoding error at scanline 0, invalid block type.
PixarLogDecode: Decoding error at scanline 0, incorrect data check.
PixarLogDecode: Decoding error at scanline 0, incorrect header check.
PixarLogDecode: Decoding error at scanline 0, invalid block type.
PixarLogDecode: Decoding error at scanline 0, incorrect data check.
PixarLogDecode: Decoding error at scanline 0, invalid block type.
PixarLogDecode: Decoding error at scanline 0, invalid distance code.
PixarLogDecode: Decoding error at scanline 0, incorrect header check.
PixarLogDecode: Decoding error at scanline 0, invalid block type.
=================================================================
==29380==ERROR: AddressSanitizer: attempting free on address which was not malloc()-ed: 0x61500000fd00 in thread T0
    #0 0x4b8c90 in __interceptor_cfree.localalias.0 (/benchmarks/libtiff/cve_2016_5314/source/tools/.libs/lt-rgb2ycbcr+0x4b8c90)
    #1 0x7fec94f34634 in _TIFFfree /benchmarks/libtiff/cve_2016_5314/source/libtiff/tif_unix.c:322:2
    #2 0x7fec94e9aea5 in PixarLogCleanup /benchmarks/libtiff/cve_2016_5314/source/libtiff/tif_pixarlog.c:1256:17
    #3 0x7fec94c6a677 in TIFFReadDirectory /benchmarks/libtiff/cve_2016_5314/source/libtiff/tif_dirread.c:3412:2
    #4 0x4eb218 in main /benchmarks/libtiff/cve_2016_5314/source/tools/rgb2ycbcr.c:132:13
    #5 0x7fec9331d83f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #6 0x418ce8 in _start (/benchmarks/libtiff/cve_2016_5314/source/tools/.libs/lt-rgb2ycbcr+0x418ce8)

0x61500000fd00 is located 112 bytes inside of 1970632053-byte region [0x61500000fc90,0x615075767205)
ASAN:DEADLYSIGNAL
AddressSanitizer: nested bug in the same thread, aborting.

"""

test_6_json = """
{
    "num_ubsan": 0,
    "num_addsan": 1,
    "addsans": [
        {
            "type": "attempting free on address which was not malloc()-ed",
            "loc": ["tif_unix.c", "/benchmarks/libtiff/cve_2016_5314/source/libtiff", 322, 2, "_TIFFfree"],
            "trace": [
                ["tif_unix.c", "/benchmarks/libtiff/cve_2016_5314/source/libtiff", 322, 2, "_TIFFfree"],
                ["tif_pixarlog.c", "/benchmarks/libtiff/cve_2016_5314/source/libtiff", 1256, 17, "PixarLogCleanup"],
                ["tif_dirread.c", "/benchmarks/libtiff/cve_2016_5314/source/libtiff", 3412, 2, "TIFFReadDirectory"],
                ["rgb2ycbcr.c", "/benchmarks/libtiff/cve_2016_5314/source/tools", 132, 13, "main"]
            ]
        }
    ]
}
"""

test_7 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFFetchNormalTag: Warning, ASCII value for tag "DocumentName" does not end in null byte.
TIFFFetchNormalTag: Warning, Sanity check on size of "Software" value failed; tag ignored.
JPEGLib: Not a JPEG file: starts with 0x01 0x01.
JPEGSetupDecode: Bogus JPEGTables field.
tif_jpeg.c:1646:19: runtime error: shift exponent 136 is too large for 64-bit type 'long'
SUMMARY: AddressSanitizer: undefined-behavior tif_jpeg.c:1646:19 in 
JPEGSetupEncode: BitsPerSample 136 not allowed for JPEG.
foo: Error, can't write strip 0.
TIFFWriteDirectoryTagCheckedRational: Not-a-number value is illegal.

"""

test_7_json = """
{
    "num_ubsan": 1,
    "ubsans": [
        {
            "type": "shift exponent 136 is too large for 64-bit type 'long'",
            "loc": ["tif_jpeg.c", null, 1646, 19, null]
        }
    ],
    "num_addsan": 1,
    "addsans": [
        {
            "type": "undefined-behavior",
            "loc": ["tif_jpeg.c", null, 1646, 19, null],
            "trace": []
        }
    ]
}
"""

test_8 = """=================================================================
==31469==ERROR: AddressSanitizer: memcpy-param-overlap: memory ranges [0x631000015003,0x631000015007) and [0x631000015000, 0x631000015004) overlap
    #0 0x4a3049 in __asan_memcpy (/benchmarks/coreutils/gnubug_26545/source/src/shred+0x4a3049)
    #1 0x4f421b in fillpattern /benchmarks/coreutils/gnubug_26545/source/src/shred.c:293:5
    #2 0x4f16c6 in dopass /benchmarks/coreutils/gnubug_26545/source/src/shred.c:480:7
    #3 0x4efffd in do_wipefd /benchmarks/coreutils/gnubug_26545/source/src/shred.c:967:17
    #4 0x4ecee7 in wipefile /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1191:8
    #5 0x4ec906 in main /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1317:17
    #6 0x7f16ac53183f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #7 0x419378 in _start (/benchmarks/coreutils/gnubug_26545/source/src/shred+0x419378)

0x631000015003 is located 2051 bytes inside of 69633-byte region [0x631000014800,0x631000025801)
allocated by thread T0 here:
    #0 0x4b94a8 in __interceptor_malloc (/benchmarks/coreutils/gnubug_26545/source/src/shred+0x4b94a8)
    #1 0x511f54 in xmalloc /benchmarks/coreutils/gnubug_26545/source/lib/xmalloc.c:41:13
    #2 0x4f13e3 in dopass /benchmarks/coreutils/gnubug_26545/source/src/shred.c:451:28
    #3 0x4efffd in do_wipefd /benchmarks/coreutils/gnubug_26545/source/src/shred.c:967:17
    #4 0x4ecee7 in wipefile /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1191:8
    #5 0x4ec906 in main /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1317:17
    #6 0x7f16ac53183f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

0x631000015000 is located 2048 bytes inside of 69633-byte region [0x631000014800,0x631000025801)
allocated by thread T0 here:
    #0 0x4b94a8 in __interceptor_malloc (/benchmarks/coreutils/gnubug_26545/source/src/shred+0x4b94a8)
    #1 0x511f54 in xmalloc /benchmarks/coreutils/gnubug_26545/source/lib/xmalloc.c:41:13
    #2 0x4f13e3 in dopass /benchmarks/coreutils/gnubug_26545/source/src/shred.c:451:28
    #3 0x4efffd in do_wipefd /benchmarks/coreutils/gnubug_26545/source/src/shred.c:967:17
    #4 0x4ecee7 in wipefile /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1191:8
    #5 0x4ec906 in main /benchmarks/coreutils/gnubug_26545/source/src/shred.c:1317:17
    #6 0x7f16ac53183f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: memcpy-param-overlap (/benchmarks/coreutils/gnubug_26545/source/src/shred+0x4a3049) in __asan_memcpy
==31469==ABORTING

"""

test_8_json = """

"""

test_9 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 2583 (0xa17) encountered.
TIFFFetchNormalTag: Warning, Sanity check on size of "DocumentName" value failed; tag ignored.
TIFFFetchNormalTag: Warning, Sanity check on size of "Tag 2583" value failed; tag ignored.
TIFFFetchNormalTag: Warning, incorrect count for field "PageNumber", expected 2, got 2.
TIFFFetchNormalTag: Warning, Incompatible type for "Software"; tag ignored.
TIFFReadDirectory: Warning, TIFF directory is missing required "StripByteCounts" field, calculating from imagelength.
TIFFFillStrip: Read error on strip 0; got 18446494488865014140 bytes, expected 2.
tif_dirwrite.c:980:26: runtime error: value 65280 is outside the range of representable values of type 'short'
SUMMARY: AddressSanitizer: undefined-behavior tif_dirwrite.c:980:26 in 
tif_dirwrite.c:2110:26: runtime error: value -nan is outside the range of representable values of type 'unsigned int'
SUMMARY: AddressSanitizer: undefined-behavior tif_dirwrite.c:2110:26 in 
tif_dirwrite.c:2123:8: runtime error: value -nan is outside the range of representable values of type 'unsigned int'
SUMMARY: AddressSanitizer: undefined-behavior tif_dirwrite.c:2123:8 in 
TIFFFetchDirectory: Can not read TIFF directory count.
TIFFReadDirectory: Failed to read directory at offset 7738144477487657827.

"""

test_9_json = """
{
    "num_ubsan": 3,
    "ubsans": [
        {
            "type": "value 65280 is outside the range of representable values of type 'short'",
            "loc": ["tif_dirwrite.c", null, 980, 26, null]
        }, 
        {
            "type": "value -nan is outside the range of representable values of type 'unsigned int'",
            "loc": ["tif_dirwrite.c", null, 2110, 26, null]
        },
        {
            "type": "value -nan is outside the range of representable values of type 'unsigned int'",
            "loc": ["tif_dirwrite.c", null, 2123, 8, null]
        }
    ],
    "num_addsan": 3,
    "addsans": [
        {
            "type": "undefined-behavior",
            "loc": ["tif_dirwrite.c", null, 980, 26, null],
            "trace": []
        },
        {
            "type": "undefined-behavior",
            "loc": ["tif_dirwrite.c", null, 2110, 26, null],
            "trace": []
        },
        {
            "type": "undefined-behavior",
            "loc": ["tif_dirwrite.c", null, 2123, 8, null],
            "trace": []
        }
    ]
}

"""

test_10 = """/benchmarks/libxml2/cve_2017_5969/exploit:15: parser error : xmlParseElementChildrenContentDecl : '|' expected
  <!ELEMENT child4 (a, (b|cp+, (a|d)?, (e|f)* )?>
                             ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : Input is not proper UTF-8, indicate encoding !
Bytes: 0xA5 0x62 0x29 0x2A
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : ContentDecl : ',' '|' or ')' expected
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : ContentDecl : ',' '|' or ')' expected
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : expected '>'
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : internal error: xmlParseInternalSubset: error detected in Markup declaration

  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : DOCTYPE improperly terminated
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
/benchmarks/libxml2/cve_2017_5969/exploit:17: parser error : Start tag expected, '<' not found
  <!ELEMENT child5_1 ( (a•b)* | (c,b)? | (d,a)+ | ((e|f),b,c) )* >
                         ^
valid.c:1181:24: runtime error: member access within null pointer of type 'struct _xmlElementContent'
SUMMARY: AddressSanitizer: undefined-behavior valid.c:1181:24 in 
valid.c:1181:24: runtime error: load of null pointer of type 'xmlElementContentType'
SUMMARY: AddressSanitizer: undefined-behavior valid.c:1181:24 in 
ASAN:DEADLYSIGNAL
=================================================================
==27092==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000000 (pc 0x7fb74d91bd3b bp 0x7fffa85b3d10 sp 0x7fffa85b3a60 T0)
    #0 0x7fb74d91bd3a in xmlDumpElementContent /benchmarks/libxml2/cve_2017_5969/source/valid.c:1181:29
    #1 0x7fb74d91ba60 in xmlDumpElementContent /benchmarks/libxml2/cve_2017_5969/source/valid.c:1177:3
    #2 0x7fb74d91b191 in xmlDumpElementDecl__internal_alias /benchmarks/libxml2/cve_2017_5969/source/valid.c:1708:6
    #3 0x7fb74e20e185 in xmlBufDumpElementDecl /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:501:5
    #4 0x7fb74e214c9a in xmlNodeDumpOutputInternal /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:939:9
    #5 0x7fb74e2338ed in xmlNodeListDumpOutput /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:825:9
    #6 0x7fb74e232a04 in xmlDtdDumpOutput /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:749:5
    #7 0x7fb74e214897 in xmlNodeDumpOutputInternal /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:931:9
    #8 0x7fb74e213679 in xmlDocContentDumpOutput /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:1234:7
    #9 0x7fb74e210355 in xmlSaveDoc__internal_alias /benchmarks/libxml2/cve_2017_5969/source/xmlsave.c:1936:9
    #10 0x504e5a in parseAndPrintFile /benchmarks/libxml2/cve_2017_5969/source/xmllint.c:2712:11
    #11 0x4fb0d8 in main /benchmarks/libxml2/cve_2017_5969/source/xmllint.c:3767:7
    #12 0x7fb74bcb483f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #13 0x41c068 in _start (/benchmarks/libxml2/cve_2017_5969/source/.libs/lt-xmllint+0x41c068)

AddressSanitizer can not provide additional info.
SUMMARY: AddressSanitizer: SEGV /benchmarks/libxml2/cve_2017_5969/source/valid.c:1181:29 in xmlDumpElementContent
==27092==ABORTING

"""

test_10_json = """

"""

test_11 = """/benchmarks/libxml2/cve_2016_1838/exploit:1: namespace error : Namespace prefix a-340282366920938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867209384634725979468672093846347259794686720938463472597946867261d on a is not defined
63472597946867209384634725979468672093846347259794686720938463472597946867261d:a
                                                                               ^
/benchmarks/libxml2/cve_2016_1838/exploit:1: parser error : internal error: Huge input lookup
=================================================================
==12972==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x6290000051ff at pc 0x7f6fe9f0cc37 bp 0x7ffdd3eaa930 sp 0x7ffdd3eaa928
READ of size 1 at 0x6290000051ff thread T0
    #0 0x7f6fe9f0cc36 in xmlParserPrintFileContextInternal /benchmarks/libxml2/cve_2016_1838/source/error.c:192:6
    #1 0x7f6fe9f1b190 in xmlReportError /benchmarks/libxml2/cve_2016_1838/source/error.c:406:9
    #2 0x7f6fe9f124ff in __xmlRaiseError /benchmarks/libxml2/cve_2016_1838/source/error.c:633:2
    #3 0x7f6fe9f65bae in xmlFatalErr /benchmarks/libxml2/cve_2016_1838/source/parser.c:542:5
    #4 0x7f6fe9f5d719 in xmlGROW /benchmarks/libxml2/cve_2016_1838/source/parser.c:2079:9
    #5 0x7f6fea09d8f5 in xmlParseEndTag2 /benchmarks/libxml2/cve_2016_1838/source/parser.c:9855:5
    #6 0x7f6fea0854c2 in xmlParseElement__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parser.c:10247:2
    #7 0x7f6fea0bd130 in xmlParseDocument__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parser.c:10921:2
    #8 0x7f6fea126329 in xmlDoRead /benchmarks/libxml2/cve_2016_1838/source/parser.c:15400:5
    #9 0x7f6fea126976 in xmlReadFile__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parser.c:15462:13
    #10 0x50318a in parseAndPrintFile /benchmarks/libxml2/cve_2016_1838/source/xmllint.c:2408:9
    #11 0x4fb0d8 in main /benchmarks/libxml2/cve_2016_1838/source/xmllint.c:3767:7
    #12 0x7f6fe861283f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #13 0x41c068 in _start (/benchmarks/libxml2/cve_2016_1838/source/.libs/lt-xmllint+0x41c068)

0x6290000051ff is located 1 bytes to the left of 16384-byte region [0x629000005200,0x629000009200)
allocated by thread T0 here:
    #0 0x4bc198 in malloc (/benchmarks/libxml2/cve_2016_1838/source/.libs/lt-xmllint+0x4bc198)
    #1 0x7f6feabcb72e in xz_head /benchmarks/libxml2/cve_2016_1838/source/xzlib.c:396:22
    #2 0x7f6feabc517f in xz_make /benchmarks/libxml2/cve_2016_1838/source/xzlib.c:639:13
    #3 0x7f6feabc2f44 in __libxml2_xzread /benchmarks/libxml2/cve_2016_1838/source/xzlib.c:743:17
    #4 0x7f6fea211ef2 in xmlXzfileRead /benchmarks/libxml2/cve_2016_1838/source/xmlIO.c:1435:11
    #5 0x7f6fea21dcf6 in xmlParserInputBufferGrow__internal_alias /benchmarks/libxml2/cve_2016_1838/source/xmlIO.c:3337:8
    #6 0x7f6fe9f1ea52 in xmlParserInputGrow__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parserInternals.c:320:8
    #7 0x7f6fe9f5d812 in xmlGROW /benchmarks/libxml2/cve_2016_1838/source/parser.c:2083:5
    #8 0x7f6fea0b426e in xmlParseDocument__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parser.c:10798:5
    #9 0x7f6fea126329 in xmlDoRead /benchmarks/libxml2/cve_2016_1838/source/parser.c:15400:5
    #10 0x7f6fea126976 in xmlReadFile__internal_alias /benchmarks/libxml2/cve_2016_1838/source/parser.c:15462:13
    #11 0x50318a in parseAndPrintFile /benchmarks/libxml2/cve_2016_1838/source/xmllint.c:2408:9
    #12 0x4fb0d8 in main /benchmarks/libxml2/cve_2016_1838/source/xmllint.c:3767:7
    #13 0x7f6fe861283f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: heap-buffer-overflow /benchmarks/libxml2/cve_2016_1838/source/error.c:192:6 in xmlParserPrintFileContextInternal
Shadow bytes around the buggy address:
  0x0c527fff89e0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff89f0: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff8a00: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff8a10: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c527fff8a20: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c527fff8a30: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]
  0x0c527fff8a40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff8a50: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff8a60: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff8a70: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c527fff8a80: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==12972==ABORTING


"""

test_11_json = """

"""

test_12 = """
TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 32768 (0x8000) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 58907 (0xe61b) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 4096 (0x1000) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 5971 (0x1753) encountered.
TIFFFetchNormalTag: Warning, IO error during reading of "Tag 32768"; tag ignored.
TIFFFetchNormalTag: Warning, IO error during reading of "DocumentName"; tag ignored.
TIFFFetchNormalTag: Warning, IO error during reading of "XResolution"; tag ignored.
TIFFReadDirectory: Warning, Incorrect count for "ColorMap"; tag ignored.
TIFFFetchNormalTag: Warning, IO error during reading of "Software"; tag ignored.
TIFFFetchNormalTag: Warning, Sanity check on size of "Tag 5971" value failed; tag ignored.
TIFFNumberOfDirectories: Directory count exceeded 65535 limit, giving up on counting..
loadImage: Image lacks Photometric interpreation tag.
TIFFFillStrip: Read error on strip 0; got 327 bytes, expected 786474.
: Strip 1: read 18446744073709551615 bytes, strip size 2048.
TIFFFillStrip: Invalid strip byte count 0, strip 1.
: Strip 2: read 18446744073709551615 bytes, strip size 2048.
TIFFFillStrip: Read error on strip 2; got 335 bytes, expected 1179648.
: Strip 3: read 18446744073709551615 bytes, strip size 2048.
TIFFFillStrip: Read error on strip 3; got 335 bytes, expected 196864.
: Strip 4: read 18446744073709551615 bytes, strip size 2048.
=================================================================
==21786==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x62d00000a3fc at pc 0x7fc3d1192047 bp 0x7ffc4058bfe0 sp 0x7ffc4058bfd8
WRITE of size 1 at 0x62d00000a3fc thread T0
    #0 0x7fc3d1192046 in NeXTDecode /benchmarks/libtiff/cve_2016_10272/source/libtiff/tif_next.c:64:9
    #1 0x7fc3d11de6be in TIFFReadEncodedStrip /benchmarks/libtiff/cve_2016_10272/source/libtiff/tif_read.c:380:6
    #2 0x509ab1 in readContigStripsIntoBuffer /benchmarks/libtiff/cve_2016_10272/source/tools/tiffcrop.c:3689:30
    #3 0x4f778f in loadImage /benchmarks/libtiff/cve_2016_10272/source/tools/tiffcrop.c:6167:13
    #4 0x4f1d5d in main /benchmarks/libtiff/cve_2016_10272/source/tools/tiffcrop.c:2345:11
    #5 0x7fc3cf8d283f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #6 0x419398 in _start (/benchmarks/libtiff/cve_2016_10272/source/tools/.libs/lt-tiffcrop+0x419398)

0x62d00000a3fc is located 4 bytes to the left of 32771-byte region [0x62d00000a400,0x62d000012403)
allocated by thread T0 here:
    #0 0x4b94c8 in malloc (/benchmarks/libtiff/cve_2016_10272/source/tools/.libs/lt-tiffcrop+0x4b94c8)
    #1 0x7fc3d11fcc0c in _TIFFmalloc /benchmarks/libtiff/cve_2016_10272/source/libtiff/tif_unix.c:316:10
    #2 0x4f744e in loadImage /benchmarks/libtiff/cve_2016_10272/source/tools/tiffcrop.c:6125:34
    #3 0x4f1d5d in main /benchmarks/libtiff/cve_2016_10272/source/tools/tiffcrop.c:2345:11
    #4 0x7fc3cf8d283f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: heap-buffer-overflow /benchmarks/libtiff/cve_2016_10272/source/libtiff/tif_next.c:64:9 in NeXTDecode
Shadow bytes around the buggy address:
  0x0c5a7fff9420: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff9430: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff9440: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff9450: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c5a7fff9460: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
=>0x0c5a7fff9470: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa[fa]
  0x0c5a7fff9480: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff9490: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff94a0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff94b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c5a7fff94c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==21786==ABORTING

"""

test_12_json = """

"""

test_13 = """
/benchmarks/libxml2/cve_2016_1839/exploit:1: HTML parser error : htmlParseEntityRef: expecting ';'
&:&::&:::::jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
  ^
/benchmarks/libxml2/cve_2016_1839/exploit:1: HTML parser error : htmlParseEntityRef: expecting ';'
&:&::&:::::jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj
     ^
=================================================================
==20743==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x631000010810 at pc 0x0000004a5ecd bp 0x7ffd29c662e0 sp 0x7ffd29c65a90
READ of size 73661 at 0x631000010810 thread T0
    #0 0x4a5ecc in __asan_memcpy (/benchmarks/libxml2/cve_2016_1839/source/.libs/lt-xmllint+0x4a5ecc)
    #1 0x7fb71e11dce3 in xmlDictAddString /benchmarks/libxml2/cve_2016_1839/source/dict.c:285:5
    #2 0x7fb71e11cdc0 in xmlDictLookup__internal_alias /benchmarks/libxml2/cve_2016_1839/source/dict.c:926:11
    #3 0x7fb71de4d2e8 in htmlParseNameComplex /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2517:12
    #4 0x7fb71de29324 in htmlParseName /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2483:12
    #5 0x7fb71de28390 in htmlParseEntityRef__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2682:16
    #6 0x7fb71de5c8ce in htmlParseReference /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4044:8
    #7 0x7fb71de35378 in htmlParseContentInternal /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4619:3
    #8 0x7fb71de3790b in htmlParseDocument__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4769:5
    #9 0x7fb71de4ba53 in htmlDoRead /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:6741:5
    #10 0x7fb71de4bc9b in htmlReadFile__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:6799:13
    #11 0x4f6d5e in parseAndPrintFile /benchmarks/libxml2/cve_2016_1839/source/xmllint.c:2255:8
    #12 0x4f29ee in main /benchmarks/libxml2/cve_2016_1839/source/xmllint.c:3767:7
    #13 0x7fb71c8a683f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #14 0x41c068 in _start (/benchmarks/libxml2/cve_2016_1839/source/.libs/lt-xmllint+0x41c068)

0x631000010810 is located 0 bytes to the right of 65552-byte region [0x631000000800,0x631000010810)
allocated by thread T0 here:
    #0 0x4bc518 in realloc (/benchmarks/libxml2/cve_2016_1839/source/.libs/lt-xmllint+0x4bc518)
    #1 0x7fb71df6e3a5 in xmlBufGrowInternal /benchmarks/libxml2/cve_2016_1839/source/buf.c:486:23
    #2 0x7fb71df6d8f2 in xmlBufGrow /benchmarks/libxml2/cve_2016_1839/source/buf.c:515:11
    #3 0x7fb71ddd2b37 in xmlParserInputBufferGrow__internal_alias /benchmarks/libxml2/cve_2016_1839/source/xmlIO.c:3326:9
    #4 0x7fb71dcb8fc8 in xmlParserInputGrow__internal_alias /benchmarks/libxml2/cve_2016_1839/source/parserInternals.c:320:8
    #5 0x7fb71de4cdc1 in htmlParseNameComplex /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2511:6
    #6 0x7fb71de29324 in htmlParseName /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2483:12
    #7 0x7fb71de28390 in htmlParseEntityRef__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:2682:16
    #8 0x7fb71de5c8ce in htmlParseReference /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4044:8
    #9 0x7fb71de35378 in htmlParseContentInternal /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4619:3
    #10 0x7fb71de3790b in htmlParseDocument__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:4769:5
    #11 0x7fb71de4ba53 in htmlDoRead /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:6741:5
    #12 0x7fb71de4bc9b in htmlReadFile__internal_alias /benchmarks/libxml2/cve_2016_1839/source/HTMLparser.c:6799:13
    #13 0x4f6d5e in parseAndPrintFile /benchmarks/libxml2/cve_2016_1839/source/xmllint.c:2255:8
    #14 0x4f29ee in main /benchmarks/libxml2/cve_2016_1839/source/xmllint.c:3767:7
    #15 0x7fb71c8a683f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)

SUMMARY: AddressSanitizer: heap-buffer-overflow (/benchmarks/libxml2/cve_2016_1839/source/.libs/lt-xmllint+0x4a5ecc) in __asan_memcpy
Shadow bytes around the buggy address:
  0x0c627fffa0b0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c627fffa0c0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c627fffa0d0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c627fffa0e0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x0c627fffa0f0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
=>0x0c627fffa100: 00 00[fa]fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c627fffa110: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c627fffa120: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c627fffa130: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c627fffa140: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
  0x0c627fffa150: fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa fa
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==20743==ABORTING"""

test_13_json = """

"""

test_14 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
/benchmarks/libtiff/cve_2016_5321/exploit: Warning, Nonstandard tile length 1, convert file.
TIFFReadDirectory: Warning, Unknown field with tag 406 (0x196) encountered.
TIFFFetchNormalTag: Warning, ASCII value for tag "DocumentName" contains null byte in value; value incorrectly truncated during reading due to implementation limitations.
TIFFFetchNormalTag: Warning, IO error during reading of "YResolution"; tag ignored.
TIFFFetchNormalTag: Warning, incorrect count for field "PageNumber", expected 2, got 514.
TIFFReadDirectory: Warning, TIFF directory is missing required "StripByteCounts" field, calculating from imagelength.
TIFFAdvanceDirectory: Error fetching directory count.
tiffcrop.c:994:28: runtime error: index 8 out of bounds for type 'unsigned char *[8]'
SUMMARY: AddressSanitizer: undefined-behavior tiffcrop.c:994:28 in 
=================================================================
==25767==ERROR: AddressSanitizer: stack-buffer-overflow on address 0x7ffd5967efa0 at pc 0x000000535970 bp 0x7ffd5967ef30 sp 0x7ffd5967ef28
READ of size 8 at 0x7ffd5967efa0 thread T0
    #0 0x53596f in readSeparateTilesIntoBuffer /benchmarks/libtiff/cve_2016_5321/source/tools/tiffcrop.c:994:28
    #1 0x504d7f in loadImage /benchmarks/libtiff/cve_2016_5321/source/tools/tiffcrop.c:6079:11
    #2 0x4f9442 in main /benchmarks/libtiff/cve_2016_5321/source/tools/tiffcrop.c:2278:11
    #3 0x7f95d99e783f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x2083f)
    #4 0x419398 in _start (/benchmarks/libtiff/cve_2016_5321/source/tools/.libs/lt-tiffcrop+0x419398)

Address 0x7ffd5967efa0 is located in stack of thread T0 at offset 96 in frame
    #0 0x53511f in readSeparateTilesIntoBuffer /benchmarks/libtiff/cve_2016_5321/source/tools/tiffcrop.c:955

  This frame has 1 object(s):
    [32, 96) 'srcbuffs' <== Memory access at offset 96 overflows this variable
HINT: this may be a false positive if your program uses some custom stack unwind mechanism or swapcontext
      (longjmp and C++ exceptions *are* supported)
SUMMARY: AddressSanitizer: stack-buffer-overflow /benchmarks/libtiff/cve_2016_5321/source/tools/tiffcrop.c:994:28 in readSeparateTilesIntoBuffer
Shadow bytes around the buggy address:
  0x10002b2c7da0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7db0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7dc0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7dd0: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7de0: 00 00 00 00 00 00 00 00 f1 f1 f1 f1 00 00 00 00
=>0x10002b2c7df0: 00 00 00 00[f3]f3 f3 f3 00 00 00 00 00 00 00 00
  0x10002b2c7e00: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7e10: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7e20: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7e30: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
  0x10002b2c7e40: 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00
Shadow byte legend (one shadow byte represents 8 application bytes):
  Addressable:           00
  Partially addressable: 01 02 03 04 05 06 07 
  Heap left redzone:       fa
  Heap right redzone:      fb
  Freed heap region:       fd
  Stack left redzone:      f1
  Stack mid redzone:       f2
  Stack right redzone:     f3
  Stack partial redzone:   f4
  Stack after return:      f5
  Stack use after scope:   f8
  Global redzone:          f9
  Global init order:       f6
  Poisoned by user:        f7
  Container overflow:      fc
  Array cookie:            ac
  Intra object redzone:    bb
  ASan internal:           fe
  Left alloca redzone:     ca
  Right alloca redzone:    cb
==25767==ABORTING


"""

test_14_json = """

"""


test_15 = """TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 33537 (0x8301) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 57345 (0xe001) encountered.
TIFFFetchNormalTag: Warning, IO error during reading of "XResolution"; tag ignored.
TIFFFetchNormalTag: Warning, incorrect count for field "PageNumber", expected 2, got 8388610.
TIFFFetchNormalTag: Warning, IO error during reading of "WhitePoint"; tag ignored.
TIFFFetchNormalTag: Warning, IO error during reading of "PrimaryChromaticities"; tag ignored.
TIFFReadDirectory: Warning, Bogus "StripByteCounts" field, ignoring and calculating from imagelength.
tif_dirwrite.c:994:26: runtime error: value -115 is outside the range of representable values of type 'unsigned char'
SUMMARY: AddressSanitizer: undefined-behavior tif_dirwrite.c:994:26 in 
TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 33537 (0x8301) encountered.
/benchmarks/libtiff/cve_2017_7600/exploit: Warning, Nonstandard tile length 7, convert file.
TIFFReadDirectory: Warning, Unknown field with tag 63 (0x3f) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 1 (0x1) encountered.
TIFFReadDirectory: Warning, Unknown field with tag 2 (0x2) encountered.
TIFFFetchNormalTag: Warning, Incorrect count for "XResolution"; tag ignored.
TIFFReadDirectory: Warning, Bogus "StripByteCounts" field, ignoring and calculating from imagelength.
/benchmarks/libtiff/cve_2017_7600/exploit: Error, cannot handle BitsPerSample that is not a multiple of 8."""

test_15_json = """

"""

test_16 = """
TIFFReadDirectoryCheckOrder: Warning, Invalid TIFF directory; tags are not sorted in ascending order.
TIFFReadDirectory: Warning, Unknown field with tag 2583 (0xa17) encountered.
TIFFFetchNormalTag: Warning, Sanity check on size of "DocumentName" value failed; tag ignored.
TIFFFetchNormalTag: Warning, Sanity check on size of "Tag 2583" value failed; tag ignored.
TIFFFetchNormalTag: Warning, incorrect count for field "PageNumber", expected 2, got 2.
TIFFFetchNormalTag: Warning, Incompatible type for "Software"; tag ignored.
TIFFReadDirectory: Warning, TIFF directory is missing required "StripByteCounts" field, calculating from imagelength.
TIFFFillStrip: Read error on strip 0; got 18446494488865014140 bytes, expected 2.
tif_dirwrite.c:980:26: runtime error: value 65280 is outside the range of representable values of type 'short'
tif_dirwrite.c:2110:26: runtime error: value -nan is outside the range of representable values of type 'unsigned int'
tif_dirwrite.c:2123:8: runtime error: value -nan is outside the range of representable values of type 'unsigned int'
TIFFFetchDirectory: Can not read TIFF directory count.
TIFFReadDirectory: Failed to read directory at offset 7738144477487657827.
"""

test_16_json = """

"""

