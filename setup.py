from setuptools import setup, find_packages

setup(
    name='HC',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            "HC=source.__main__:main",
        ],
    },
)