from setuptools import setup, find_packages

with open("requirements.txt") as f:
    required = f.read().splitlines()

with open("teacher_requirements.txt") as f:
    teacher_required = f.read().splitlines()


setup(
    name="calculator",
    version="0.0.1",
    description="A simple calculator package.",
    author="Ander Fernández",
    author_email="anderfernandezj@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=required,
    extras_require={"teacher": teacher_required},
    python_requires=">=3.8",
)