import setuptools

setuptools.setup(
    name='octicons16px',
    version='2021.1.11',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
