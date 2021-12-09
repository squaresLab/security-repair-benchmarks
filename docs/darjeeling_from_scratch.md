## Prerequisites
This guide assumes a fresh updated installation of Ubuntu 21.04. Other Ubuntu versions
may require more/different packages to be installed. This guide is annotated with
instructions necessary to configure Ubuntu 18.04 when instructions differ. 

## Install docker
Docker is required for this project and must be installed first. We recommend using the official
[docker](https://docs.docker.com/engine/install/ubuntu/) documentation.
## Retrieve the code from the repository and build
1. Clone the repository :
~~~
git clone git@github.com:squaresLab/security-repair-benchmarks.git
~~~
In the event that you run into errors cloning, such as:
~~~
Please make sure you have the correct access rights
and the repository exists.
~~~
use the https version: 
~~~
git clone https://github.com/squaresLab/security-repair-benchmarks.git
~~~
2. Make the project in the cloned repository
~~~
cd security-repair-benchmarks
~~~
Checkout the demonstration branch:
~~~
git checkout aflr_demo_12_2021
~~~
Make the project:
~~~
make
~~~
In the event that make gives the same error about access rights, edit `.git/config` such
that the URLs are of the https type. For example:
~~~
[submodule "tools/Darjeeling"]
	active = true
	url = https://github.com/squaresLab/Darjeeling

~~~
This will make all the test containers and requires no less than an hour.
To make an individual test: ADD DOCS HERE AFTER VERIFYING.

3. Verify the project made correctly:
~~~
scripts/run.sh
~~~
This will open the secbugs docker container. `<ctrl> d` to exit.

## Install requirements and run darjeeling:
The following steps assume you are in the same directory as as above (`security-repair-benchmarks`).
1. Install pipenv and pip:
~~~
sudo apt-get install pipenv pip
~~~
2. Set up the python environment:
~~~
python3 -m pip install --user pipenv
pipenv install
~~~
If prompted about "lock" issues reboot the machine.

***If running Ubuntu 18.04 use the following instructions in stead of 1 and 2 above:***
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

3. Run darjeeling


To run darjeeling first generate a configuration file, for example: 
~~~
pipenv run scripts/generate-darjeeling-config.py bugs/vulnloc/coreutils/gnubug_19784
~~~
Next run darjeeling on the generated yml file:
~~~
pipenv run darjeeling repair bugs/vulnloc/coreutils/gnubug_19784/repair.darjeeling.yml
~~~
