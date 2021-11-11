Security Repair Benchmark
=========================

**Author:** `Chris Timperley <https://github.com/ChrisTimperley>`_ (ctimperley at cmu dot edu)

This project provides a reusable and reproducible infrastructure for evaluating C/C++ security vulnerability
repair techniques. The project consists of Dockerized repair tools and bug benchmarks, and can accessed either
via one monolithic Docker image, containing all tools and bugs, or via separate Docker images for individual bug
scenarios.

Out of the box, we provide Dockerized versions of ExtractFix and HiFix, as well as a useful helper script
for quickly running experiments using those tools. We also provide the VulnLoc benchmarks.


Installation
------------

To build a single Docker image, :code:`secbugs`, containing all of the bug scenarios and experimental
infrastructure, execute the following:

.. code:: command

  $ git submodule update --init --recursive
  $ make

**Beware that this will take a considerable amount of time (1-3 hours depending on hardware), memory (16 GB is a minimum), and disk space
(tens of GBs) to build for the first time.**
Subsequent builds will be faster since image caching can be used.

Note that you may observe failures when building the complete benchmark Docker image
(e.g., failed to copy non-existent layer for :code:`COPY --from=...` instructions).
This is an issue that non-deterministically crops up in Docker when attempting to copy
from large images. The (rather hacky) solution is to simply attempt to rebuild the image.
You may need to attempt building the image several times until it finishes successfully,
but in most cases, you should see progress being made between build attempts.


Usage
-----

We provide a convenient executable, :code:`secbugs`, within the container.
This command is used to run a given tool against a specified benchmark inside
the container.

To attempt to repair a given bug scenario using a certain tool, run the following:

.. code:: command

  $ scripts/run.sh
  # secbugs repair [name-of-tool] [benchmark-directory]


where :code:`[name-of-tool]` is replaced by either :code:`hifix` or :code:`extractfix`,
and :code:`[benchmark-directory]` gives the absolute path to the scenario directory
inside the container.

For example, to fix the :code:`jasper/cve_2016_9557` scenario within the VulnLoc dataset using
ExtractFix, execute the following:

.. code:: command

  $ scripts/run.sh
  # cd /benchmarks/jasper/cve_2016_9557
  # secbugs repair extractfix .


Darjeeling
...........

Running the original, baseline version of Darjeeling requires a different set of
steps, described here: https://github.com/squaresLab/security-repair-benchmarks/blob/main/docs/darjeeling.rst


Scenario Format
---------------

Each bug scenario within this benchmark is given its own directory (e.g., :code:`/benchmarks/vulnloc/binutils/cve_2017_14745`),
which provides the files necessary to perform repair on that bug using a variety of tools.
Below is a brief description of the files that MUST be included in each bug scenario directory:

* :code:`bug.json` provides several details about the bug as well as tool-specific configuration
  options that should be used when attempting to repair it.
* :code:`test` provides a script for executing the single failing test (i.e., payload) for the bug
  scenario. The script takes a single, optional argument, providing the absolute path of the binary
  that should be used to run the test. (This is useful in cases where a repaired binary is created in
  a different location to the original binary.) If no argument is provided, the script will use the
  original binary to perform the test.
* :code:`clean` (equivalent to :code:`make clean`) removes any compiled binaries, objects, etc. This
  is useful for recompiling the program with coverage instrumentation enabled (e.g., when performing
  repair with Darjeeling).
* :code:`prebuild` (similar to :code:`./configure`) appropriately configures the project. Note that
  this script requires that a :code:`REPAIR_TOOL` environment variable is set, stating the repair tool,
  if any, that is being used in conjunction with the code. This feature is used to compile the program
  in slightly different ways according to the assumptions of various tools. To build the program without
  targeting any specific tool, you can just pass in :code:`REPAIR_TOOL=none`. (E.g., :code:`REPAIR_TOOL=none ./prebuild`.)
* :code:`build` (similar to :code:`make`) builds the project. As with :code:`prebuild`, this step requires
  that the :code:`REPAIR_TOOL` environment variable be appropriately set.


Contributors
------------

* `Jyoti Prakash <https://github.com/jpksh90>`_ (jyoti at u dot nus dot edu)
