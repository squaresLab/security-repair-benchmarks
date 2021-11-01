#!/usr/bin/env python
import argparse
import json
import os
import sys
import typing as t

import yaml

DESCRIPTION = "generates a Darjeeling config file for a given bug."


def generate_config(
    program_name: str,
    bug_name: str,
    seed: int,
    threads: int,
    max_candidates: int,
    coverage_files: t.List[t.Union[str, t.Dict[str, t.Any]]],
    *,
    source_directory: str = "/workspace/source",
    workspace_directory: str = "/workspace",
    test_time_limit_seconds: int = 5,
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
        "metric": "genprog",
    }

    config["optimizations"] = {
        "ignore-equivalent-insertions": True,
        "ignore-dead-code": True,
        "ignore-string-equivalent-snippets": True,
    }

    # determine the name of the Docker image
    docker_image_name = f"{program_name}-{bug_name}"

    config["program"] = {
        "image": docker_image_name,
        "language": "c",
        "source-directory": source_directory,
        "build-instructions": {
            "time-limit": 30,
            "environment": {
                "REPAIR_TOOL": "darjeeling",
            },
            "steps": [
                {
                    "command": "REPAIR_TOOL=darjeeling ./prebuild",
                    "directory": workspace_directory,
                },
                {
                    "command": "REPAIR_TOOL=darjeeling ./build",
                    "directory": workspace_directory,
                },
            ],
            "steps-for-coverage": [
                {
                    "command": "REPAIR_TOOL=darjeeling CFLAGS=--coverage LDFLAGS=--coverage ./clean",
                    "directory": workspace_directory,
                },
                {
                    "command": "REPAIR_TOOL=darjeeling CFLAGS=--coverage LDFLAGS=--coverage ./prebuild",
                    "directory": workspace_directory,
                },
                {
                    "command": "REPAIR_TOOL=darjeeling CFLAGS=--coverage LDFLAGS=--coverage ./build",
                    "directory": workspace_directory,
                },
            ],
        },
        "tests": {
            "type": "shell",
            "workdir": workspace_directory,
            "tests": ["./test"],
            "time-limit": test_time_limit_seconds,
        }
    }

    config["coverage"] = {
        "method": {
            "type": "gcov",
            "files-to-instrument": coverage_files,
        },
    }

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
        "options",
    )
    for field_name in expected_fields:
        if field_name not in bug_description:
            raise ValueError(f"missing required property in bug.json: {field_name}")

    # TODO turn these into command-line arguments to this script!
    seed = 0
    threads = 8
    max_candidates = 100

    try:
        coverage_files = bug_description["options"]["darjeeling"]["coverage-files"]
    except KeyError:
        raise ValueError("missing darjeeling.coverage-files field in bug.json")

    config = generate_config(
        program_name=bug_description["subject"],
        bug_name=bug_description["name"],
        seed=seed,
        threads=threads,
        max_candidates=max_candidates,
        coverage_files=coverage_files,
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
