from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

# Install python package, scripts and manual pages
setup(
    name="ibf",
    version=0.1,
    author="Mathias Lohne",
    author_email="mathialo@ifi.uio.no",
    license="MIT",
    description="An interactive BrainFuck interpreter",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mathialo/interactive-brainfuck",
    scripts=["etc/ibf"],
    data_files=[("man/man1", ["etc/ibf.1"])],
    install_requires=["argparse", "readline", "numpy"],
    packages=["ibf"],
    zip_safe=False)
