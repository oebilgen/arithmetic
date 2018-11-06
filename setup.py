from setuptools import setup

setup(
    name='arithmetics',
    version='0.2.0',
    author='Ozan Eren Bilgen',
    author_email='oebilgen@gmail.com',
    packages=['arithmetics', 'arithmetics.test'],
    url='https://github.com/oebilgen/arithmetics',
    license='MIT',
    description='Python arithmetics for very long numbers.',
    long_description=open('README.txt').read(),
    keywords='arithmetic math floating point multiplication subtraction addition precision decimal rounding'
)
