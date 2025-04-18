from setuptools import setup, find_packages

setup(
    name="Custom_Widgets",
    version="0.1.0",
    author="himaj joshi",
    author_email="himajjoshi932@gmail.com",
    description="A Python package for ROS2 integration with FROS user interface",
    url="https://github.com/himaj47/Qt-FROS-Custom-Widget",
    packages=find_packages(),
    install_requires=[
        "PySide2>=5.15.2",
        "setuptools",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    entry_points={
        "console_scripts": [
        ],
    },
)
