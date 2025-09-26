from setuptools import setup, find_packages

setup(
    name="sherma-ddos-tool",
    version="0.1.0",
    description="Ferramenta educativa para testar requisições em servidores locais (uso autorizado apenas).",
    author="Seu Nome",
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
name="sherma-tool"
