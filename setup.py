from setuptools import setup, find_packages

setup(
    name='peract',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    license=open('LICENSE').read(),
    zip_safe=False,
    description="Perceiver-Actor: A Multi-Task Transformer for Robotic Manipulation",
    author='Mohit Shridhar',
    author_email='mshr@cs.washington.edu',
    url='https://peract.github.io/',
    keywords=['Transformer', 'Behavior-Cloning', 'Langauge', 'Robotics', 'Manipulation'],
)
