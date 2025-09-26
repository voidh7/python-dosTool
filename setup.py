from setuptools import setup, find_packages

setup(
    name="sherma-ddos-tool",
    version="1.0.0",
    description="Ferramenta para ataques dos/ddos.",
    author="vøidh7",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31",
        "pyfiglet>=0.8"
    ],
    entry_points={
        "console_scripts": [
            "sherma-tool = sherma.__main__:main"
        ]
    }
name="sherma-Ddos-tool"
