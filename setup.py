from setuptools import setup, find_packages

setup(
    name='zaifexport',
    version='0.1.0',
    author='tetocode',
    packages=find_packages(),
    install_requires=['docopt', 'python-dateutil', 'pytz', 'zaifapi'],
    description='export tool for zaif',
    entry_points={
        'console_scripts': 'zaifexport=zaifexport.main:main'
    },
    license='MIT',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python3',
        'Topic :: Utilities'
    ]
)
