from setuptools import setup, find_packages

setup(
    name='clld-cognacy-plugin',
    version='0.1.0',
    description='clld-cognacy-plugin',
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    url='https://github.com/clld/clld-cognacy-plugin',
    keywords='web pyramid pylons',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld>=3.3.3',
        'sqlalchemy',
        'zope.interface',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'pytest>=3.6',
            'pytest-mock',
            'mock',
            'coverage>=4.2',
            'pytest-cov',
            'webtest',
        ],
    },
    license="Apache 2.0",
)
