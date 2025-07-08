from setuptools import find_packages, setup

setup(
    name="datalib_dagster_project_scaffold_ped",
    packages=find_packages(exclude=["datalib_dagster_project_scaffold_ped_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud"
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
