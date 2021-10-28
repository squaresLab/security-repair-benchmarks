#!/usr/bin/env python
import argparse
import json
import os
import sys
import typing as t

import yaml

DESCRIPTION = "generates a Darjeeling config file for a given bug."

LOCALIZATION_CONFIG = {
    "type": "spectrum",
    "metric": "tarantula",
}
OPTIMIZATIONS_CONFIG = {
    "ignore-equivalent-insertions": "yes",
    "ignore-dead-code": "yes",
    "ignore-string-equivalent-snippets": "yes",
}
TRANSFORMATIONS_CONFIG = {
    "schemas": [
        {"type": "delete-statement"},
        {"type": "replace-statement"},
        {"type": "append-statement"},
    ],
}
ALGORITHM_CONFIG = {
    "type": "exhaustive",
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


def generate_for_bug_file(bug_filename: str) -> None:
    bug_directory = os.path.dirname(bug_filename)
    output_filename = os.path.join(bug_directory, "repair.darjeeling.yml")

    if not os.path.exists(bug_filename):
        raise ValueError(f"bug.json file does not exist: {filename}")

    seed = 0
    threads = 8
    max_candidates = 100

    config = {
        "version": "1.0",
        "program": program_config,
        "seed": seed,
        "threads": threads,
        "localization": LOCALIZATION_CONFIG,
        "resource-limits": {
            "candidates": max_candidates,
        },
    }

    raise NotImplementedError


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


if __name__ == "__main__":
    main()
