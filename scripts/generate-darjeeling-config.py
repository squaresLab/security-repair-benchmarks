#!/usr/bin/env python
import argparse
import json
import os
import sys
import typing as t

import yaml

DESCRIPTION = "generates a Darjeeling config file for a given bug."

TESTS_CONFIG = {
    "type": "shell",
    "workdir": "FOO_BAR_BAZ",  # FIXME
    "time-limit": 5,
    "tests": [

    ],
}

BUILD_INSTRUCTIONS = {
    "time-limit": 30,
    "environment": {
        "REPAIR_TOOL": "darjeeling",
    },
    "steps": [
        "REPAIR_TOOL=darjeeling ./prebuild",
        "REPAIR_TOOL=darjeeling ./build",
    ],
    "steps-for-coverage": [
        "REPAIR_TOOL=darjeeling CFLAGS=--coverage LDFLAGS=--coverage ./prebuild",
    ],
}


def generate_config(
    seed: int,
    threads: int,
    max_candidates: int,
) -> t.Dict[str, t.Any]:
    config = {}
    config["version"] = 1.0
    config["seed"] = seed
    config["threads"] = threads

    config["algorithm"] = {
        "type": "exhaustive",
    }

    config["transformations"] = {
        "schemas": [
            {"type": "delete-statement"},
            {"type": "replace-statement"},
            {"type": "append-statement"},
        ],
    }

    config["resource-limits"] = {
        "candidates": max_candidates,
    }

    config["localization"] = {
        "type": "spectrum",
        "metric": "tarantula",
    }

    config["optimizations"] = {
        "ignore-equivalent-insertions": "yes",
        "ignore-dead-code": "yes",
        "ignore-string-equivalent-snippets": "yes",
    }

    # TODO program
    # program:
    #   image: darjeeling/example:zune
    #   language: c
    #   source-directory: /experiment/source
    #   build-instructions:
    #     time-limit: 15
    #     environment:
    #       REPAIR_TOOL: darjeeling
    #       CC: /opt/llvm11/bin/clang
    #       CXX: /opt/llvm11/bin/clang++
    #     steps:
    #       - REPAIR_TOOL=darjeeling ./prebuild
    #       - REPAIR_TOOL=darjeeling ./build
    #     steps-for-coverage:
    #       - REPAIR_TOOL=darjeeling CFLAGS=- ./prebuild
    #   tests:
    #     type: genprog
    #     workdir: /experiment
    #     number-of-failing-tests: 4
    #     number-of-passing-tests: 18
    #     time-limit: 5

    # TODO coverage
    # coverage:
    #   method:
    #     type: gcov
    #     files-to-instrument:
    #       - zune.c

    return config


def generate_for_bug_file(bug_filename: str) -> None:
    bug_directory = os.path.dirname(bug_filename)
    output_filename = os.path.join(bug_directory, "repair.darjeeling.yml")

    if not os.path.exists(bug_filename):
        raise ValueError(f"bug.json file does not exist: {filename}")

    # TODO turn these into command-line arguments to this script!
    seed = 0
    threads = 8
    max_candidates = 100

    # FIXME
    config = generate_config(
        seed=seed,
        threads=threads,
        max_candidates=max_candidates,
    )

    with open(output_filename, "w") as fh:
        yaml.dump(config, fh, default_flow_style=False)


def generate_for_bug_directory(directory: str) -> None:
    if not os.path.exists(directory):
        raise ValueError(f"bug directory does not exist: {directory}")

    bug_filename = os.path.join(directory, "bug.json")
    generate_for_bug_file(bug_filename)


def main(args: t.Optional[t.Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "directory",
        help="the directory for the bug scenario",
    )

    parsed_args = parser.parse_args(args)
    generate_for_bug_directory(parsed_args.directory)


if __name__ == "__main__":
    main()
