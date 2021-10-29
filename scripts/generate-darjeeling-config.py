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
    program_name: str,
    bug_name: str,
    seed: int,
    threads: int,
    max_candidates: int,
    *,
    source_directory: str = "/workspace/src",
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

    # determine the name of the Docker image
    docker_image_name = f"{program_name}-{bug_name}"

    config["program"] = {
        "image": docker_image_name,
        "language": "c",
        "source-directory": source_directory,
        "build-instructions": BUILD_INSTRUCTIONS,
        "tests": "FIXME",
    }

    # TODO add test config to program
    # program:
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


def generate_for_bug_file(bug_filename: str) -> str:
    bug_directory = os.path.dirname(bug_filename)
    output_filename = os.path.join(bug_directory, "repair.darjeeling.yml")

    if not os.path.exists(bug_filename):
        raise ValueError(f"bug.json file does not exist: {filename}")

    with open(bug_filename, "r") as fh:
        bug_description = json.load(fh)

    expected_fields = (
        "subject",
        "name",
    )
    for field_name in expected_fields:
        if field_name not in bug_description:
            raise ValueError(f"missing required property in bug.json: {field_name}")

    # TODO turn these into command-line arguments to this script!
    seed = 0
    threads = 8
    max_candidates = 100

    # FIXME
    config = generate_config(
        program_name=bug_description["subject"],
        bug_name=bug_description["name"],
        seed=seed,
        threads=threads,
        max_candidates=max_candidates,
    )

    with open(output_filename, "w") as fh:
        yaml.dump(config, fh, default_flow_style=False)

    return output_filename


def generate_for_bug_directory(directory: str) -> str:
    if not os.path.exists(directory):
        raise ValueError(f"bug directory does not exist: {directory}")

    bug_filename = os.path.join(directory, "bug.json")
    return generate_for_bug_file(bug_filename)


def main(args: t.Optional[t.Sequence[str]] = None) -> None:
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument(
        "directory",
        help="the directory for the bug scenario",
    )

    parsed_args = parser.parse_args(args)
    output_filename = generate_for_bug_directory(parsed_args.directory)
    print(f"wrote Darjeeling config file: {output_filename}")


if __name__ == "__main__":
    main()
