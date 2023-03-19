from ensurepip import version
from gettext import install
from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    """
    This function will return list of requirements
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]



setup(
name = 'End-to-End ML Project',
version = '0.0.1',
author = 'Sachin Bhumihar',
author_email= 'bhumiharsachin0@gmail.com',
packages= find_packages(),
install_requires = get_requirements('requirements.txt')




    
)
