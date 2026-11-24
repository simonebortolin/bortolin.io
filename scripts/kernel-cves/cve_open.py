#!/usr/bin/env python3
"""Counts the kernel CVEs that affect a given kernel version and are not fixed in it.

Data source: the Linux kernel CNA's own records, in
https://git.kernel.org/pub/scm/linux/security/vulns.git (directory cve/published).
Each record states where a bug was introduced and in which stable releases it
was fixed; a version counts as affected unless one of the "unaffected" ranges
covers it.

    git clone --depth 1 https://git.kernel.org/pub/scm/linux/security/vulns.git
    python3 cve_open.py vulns/cve/published 3.10.108 5.10.274

Limits: the count covers the whole kernel source, including drivers and
architectures a given device does not build, and only CVEs issued by the
kernel CNA (from February 2024, plus older IDs it assigned retroactively).
"""
import json
import os
import re
import sys


def parse_version(text):
    parts = []
    for piece in text.split("."):
        match = re.match(r"\d+", piece)
        if not match:
            return None
        parts.append(int(match.group()))
    return tuple(parts)


def in_range(version, entry):
    low = parse_version(entry["version"]) if entry["version"] != "0" else (0,)
    if low is None:
        return None
    if "lessThan" in entry:
        high = parse_version(entry["lessThan"])
        return high is not None and low <= version < high
    if "lessThanOrEqual" in entry:
        limit = entry["lessThanOrEqual"]
        if limit == "*":
            return version >= low
        if limit.endswith(".*"):  # a whole stable branch, e.g. "6.1.*"
            prefix = parse_version(limit[:-2])
            return version >= low and version[:len(prefix)] == prefix
        high = parse_version(limit)
        return high is not None and low <= version <= high
    return None  # a bare version only says where the bug was introduced


def is_affected(version, record):
    blocks = [a for a in record["containers"]["cna"].get("affected", [])
              if a.get("defaultStatus") == "affected"]
    if not blocks:
        return None  # no version data
    for block in blocks:
        for entry in block.get("versions", []):
            if entry.get("versionType") not in (None, "semver", "original_commit_for_fix"):
                continue
            if entry["status"] == "unaffected" and in_range(version, entry):
                return False
    return True


def main():
    if len(sys.argv) < 3:
        sys.exit("Usage: cve_open.py <vulns/cve/published> <version> [<version> ...]")
    root, versions = sys.argv[1], sys.argv[2:]
    records = []
    for directory, _, files in os.walk(root):
        for name in files:
            if name.endswith(".json"):
                with open(os.path.join(directory, name), encoding="utf-8") as f:
                    records.append(json.load(f))
    for text in versions:
        version = parse_version(text)
        count = sum(1 for record in records if is_affected(version, record))
        print(f"{text:10} {count:>6}")


if __name__ == "__main__":
    main()
