import setuptools

setuptools.setup(
    name='octicons16px',
    version='2020.10.22',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
