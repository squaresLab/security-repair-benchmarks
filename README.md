Security Repair Benchmark - Overview for Red Team Use
=====================================================

**Author:** Chris Timperley <https://github.com/ChrisTimperley>

This project provides a reusable and reproducible infrastructure for evaluating C/C++ security vulnerability
repair techniques. In particular, it can be used to evaluate both a baseline approach: *Baseline Darjeeling*
as well as a future improved *Darjeeling++*. To enable this evaluation, this project consists of Dockerized 
repair tools and bug benchmarks via separate Docker images for individual bug scenarios.

Out of the box, we provide Dockerized versions of bugs in the VulnLoc benchmark set. We also provide
infrastructure for running *Baseline Darjeeling* on a subset of the vulnerabilities in VulLoc. 

In this documentation, we provide instructions for installing the Dockerized bug versions, installing
Darjeeling, running Darjeeling on Dockerized bugs, and modifying scenarios.


Installation 
-------------

We provide detailed instructions on getting *Baseline Darjeeling* up and running on the bugs in this
benchmark set [here](https://github.com/squaresLab/security-repair-benchmarks/blob/aflr_demo_12_2021/docs/darjeeling_from_scratch.md).

**Beware that this installation will take a considerable amount of time (1-3 hours depending on hardware), memory (16 GB is a minimum), and disk space
(tens of GBs) to build for the first time.**
Subsequent builds will be faster since image caching can be used.

We note that we currently provide support for Darjeeling to run on a subset of bug scenarios from the following projects in the VulnLoc becnhmarks (found in `bugs/vulnloc`). 
* libtiff
* libxml2
* coreutils
* binutils

More details about the specific bug scenarios we currently support with darjeeling can be found [here](https://github.com/squaresLab/security-repair-benchmarks/blob/aflr_demo_12_2021/docs/supported_bug_scenarios.md)


Bug Scenario Format
-------------------

Each bug scenario within this benchmark is given its own directory (e.g., `/benchmarks/vulnloc/binutils/cve_2017_14745`),
which provides the files necessary to perform repair on that bug using a variety of tools.
Below is a brief description of the files that MUST be included in each bug scenario directory:

* `bug.json` provides several details about the bug as well as tool-specific configuration
  options that should be used when attempting to repair it.
* `test` provides a script for executing the single failing test (i.e., payload) for the bug
  scenario. The script takes a single, optional argument, providing the absolute path of the binary
  that should be used to run the test. (This is useful in cases where a repaired binary is created in
  a different location to the original binary.) If no argument is provided, the script will use the
  original binary to perform the test.
* `clean` (equivalent to `make clean`) removes any compiled binaries, objects, etc. This
  is useful for recompiling the program with coverage instrumentation enabled (e.g., when performing
  repair with Darjeeling).
* `prebuild` (similar to `./configure`) appropriately configures the project. Note that
  this script requires that a `REPAIR_TOOL` environment variable is set, stating the repair tool,
  if any, that is being used in conjunction with the code. This feature is used to compile the program
  in slightly different ways according to the assumptions of various tools. To build the program without
  targeting any specific tool, you can just pass in `REPAIR_TOOL=none`. (E.g., `REPAIR_TOOL=none ./prebuild`.)
* `build` (similar to `make`) builds the project. As with `prebuild`, this step requires
  that the `REPAIR_TOOL` environment variable be appropriately set.


### File Format: bug.json

Below is an example of a `bug.json` file for `libtiff/cve_2016_10092`.

```json
{
  "subject": "libtiff",
  "name": "cve_2016_10092",
  "binary": "dbuild/tools/.libs/tiffcrop",
  "fbinary": "fbuild/tools/.libs/tiffcrop",
  "options": {
    "darjeeling": {
      "gcovr-build-subdir": "dbuild/tools",
      "gcovr-src-subdir":"",
      "coverage-files": [
       { "filename": "tools/tiffcrop.c", "line": 2177}
      ]
    },
    "extractfix": {
      "bug-type": "buffer_overflow",
      "binary": {
        "name": "tiffcrop",
        "path": "dbuild/tools/tiffcrop"
      },
      "lowfat": {
        "CFLAGS": "-fsanitize=lowfat -mllvm -lowfat-symbolize -lstlimpl"
      }
    },
    "hifix": {
      "linker-options": "/benchmarks/libtiff/cve_2016_10092/source/libtiff/.libs/libtiff.a -ljpeg -llzma -lm -ljbig -lz"
    }
  }
}
```

Here is a brief description of the most relevant fields in the above file:

* `subject` gives the name of the project/program that the bug occurs in (e.g., libtiff, coreutils)
* `name` gives the name of the bug, usually based on its CVE or issue number (e.g., cve_2016_10092). This is also the name of the docker container for this specific scenario, so it should match the name of the generated
docker container (see the Makefile for each project/program).
* `binary` specifies the path of the affected binary, relative to the root of the `source`
  directory for the bug that is used by darjeeling when generating coverage.
* `fbinary` specifies the path of the affected binary, relative to the root of the `source`
  directory for the bug for the failing build. That is, this is the binary that exposes the
  exploit for this bug. This directory is often different from `binary` because the build to expose the exploit is often not compatible with the build darjeeling uses to generate coverage information.
* `options` provides tool-specific options for repairing the bug.

Here is a description of darjeeling specific fields in `bug.json`:

* `gcovr-build-subdir`: This is the subdirectory where for the coverage build. `binary` from above should be 
  somewhere in this directory.
* `gcovr-src-subdir`: This is the source directory for the project source, relevant to the root of the 
  `source` directory for the bug,
* `coverage-files`: This gives information to allow darjeeling to still collect coverage information even when the program crashes. This property takes a list where each entry specifies the particular line in each file where coverage instrumentation should be added.


Troubleshooting and Questions
-----------------------------

### How does Darjeeling obtain coverage?

Darjeeling recompiles the program with the appropriate `--coverage` flags to allow line-level coverage to be collected via `gcov`.
(More specifically, we use `gcovr` under the hood to make life a little easier.)
A problem with this approach is that if the program abruptly terminates (i.e., crashes), coverage information will not be flushed to disk (`.gcda` files).
This causes coverage to be incomplete or missing for essentially every program in this benchmark.

To workaround that limitation, Darjeeling injects instrumentation, shown below, into the top of the program under repair to cause it to flush coverage information before terminating.
Darjeeling uses the information provided by `coverage-files` to determine which files should be instrumented.

```c

    /* DARJEELING :: INSTRUMENTATION :: START */
    #include <stdio.h>
    #include <stdlib.h>
    #include <signal.h>
    #ifdef __cplusplus
      extern "C" void __gcov_flush(void);
    #else
      void __gcov_flush(void);
    #endif
    void darjeeling_sighandler(int sig){
      __gcov_flush();
      if(sig != SIGUSR1 && sig != SIGUSR2)
        exit(1);
    }
    void darjeeling_ctor (void) __attribute__ ((constructor));
    void darjeeling_ctor (void) {
      struct sigaction new_action;
      new_action.sa_handler = darjeeling_sighandler;
      sigemptyset(&new_action.sa_mask);
      new_action.sa_flags = 0;
      sigaction(SIGTERM, &new_action, NULL);
      sigaction(SIGINT, &new_action, NULL);
      sigaction(SIGKILL, &new_action, NULL);
      sigaction(SIGSEGV, &new_action, NULL);
      sigaction(SIGFPE, &new_action, NULL);
      sigaction(SIGBUS, &new_action, NULL);
      sigaction(SIGILL, &new_action, NULL);
      sigaction(SIGABRT, &new_action, NULL);
      /* Use signal for SIGUSR to remove handlers */
      signal(SIGUSR1, darjeeling_sighandler);
      signal(SIGUSR2, darjeeling_sighandler);
    }
    /* DARJEELING :: INSTRUMENTATION :: END */
```

### What files should I add to coverage-files?

You should add the translation unit that provides `main` for the specific binary that is under repair.
Other files should not be added.
If multiple source files from the same binary are instrumented, compilation will fail due to multiple definitions.


Contributors
------------

* `Jyoti Prakash <https://github.com/jpksh90>`_ (jyoti at u dot nus dot edu)
