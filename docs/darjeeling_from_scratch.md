1. Install docker on the base machine. We recommend using the official
[docker](https://docs.docker.com/engine/install/ubuntu/) documentation.
2. Clone the repository:
	- `git clone git@github.com:squaresLab/security-repair-benchmarks.git`
        - `git clone https://github.com/squaresLab/security-repair-benchmarks.git`
3. Make the project in the cloned repository:
	- `cd security-repair-benchmarks`
	- Checkout the demonstration branch:
		- `git checkout aflr_demo_12_2021`
        - `make`
4. Verify the project made correctly:
        - `cd security-repair-benchmarks`
        - `scripts/run.sh`
                - This will open the docker container from the command line.
5. Setup the system to run darjeeling:
        - `python3 -m pip install --user pipenv`
        - `may need to install pipenv and pip`
                - `sudo apt-get install pipenv pip`
        - run `pipenv install`

6. Run darjeeling
- `pipenv run scripts/generate-darjeeling-config.py bugs/vulnloc/coreutils/gnubug_19784`
- `pipenv run darjeeling repair bugs/vulnloc/coreutils/gnubug_19784/repair.darjeeling.yml`
