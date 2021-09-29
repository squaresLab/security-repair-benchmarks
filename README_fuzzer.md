# Documentation for Concentrated Fuzzing

## TODOs
- [X] Generate inputs in our environment for test `cve_2016_5314`
- [ ] Include fuzzer reliably in the environment
	- [X] fix python package installations with PYTHONPATH
 	- [X] fix other installations with PATH
 	- [X] provide wrapper for fuzz.py
 	- [ ] include fuzzer volume in secbugs container (not sure exactly, see below)
- [ ] Provide configuration files (`config.ini`) for all subjects 
- [ ] Check binary compilation for all subjects (expected to need a recompilation for each fuzzing campaign because of different parameters)
- [ ] Integrate fuzzer in patch validation and ranking algorithm. Chris wanted to fill in the control code and the instrumentation of the patched program.


## Commands for example `cve_2016_5314`


### 1. Build the secbugs Docker image

```
git submodule update --init --recursive
make
```


### 2. Build the fuzzer Docker image

```
cd tools
make fuzzer
cd ../
```


### 3. Extract the *fuzzer_opt* volume

TODO (YN) I did not know how exactly to do this, so this might be just a work-around and paths need to be modified for host machines

```
docker run --rm -v /Users/yannic/repositories/darjeeling_collaboration/security-repair-benchmarks/scripts/fuzzer_opt:/fuzzer_opt --name fuzzer_container -it fuzzer
cp -r . /fuzzer_opt # (this may time a while)
exit
```


### 4. Start secbugs container

```
./scripts/run_fuzzer_test.sh
```


### 5. Prepare binary

```
cd /benchmarks/libtiff/cve_2016_5314/source
./configure
make CFLAGS="-static -ggdb" CXXFLAGS="-static -ggdb"
```


### 6. Modify configuration (if needed)

```
vi /benchmarks/libtiff/cve_2016_5314/config.ini
```

### 7. Run fuzzer

```
/opt/fuzzer/code/fuzz --config_file /benchmarks/libtiff/cve_2016_5314/config.ini --tag cve_2016_5314
```

... wait for specified time bound in config.ini (current default setup is 5 min for testing purpose)


### 8. Check generated inputs

```
ls /benchmarks/libtiff/cve_2016_5314/output_<timestamp>/inputs
```