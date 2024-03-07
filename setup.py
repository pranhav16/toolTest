from setuptools import setup

setup(
    name='toolTest',
    version='1.0',
    description='Example tool',
    author='Pranhav Sundararajan',
    author_email='pranhav16@gmail.com',
    url='https://github.com/pranhav16/toolTest',
    py_modules=['toolTest'], 
    install_requires=[
        'csvkit', 
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
)
