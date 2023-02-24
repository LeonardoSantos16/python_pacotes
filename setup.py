from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculadora_pacote",
    version="0.0.1",
    author="Leonardo dos Santos Mendes Ferreira",
    author_email="leodsmf@gmail.com",
    description="Testando a criação de um pacote em python, utilizando uma calculadora simples",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LeonardoSantos16/criando_pacotes.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)