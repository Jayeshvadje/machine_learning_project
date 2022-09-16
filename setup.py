from setuptools import setup
from typing import List


PROJECT_NAME= "housing-predictor"
VERSION="0.0.1"
AUTHOR="jayesh"
DESCRIPTION="this is my first machinea learning project"
PACKAGES=["housing"]
REQUIREMNTS_FILE_NAME="requirements.txt"

def get_requirements_list()->List[str]:
    '''this function is going to return a list which contain the name
    of libraries mention in the requirments.txt'''


    with open(REQUIREMNTS_FILE_NAME) as requirements_file:
        return requirements_file.readlines()





setup(
    namae=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=PACKAGES,
    install_requires=get_requirements_list()

)

if __name__== "__main__":
    print(get_requirements_list())
