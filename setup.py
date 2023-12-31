from setuptools import setup
from pathlib import Path

parent_path = Path(__file__).parent
long_description = (parent_path/"binarycalculation/README.md").read_text()

setup(
    name="binarycalculation",
    version="1.5",
    description="Binary Number Calculations",
    packages=['binarycalculation'],
    author="Josi Kie N.",
    author_email="kiejosi12@gmail.com",
    zip_safe=False,
    long_description=long_description,
    long_description_content_type="text/markdown"
)