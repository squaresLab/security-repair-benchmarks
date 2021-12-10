# Baseline darjeeling
This is a step by step guide to get darjeeling up and running on the bugs in this benchmark set on an Ubuntu machine. There are currently 15 exploits (located in the table at the bottom) on which darjeeling can be successfully run. 

## Prerequisites
This guide assumes a fresh updated installation of Ubuntu 21.04. Other Ubuntu versions
may require more/different packages to be installed. This guide is annotated with
instructions necessary to configure Ubuntu 18.04 when instructions differ. 

## Authentication and Github.com
This git repository and related submodules assume by default that the user has both a `github.com` account and uses `SSH` authentication between their local machine and their `github.com` account. 
If you do not have any of these, please see the instructions at [Git without SSH Authentication](#git-without-ssh-authentication)

## Install docker
Docker is required for this project and must be installed first. We recommend using the official
[docker](https://docs.docker.com/engine/install/ubuntu/) documentation.
## Retrieve the code from the repository and build
1. Clone the repository :
~~~
git clone git@github.com:squaresLab/security-repair-benchmarks.git
~~~
***NOTE:*** In the event that you run into errors cloning, such as ```Please make sure you have the correct access rights and the repository exists```, please follow all instructions at [Git without SSH Authentication](#git-without-ssh-authentication).

2. Check out the demonstration branch:
~~~
cd security-repair-benchmarks
git checkout aflr_demo_12_2021
~~~

3. Make the project:
~~~
make
~~~
In the event that `make` gives an error about 'access rights', see [Git without SSH Authentication](#git-without-ssh-authentication).

This will make all the test containers and requires no less than an hour.

To make an individual test container: 
~~~
cd security-repair-benchmarks/bugs/vulnloc/<prog>
make <CVE/exploit>
~~~

Note that you may observe failures when building the complete benchmark Docker image
(e.g., failed to copy non-existent layer for :code:`COPY --from=...` instructions).
This is an issue that non-deterministically crops up in Docker when attempting to copy
from large images. The (rather hacky) solution is to simply attempt to rebuild the image.
You may need to attempt building the image several times until it finishes successfully,
but in most cases, you should see progress being made between build attempts.

4. Verify the project made correctly:
~~~
scripts/run.sh
~~~
This will open the secbugs docker container. `<ctrl> d` to exit.

## Install requirements and run darjeeling:
The following steps assume you are in the same directory as as above (`security-repair-benchmarks`).

***NOTE: If running Ubuntu 18.04 use the instructions at [Ubuntu 18.04 Installation](#ubuntu-18-installation) instead of 1 and 2 below.***
1. Install pipenv and pip:
~~~
sudo apt-get install python3-pip
python3 -m pip install --user pipenv
sudo apt-get install pipenv
~~~
2. Set up the python environment:
~~~
pipenv install
~~~
***NOTE:*** If you run into `pipenv` issues, please see [Resolutions for Known Issues](#resolutions-for-known-issues)-[PIPENV Issues](#pipenv-issues)

3. Run darjeeling
To run darjeeling on a specific bug first generate a configuration file for that bug, for example: 
~~~
pipenv run scripts/generate-darjeeling-config.py bugs/vulnloc/coreutils/gnubug_19784
~~~
This command uses the information in the `bug.json` file for the given bug to generate a Darjeeling 
configuration yml file. 

*Note:* `generate-darjeeling-config.py` currently generates a working default darjeeling yml
configuration file for the bug scenario. Should you want to modify the yml directly (e.g., 
modify the number of candidate patches evaluated), see the Darjeeling configuration documentation
available [here](https://github.com/squaresLab/Darjeeling).

Next run darjeeling on this generated yml file:
~~~
pipenv run darjeeling repair bugs/vulnloc/coreutils/gnubug_19784/repair.darjeeling.yml
~~~
### Darjeeling-supported Exploit Scenarios
The following bugs can be used with darjeeling:
| Project | CVE/exploit |
|---------|-------------|
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

To run darjeeling on any of the bugs:
~~~
pipenv run scripts/generate-darjeeling-config.py bugs/vulnloc/<Project>/<CVE/exploit>
pipenv run darjeeling repair bugs/vulnloc/<Project>/<CVE/exploit>/repair.darjeeling.yml
~~~
where `<Project>` and `<CVE/exploit>` can be any of the pairs of values from the table.

---
## Resolutions for Known Issues

### Git without SSH Authentication
This git repository and related submodules assume by default that the user has both a `github.com` account and uses `SSH` authentication between their local machine and their `github.com` account. 
If you do not have both, follow these directions:

1. Clone the https version: 
~~~
git clone https://github.com/squaresLab/security-repair-benchmarks.git
~~~
2. Checkout the demonstration branch:
~~~
cd security-repair-benchmarks
git checkout aflr_demo_12_2021
~~~
3. Edit `.git/config` to reference `https` not `git@` urls.
For example:
~~~
[submodule "tools/Darjeeling"]
	active = true
	url = https://github.com/squaresLab/Darjeeling
~~~

### PIPENV Issues 
If prompted about the following "lock" error, log out and back in to solve this issue.
~~~
Traceback (most recent call last):
  File "/home/tony/.local/lib/python3.9/site-packages/pipenv/resolver.py", line 766, in <module>
    main()
  File "/home/tony/.local/lib/python3.9/site-packages/pipenv/resolver.py", line 751, in main
    from pipenv.vendor.vistir.compat import ResourceWarning
ModuleNotFoundError: No module named 'pipenv.vendor.vistir'
~~~


### UBUNTU 18 Installation 

***If running Ubuntu 18.04 use the following instructions***
~~~
sudo apt update && sudo apt install software-properties-common && sudo add-apt-repository ppa:deadsnakes/ppa && sudo apt install python3.9
sudo apt install python3.9-distutils
sudo apt install python3-pip
python3.9 -m pip install --user pipenv
pipenv install
~~~
If this fails, log out and log back in again, then rerun in `security-repair-benchmarks`:
~~~
pipenv install
~~~
