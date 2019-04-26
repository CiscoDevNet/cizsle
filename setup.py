"""cizsle setup module."""


from pathlib import Path

from setuptools import find_packages, setup


# Constants
PACKAGE_NAME = "cizsle"

KEYWORDS = [
    "cisco",
    "ztp",
    "ios-xe",
    "catalyst",
]

CLASSIFIERS = [
    "Development Status :: 3 - Alpha",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3 :: Only",
    "Programming Language :: Python :: 3.6",
    "Natural Language :: English",
    "Intended Audience :: System Administrators",
    "Intended Audience :: Telecommunications Industry",
    "Topic :: System :: Networking",
    "Topic :: System :: Installation/Setup",
    "Topic :: System :: Software Distribution",
]

DEPENDENCIES = [
    "click",
    "crayons",
    "requests>=2.20.0",
]

OPTIONAL_DEPENDENCIES = {
    "server": []
}

ENTRY_POINTS = {
    "console_scripts": [
        "cizsle = cizsle.client.__main__:main",
        "cizsle-server = cizsle.server.__main__:main [server]",
    ]
}


# Locate directories
project_root = Path(__file__).parent
package_dir = project_root/"cizsle"


# Get the app metadata
metadata = {}
with open(package_dir/"_metadata.py") as file:
    exec(file.read(), metadata)


# Get the long description from the project's README.rst file
with open(project_root/"README.rst") as file:
    long_description = file.read()


# Call setuptools.setup()
setup(
    name=PACKAGE_NAME,
    version=metadata["__version__"],
    description=metadata["__description__"],
    long_description=long_description,
    url=metadata["__url__"],
    download_url=metadata["__download_url__"],
    author=metadata["__author__"],
    author_email=metadata["__author_email__"],
    # license=metadata["__license__"] + "; " + metadata["__copyright__"],
    classifiers=CLASSIFIERS,
    keywords=" ".join(KEYWORDS),
    install_requires=DEPENDENCIES,
    extras_require=OPTIONAL_DEPENDENCIES,
    packages=find_packages(include=[PACKAGE_NAME, PACKAGE_NAME + ".*"]),
    entry_points=ENTRY_POINTS,
)
