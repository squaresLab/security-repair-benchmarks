Support for Baseline Darjeeling
===============================

In addition to supporting HiFix and ExtractFix, we aim to support the original, baseline version of Darjeeling on this benchmark.
We provide a script, `generate-darjeeling-config.py <https://github.com/squaresLab/security-repair-benchmarks/blob/main/scripts/generate-darjeeling-config.py>`_, that automatically generates a Darjeeling configuration file for a given scenario (specified by its directory) by using the information provided in the :code:`bug.json` file for that bug scenario.


Installation
------------

Darjeeling should be installed via Pipenv.
Pipenv is a package manager for Python that allows you to install dependencies in a standalone environment.
That is, your Darjeeling installation (and its necessary dependencies) won't interfere with your system (or user) Python installation.
You can install pipenv via the following command:

.. code::

  $ python -m pip install --user pipenv

Once pipenv is installed, you can install Darjeeling by executing the following at the root of the directory:

.. code::

  $ git submodule update --init --recursive
  $ pipenv install

The lines above will initialize and update the Darjeeling repository, and instruct pipenv to install Darjeeling from source. If you wish to make changes to Darjeeling, you may do so within the `deps/darjeeling` directory, and those changes will be instantly reflected whenever you interact with Darjeeling via Pipenv.


Usage
-----

To generate the Darjeeling configuration file for a particular scenario, execute the following command from the root of the directory:

.. code::

  $ pipenv run scripts/generate-darjeeling-config.py [path-to-experiment-directory]

where :code:`[path-to-experiment-directory]` is replaced by the path to the directory for a particular bug scenario (e.g., :code:`bugs/vulnloc/libtiff/bugzilla_2611`).

Once a Darjeeling configuration file has been created, you perform repair via Darjeeling on the given bug via the following:

.. code::

  $ pipenv run darjeeling repair [path-to-experiment-directory]/repair.darjeeling.yml
