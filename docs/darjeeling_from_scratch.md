## Install docker
Docker is required for this project and must be installed first. We recommend using the official
[docker](https://docs.docker.com/engine/install/ubuntu/) documentation.
## Retrieve the code from the repository and build
1. To clone the repository use :`git clone
   git@github.com:squaresLab/security-repair-benchmarks.git`.  In the event
   that you run into errors cloning use the https version: `git clone
   https://github.com/squaresLab/security-repair-benchmarks.git`.
2. Make the project in the cloned repository
- `cd security-repair-benchmarks`
- Checkout the demonstration branch:
	- `git checkout aflr_demo_12_2021`
- `make`
3. Verify the project made correctly:
- `cd security-repair-benchmarks`
- `scripts/run.sh`
	- This will open the docker container from the command line.
## Setup the system to run darjeeling:
The following steps assume you are in the same directory as as above (`security-repair-benchmarks`).
1. Install pipenv and pip:
`sudo apt-get install pipenv pip`
2. Set up the python environment:
`python3 -m pip install --user pipenv`
`pipenv install`

4. Run darjeeling
To run darjeeling first generate the configuration file:
`pipenv run scripts/generate-darjeeling-config.py bugs/vulnloc/coreutils/gnubug_19784`.
Next run darjeeling on the generated yml file:
`pipenv run darjeeling repair bugs/vulnloc/coreutils/gnubug_19784/repair.darjeeling.yml`
