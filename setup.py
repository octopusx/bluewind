from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f:
    requirements = f.readlines()

setup(
    name='bluewind',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'bluewind=run:main'
        ]
    }
)
