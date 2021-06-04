import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="muchscript",
    version="0.1.3",
    description="A crypto language inspired by Doge and Papa Elon",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shaurya-blip/muchscript/",
    author="Shaurya Pratap Singh",
    author_email="shaurya.p.singh21@gmail.com",
    license="MIT",
    packages=["muchscript"],
    include_package_data=True,
    scripts=['bin/much']
)
