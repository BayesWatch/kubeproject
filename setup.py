#!/usr/bin/env python

from distutils.core import setup

setup(
    name="bwatchcompute",
    version="0.1.0",
    description="A set of tools built to simplify daily driving of cloud resources for individual VM access, Kubernetes batch jobs and miscellaneous useful functionality related to cloud-based ML research",
    author="Antreas Antoniou",
    author_email="iam@antreas.io",
    packages=["bwatchcompute"],
    package_data={"": ["bwatchcompute/templates/*"]},
    include_package_data=True,
    install_requires=["quote", "rich", "randomname", "pyyaml"],
)
