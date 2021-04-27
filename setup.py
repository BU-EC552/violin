from setuptools import find_packages, setup


def read_requirement():
    with open("requirement.txt", "r") as req:
        content = req.read()
        requirement = content.split("\n")

    return requirement


setup(
    name="violin",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read_requirement(),
    entry_points="""
        [console_scripts]
        violin=CLI.cli:cli
    """,
)