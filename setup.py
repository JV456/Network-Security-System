from typing import List

from setuptools import find_packages, setup


def get_requirements()->List[str]:
    """
    This function will return list of requirements
    
    """
    requirement_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            #Read lines form the file
            lines=file.readlines()
            #process each line
            for line in lines:
                requirement=line.strip()
                ## ignore the empty line and -e.
                if requirement and requirement!= '-e .':
                    requirement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    
    return requirement_lst

setup(
    name='Network Security System',
    version="0.0.1",
    author="Jai Vadula",
    author_email="jaivadula@gmail.com",
    packages=find_packages(),
    install_requirements=get_requirements()
)