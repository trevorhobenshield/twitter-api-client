import os
import re
from codecs import open

from setuptools import find_packages, setup

install_requires = [
    "aiofiles",
    "websockets",
    "nest_asyncio",
    "httpx",
    "tqdm",
    "orjson",
    'uvloop; platform_system != "Windows"',
]

about = {}
here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, "twitter", "__version__.py"), "r", "utf-8") as f:
    exec(f.read(), about)
with open("readme.md", "r", "utf-8") as f:
    readme = f.read()
temp = re.sub('\n\!\[\]\(assets\/[\w-]+\.\w+\)\n', '', readme)
pypi_readme = re.sub('### Example API Responses.*', '', temp, flags=re.DOTALL)

setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    description=about['__description__'],
    license=about['__license__'],
    long_description=pypi_readme,
    python_requires=">=3.10.10",
    long_description_content_type='text/markdown',
    author_email='trevorhobenshield@gmail.com',
    url='https://github.com/trevorhobenshield/twitter-api-client',
    install_requires=install_requires,
    keywords='twitter api client async search automation bot scrape',
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
