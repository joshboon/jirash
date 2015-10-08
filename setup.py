from setuptools import setup

setup(
    name='Jirash',
    version='0.1.1',
    description='Jira shell utility',
    author='Pavel Savshenko',
    author_email='pavel@izzysoftware.com',
    license="MIT",
    url='https://github.com/asfaltboy/jirash',
    install_requires=['requests==2.1.0', 'soappy==0.12.5',
                      'wstools==0.3', 'fpconst==0.7.2'],
    keywords="jira shell console client",
    packages=['jirash'],
    entry_points={
        'console_scripts': ['jirash=jirash.jirashell:main'],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Utilities",
    ]
)
