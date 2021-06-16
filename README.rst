Security Repair Benchmark
=========================

**Author:** `Chris Timperley <https://github.com/ChrisTimperley>`_ (ctimperley at cmu dot edu)

This project provides a reusable and reproducible infrastructure for evaluating C/C++ security vulnerability
repair techniques. The project consists of Dockerized repair tools and bug benchmarks, and can accessed either
via one monolithic Docker image, containing all tools and bugs, or via separate Docker images for individual bug
scenarios.

Out of the box, we provide Dockerized versions of ExtractFix and HiFix, as well as a useful helper script
for quickly running experiments using those tools. We also provide the VulnLoc benchmarks.


Citation
--------

TODO: Add our paper; VulnLoc; ExtractFix; etc.


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

  $ docker run --rm -it secbugs
  # secbugs repair [name-of-tool] [benchmark-directory]


where :code:`[name-of-tool]` is replaced by either :code:`hifix` or :code:`extractfix`,
and :code:`[benchmark-directory]` gives the absolute path to the scenario directory
inside the container.

For example, to fix the :code:`jasper/cve_2016_9557` scenario within the VulnLoc dataset using
ExtractFix, execute the following:

.. code:: command

  $ docker run --rm -it secbugs
  # cd /benchmarks/jasper/cve_2016_9557
  # secbugs repair extractfix .


Scenario Format
---------------

Contributors
------------

* `Jyoti Prakash <https://github.com/jpksh90>`_ (jyoti at u dot nus dot edu)
