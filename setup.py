from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT='-e .'
def get_requirements(file_path: str) -> List[str]:
    """
    Extracts a list of requirements from a text file.

    Args:
        file_path (str): The path to the text file containing requirements.

    Returns:
        list: A list of requirements extracted from the file. Each requirement
              is represented as a string element in the list.
    """
    requirements=[]
    with open(file_path) as file:
        requirements=file.readlines()
        requirements = [req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject',
    version='0.0.1',
    author='Mack',
    author_email='shonayimack@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

com.databricks:spark-xml_2.12:0.17.0