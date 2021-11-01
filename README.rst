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

To build a single Docker image, :code:`secbugs`, containing all bug scenarios, repair tools, and experimental
infrastructure, execute the following:

.. code:: command

  $ git submodule update --init --recursive
  $ make


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


Contributors
------------

* `Jyoti Prakash <https://github.com/jpksh90>`_ (jyoti at u dot nus dot edu)
