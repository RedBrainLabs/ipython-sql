from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'

install_requires = [
    'texttable',
    'ipython>=0.13',
    'pyzmq >= 2.1.4', 
]


setup(name='ipython-sql',
    version=version,
    description="RDBMS access via IPython",
    long_description=README + '\n\n' + NEWS,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Topic :: Database',
    ],
    keywords='database ipython postgresql mysql',
    author='Catherine Devlin',
    author_email='catherine.devlin@gmail.com',
    url='pypi.python.org/pypi/ipython-sql',
    license='MIT',
    packages=find_packages('src'),
    package_dir = {'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
)
