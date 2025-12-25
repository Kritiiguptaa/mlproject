## Building application as a package itself

from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    ''' This function will return list of requirements '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

# -e . is used by pip to install the current project in editable mode(install package "pip install -e .") and should not be included in 
# install_requires, which is why it is removed before iteration in setup.py.

# lets say i write -e . in requirements then -e . will search for setup.py to run but in setup.py we say to install all requirements
# (thus will insatll -e . also which we do not want thus we write if -e . found remove it)

setup(
    name='mlproject',
    version='0.0.1',
    author='Kriti',
    author_email='kgupta12_be23@thapar.edu',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
    # install_requires=['pandas','numpy','seaborn']
)