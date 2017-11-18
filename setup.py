try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='rpaste',
    packages=['rpaste'],
    version='0.1.4',
    description='Code Snippets Uploader',
    author='Anup Pokhrel',
    author_email='virtualanup@gmail.com',
    install_requires=['pyperclip', 'requests'],
    url='https://github.com/rpaste/rpaste',
    keywords=['rpaste', 'paste', 'bin'],
    classifiers=[],
    entry_points={
        "console_scripts": [
            "rpaste=rpaste:main",
        ]
    },
)
