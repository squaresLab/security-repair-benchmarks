# Documentation for Concentrated Fuzzing

## TODOs
- [X] Generate inputs in our environment for test `cve_2016_5314`
- [ ] Include fuzzer reliably in the environment
	- [X] fix python package installations with PYTHONPATH
 	- [X] fix other installations with PATH
 	- [X] provide wrapper for fuzz.py
 	- [ ] include fuzzer volume in secbugs container (not sure exactly, see below)
- [ ] Integrate fuzzer in patch validation and ranking algorithm. Chris wanted to fill in the control code and the instrumentation of the patched program.
- [ ] Provide configuration files (`config.ini`) and binary compilation for all subjects (expected to need a recompilation for each fuzzing campaign because of different parameters)
- [ ] libtiff
	- [X] bugzilla_2611, no inputs within 20 min (test on server)
	- [X] bugzilla_2633
	- [X] cve_2016_3186
	- [X] cve_2016_5314
	- [X] cve_2016_5321
	- [X] cve_2016_9273
	- [X] cve_2016_9532
	- [X] cve_2016_10092
	- [X] cve_2016_10094
	- [X] cve_2016_10272
	- [X] cve_2017_5225
	- [X] cve_2017_7595, no inputs within 5min
	- [X] cve_2017_7599, no inputs within 5min
	- [X] cve_2017_7600, no inputs within 5min
	- [X] cve_2017_7601
- [ ] binutils
	- [X] cve_2017_6965
	- [X] cve_2017_14745
	- [X] cve_2017_15020
	- [X] cve_2017_15025, no inputs within 5 min
- [ ] coreutils
	- [X] gnubug_19784 (store all inputs)
	- [X] gnubug_25003 (store all inputs)
	- [X] gnubug_25023 (store all inputs)
	- [X] gnubug_26545 (store all inputs), ! no inputs are generated
- [ ] ffmpeg
	- [ ] bugchrom_1404 TODO
	- [ ] cve_2017_9992 TODO
- [ ] jasper
	- [X] cve_2016_8691, no inputs within 5min
	- [X] cve_2016_9557, no inputs within 5min
- [ ] libarchive
	- [X] cve_2016_5844, (running on server)
- [ ] libjpeg
	- [X] cve_2012_2806, no inputs within 5min
	- [X] cve_2017_15232
	- [X] cve_2018_14498, no inputs within 5min
	- [X] cve_2018_19664, no inputs within 5min
- [X] libming
	- [X] cve_2016_9264
	- [X] cve_2018_8806
	- [X] cve_2018_8964
- [ ] libxml2
	- [X] cve_2012_5134
	- [X] cve_2016_1838, memory problem?
	- [X] cve_2016_1839, memory problem?
	- [X] cve_2017_5969
- [ ] potrace
	- [X] cve_2013_7437, memory problem?
- [X] zziplib
	- [X] cve_2017_5974
	- [X] cve_2017_5975
	- [X] cve_2017_5976


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
cd /benchmarks/libtiff/cve_2016_5314
./build-for-fuzzer
```


### 6. Modify configuration (if needed)

```
vi /benchmarks/libtiff/cve_2016_5314/config.ini
```

### 7. Run fuzzer

```
/opt/fuzzer/code/fuzz --config_file /benchmarks/libtiff/cve_2016_5314/config.ini --tag cve_2016_5314
/opt/fuzzer/code/fuzz --config_file config.ini --tag cve_2016_5314
```

... wait for specified time bound in config.ini (current default setup is 5 min for testing purpose)


### 8. Check generated inputs

```
ls /benchmarks/libtiff/cve_2016_5314/output_<timestamp>/inputs
```
