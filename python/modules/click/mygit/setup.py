from setuptools import setup

setup(
    name = 'mygit',
    version = '1.0.0',
    py_modules = ['mygit'],
    install_requires = [
        'click', 
    ],
    entry_points = {
        'console_scripts': [
            'mygit=mygit:mygit',
        ],
    },
)
