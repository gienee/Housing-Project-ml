from setuptools import find_packages,setup   ### used to install the requirements,txt file, we do not need to use pip install.
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:  ### it is going to give us the list of string datatype which contained all the libraries mentioned in the requirements.txt file.
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
    

setup(
    name='housing-predictor',
    version='0.0.1',
    author='Nikita',
    author_email='nikitathakur9938@gmil.com',
    install_requires=get_requirements('requirements.txt'),
    packages=find_packages()
)
   