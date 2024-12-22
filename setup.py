from setuptools import setup, find_packages
import os


def read_long_description():
    with open(os.path.join(os.path.dirname(__file__), "README.md"), "r") as f:
        return f.read()


setup(
    name="Gold ERP",
    version="1.0.0",
    description="A brief description of what your app does",
    long_description=read_long_description(),
    long_description_content_type="text/markdown",
    author="Feroz Mirza",
    author_email="m.ferozmirza2005@gmail.com",
    url="https://github.com/mferozmirza2005",
    packages=find_packages(),
    install_requires=[
        "PyQt5",
    ],
    entry_points={
        "console_scripts": [
            "golderp=gold_erp.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    include_package_data=True,
    package_data={
        "": [
            "assets/*",
            "resources/*",
        ],
    },
    python_requires=">=3.6",
    zip_safe=False,
)
