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

**Note that you will need to provide coverage instructions for that scenario via its associated bug.json file.**
An example of those coverage instructions, provided by the :code:`darjeeling` sub-section of :code:`options`, is given below.

.. code:: json

  {
    "subject": "coreutils",
    "name": "gnubug_19784",
    "options": {
      "extractfix": {
        "bug-type": "buffer_overflow",
        "binary": {
          "name": "make-prime-list",
          "path": "src/make-prime-list"
        },
        "lowfat": {
          "CFLAGS": "-fsanitize=lowfat -mllvm -lowfat-debug -mllvm -lowfat-no-check-memset -mllvm -lowfat-no-check-memcpy -mllvm -lowfat-no-check-escapes -mllvm -lowfat-no-check-fields -mllvm -lowfat-no-replace-globals -mllvm -lowfat-memcpy-overlap -mllvm -lowfat-symbolize -lstlimpl"
        }
      },
      "darjeeling": {
        "coverage-files": [
          {
            "filename": "src/make-prime-list.c",
            "line": 29
          }
        ]
      }
    },
    "binary": "src/make-prime-list"
  }

The :code:`coverage-files` property can take either a list of filenames, shown below, or a more detailed list, where each entry specifies the particular line in each file where coverage instrumentation should be added.
This detail is necessary when dealing with programs (e.g., coreutils) that require that certain includes appear before others.

.. code:: json

      "darjeeling": {
        "coverage-files": [
          {
            "filename": "src/make-prime-list.c",
            "line": 29
          }
        ]
      }

Once a Darjeeling configuration file has been created, you perform repair via Darjeeling on the given bug via the following:

.. code::

  $ pipenv run darjeeling repair [path-to-experiment-directory]/repair.darjeeling.yml


Troubleshooting and Questions
-----------------------------

How does Darjeeling obtain coverage?
....................................

Darjeeling recompiles the program with the appropriate :code:`--coverage` flags to allow line-level coverage to be collected via :code:`gcov`.
(More specifically, we use :code:`gcovr` under the hood to make life a little easier.)
A problem with this approach is that if the program abruptly terminates (i.e., crashes), coverage information will not be flushed to disk (:code:`.gcda` files).
This causes coverage to be incomplete or missing for essentially every program in this benchmark.

To workaround that limitation, Darjeeling injects instrumentation, shown below, into the top of the program under repair to cause it to flush coverage information before terminating.
Darjeeling uses the information provided by :code:`coverage-files` to determine which files should be instrumented.

.. code:: c

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


What files should I add to coverage-files?
..........................................

You should add the translation unit that provides :code:`main` for the specific binary that is under repair.
Other files should not be added.
If multiple source files from the same binary are instrumented, compilation will fail due to multiple definitions.


Inadequate oracles lead to false negatives during repair
........................................................
