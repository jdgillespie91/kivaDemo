from setuptools import setup, find_packages

setup(
    name='ingest',
    version='1.0.0',
    packages=find_packages(exclude=['tests']),
    description='A flask application that pulls data from the Kiva API and stores it in a Postgres database',
    author='Jake Gillespie',
    author_email='jdgillepsie91@gmail.com',
    zip_safe=True,
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
        'flask',
        'gunicorn',
        'psycopg2',
        'requests',
    ],
)
