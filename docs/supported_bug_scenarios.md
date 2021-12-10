# Provided Dockerized Bug Scenarios

## VulnLock Benchmark Set

This project contains dockerized versions of all security benchmarks available in the
[VulnLock](https://github.com/VulnLoc/VulnLoc) security vulnerability benchmark set. 
In this project, these vulnerabilities are organized by program and available in 
`bugs\vulnlock`. Each vulnerability also contains a README with a link to the original
bug report and a link to the commit with the eventual developer patch.

## Darjeeling Supported Scenarios

While this project contains dockerized versions of all vulnerabilities in VulnLoc,
out of the box, we provide Darjeeling support for only a subset of vulnerabilities taken
from four programs:
* libtiff
* libxml2
* coreutils
* binutils

We have tested that the following bugs can be used with darjeeling:

| Project | CVE/exploit     |
|---------|-----------------|
|libtiff  |bugzilla_2633    |
|libtiff  |cve_2016_10092   |
|libtiff  |cve_2016_10094   |
|libtiff  |cve_2016_10272   |
|libtiff  |cve_2016_3186    |
|libtiff  |cve_2016_5321    |
|libtiff  |cve_2016_9273    |
|libtiff  |cve_2016_9532    |
|libtiff  |cve_2017_7599    |
|libxml2  |cve_2012_5134    |
|libxml2  |cve_2016_1839    |
|libxml2  |cve_2017_5969    |
|binutils |cve_2017_14745   |
|binutils |cve_2017_15025   | 
|coreutils|gnubug_19784     |

Any other security vulnerabilities in this data set (including some additional CVEs in libtiff, libxml2, coreutils, and binutils) have not been run with Darjeeling.

## Additional Helpful Docker Images

Beyond supporting the bugs above, we also provide some additional darjeeling-supported docker images that may be helpful:

* `cve_2016_10092-multi-pos`: One thing that differentiates the vulnerabilities in VulnLoc from
those traditionally used in program repair techniques is that it does not assume a test suite 
exists for the program, and thus there is only one failing test case per scenario. However, we
also provide an additional version of libtiff's `cve_2016_10092`, `cve_2016_10092-multi-pos`,
which contains a full test suite as an additional example. Should you wish to use multiple tests when generating exploit scenarios, `cve_2016_10092-multi-pos`can be used as an example. Darjeeling
can be run on this scenario the same way it is run on scenarios with a single failing test case.
* `fixed-versions`: To aid in generating new vulnerabilities, we also provide docker images for 
the developer patched version of each darjeeling supported bug in the table above. For example, the 
`cve_2016_10092-fixed` contains the version of libtiff that was patched to expose the bug in
`cve_2016_10092`. These "fixed" versions may be a helpful jumping off point for
injecting additional faults.
* `cve_2017_760x-known-good`: We also proved a dockerized version of libtiff that contains the
eventual patches for all the libtiff bugs in VulnLoc. This may be another helpful jumping off
point for injecting additional faults.


