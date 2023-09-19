import setuptools

__version__ = "0.0.0"
REPO_NAME = "VECH"
AUTHOR_USER_NAME = "Musician9dx"
SRC_REPO = "VECH"
AUTHOR_EMAIL = "musician9dx@gmail.com"

setuptools.setup(
    name="VECH",
    version=__version__,
    author="Musician9dx",
    author_email="musician9dx@gmail.com",
    description="nops performed",
    url="https://github.com/Musician9dx/VECH",
    project_urls={
        "Bug Tracker": "https://github.com/Musician9dx/VECH" + "/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
