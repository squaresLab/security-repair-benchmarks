# security-repair-benchmarks

## Installation

To build a single Docker image, `secbugs`, containing all bug scenarios, repair tools, and experimental
infrastructure, execute the following:

```
$ git submodule update --init --recursive
$ make
```


## Usage

To attempt to repair the `jasper/cve_2016_9557` scenario within the `vulnloc`
dataset using ExtractFix, perform the following:

```
$ docker run --rm -it secbugs
# cd /benchmarks/jasper/cve_2016_9557
# ./repair extractfix
```
