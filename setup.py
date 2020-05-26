import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

requires = [
    'amqp == 2.5.2',
    'billiard == 3.6.3.0',
    'bleach == 3.1.5',
    'celery == 4.4.2',
    'certifi == 2020.4.5.1',
    'chardet == 3.0.4',
    'click == 7.1.2',
    'docutils == 0.16',
    'Flask == 1.1.2',
    'idna == 2.9',
    'importlib - metadata == 1.6.0',
    'itsdangerous == 1.1.0',
    'Jinja2 == 2.11.2',
    'keyring == 21.2.1',
    'kombu == 4.6.8',
    'MarkupSafe == 1.1.1',
    'numpy == 1.18.3',
    'opencv - python == 4.2.0.34',
    'packaging == 20.4',
    'pkginfo == 1.5.0.1',
    'Pygments == 2.6.1',
    'pyparsing == 2.4.7',
    'pytz == 2020.1',
    'pywin32 - ctypes == 0.2.0',
    'readme - renderer == 26.0',
    'requests == 2.23.0',
    'requests - toolbelt == 0.9.1',
    'six == 1.15.0',
    'tqdm == 4.46.0',
    'twine == 3.1.1',
    'urllib3 == 1.25.9',
    'vine == 1.3.0',
    'webencodings == 0.5.1',
    'Werkzeug == 1.0.1',
    'zipp == 3.1.0',
]

setuptools.setup(
    name='dbtos3',
    version='0.0.2-alpha',
    description='Replication & Full Load Application for multiple databases to s3',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='DirkSCGM',
    author_email='dirkscgm@gmail.com',
    url='https://github.com/DirksCGM/DBtoS3',
    classifiers=['Programming Language :: Python :: 3 :: Only'],
    packages=setuptools.find_packages(),
    install_requires=requires,
    python_requires='>=3.6',
    keywords=['postgres', 's3', 'aws', 'mysql']
)
