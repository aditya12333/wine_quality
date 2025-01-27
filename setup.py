from setuptools import find_packages, setup

setup(
    name="ML_project",
    version="0.0.0",
    author="aditya12333",
    author_email="adityaap3641567@gmail.com",
    description="python packages",
    url=f"https://github.com/aditya12333/wine_quality",
    project_urls={
        "Bug Tracker":f"https://github.com/aditya12333/wine_quality"
    },
    package_dir={"":"src"},
    packages=find_packages(where="src")
    )