import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_file(file_name):
    with open(file_name, 'r') as f:
        return f.read()


setuptools.setup(
    name='telegraf-xiaomi-air-purifier',
    description='Telegraf plugin for Xiaomi Air Purifier',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.2',
    url='https://github.com/SebastianCzoch/telegraf-xiaomi-air-purifier',
    author='Sebastian Czoch',
    author_email='sebastian@czoch.pl',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
    ],
    packages=setuptools.find_packages(),
    install_requires=read_file('requirements.txt').splitlines(),
    scripts=['telegraf-xiaomi-air-purifier'],
    setup_requires=[
        "flake8"
    ]
    )
