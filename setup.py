from setuptools import find_packages, setup

with open("README.md", "r") as fh:
  long_description = fh.read()

setup(
    name='walle',
    version='0.2.0',
    author='Kevin Zakka',
    author_email="kevinarmandzakka@gmail.com",
    description='Robotics Research Toolkit',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/kevinzakka/walle',
    python_requires='>=3.6.0',
    keywords='ai robotics vision',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests",)),
    install_requires=[
        'numpy>=1.0.0,<2.0.0',
        'scikit-image>=0.13.0,<2.0.0',
    ],
    extras_require={
        "rs2": ["pyrealsense2>=2.22"],
    }
)
