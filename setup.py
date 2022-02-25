# Library to configure this setup file
import pathlib
from setuptools import find_packages, setup

# VERSION - is a variable that is defined in the __init__.py file
VERSION = "0.1.0"

HERE = pathlib.Path(__file__).parent
PACKAGE_NAME = 'atomico' #Debe coincidir con el nombre de la carpeta 
AUTHOR = 'Jose Manuel Napoles'
AUTHOR_EMAIL = 'jnapoles@uach.mx'
URL = 'https://github.com/napoles-uach/atomico'

LICENSE = 'MIT' #Tipo de licencia
DESCRIPTION = 'atomico para curso'
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8')
LONG_DESC_TYPE = "text/markdown"
PROJECT_URLS = {
                #"Documentation": "https://streamlit-book.readthedocs.io/",
                'Source': 'https://github.com/napoles-uach/atomico',
                #'Tracker': 'https://github.com/sebastiandres/streamlit_book/issues',
                }
# Libraries required by the package
INSTALL_REQUIRES = ['mendeleev', 'pandas']

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    include_package_data=True,    
    url=URL,
    project_urls=PROJECT_URLS,
    license=LICENSE,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    setup_requires=INSTALL_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    )