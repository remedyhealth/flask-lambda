from setuptools import setup


with open('README.rst') as f:
    long_description = f.read()

setup(
    name='flask-lambda-support',
    version='0.1.2',
    description='Python 3.6+ module to make Flask compatible with AWS Lambda',
    long_description=long_description,
    keywords='flask aws amazon lambda',
    author='Jochen Van de Velde',
    author_email='jochen.vandevelde@cloudway.be',
    url='https://github.com/becloudway/flask-lambda',
    license='Apache License, Version 2.0',
    py_modules=['flask_lambda'],
    install_requires=['Flask>=0.10'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Environment :: Console',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
    ]
)
