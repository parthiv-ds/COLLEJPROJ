from setuptools import setup,find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "End-to-end-ML-Project-with-MLflow"
AUTHOR_USER_NAME = "entbappy"
AUTHOR_EMAIL = "entbappy73@gmail.com"


setup(
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for ml app",
    long_description=long_description,
    long_description_content="text/markdown",
    package_dir={"": "src"},
    packages=(find_packages(where="src")+find_packages(where="src")+find_packages(where="./Harvestify")+find_packages(where="./Fertilizer"))
)