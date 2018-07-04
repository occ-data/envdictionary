from setuptools import setup, find_packages

setup(
    name='gdcdictionary',
    version='0.0.0',
    packages=find_packages(),
    install_requires=[
        'dictionaryutils',
    ],
    dependency_links=[
       "git+https://github.com/uc-cdis/dictionaryutils.git@0d462e7d15b93af46c17ede74f0db9ca56312202#egg=dictionaryutils",
    ],
    package_data={
        "gdcdictionary": [
            "schemas/*.yaml",
            "schemas/projects/*.yaml",
            "schemas/projects/*/*.yaml",
        ]
    },
)
