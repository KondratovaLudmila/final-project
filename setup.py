from setuptools import setup, find_packages

setup(
    name='bot_helper',
    version='0.0.1',
    packages=find_packages(),
    author='group_5',
    description='bot-helper',
    install_requires = ['tqdm','colorama'],
    entry_points={
        'console_scripts': [
            'mycli = final-project.main:main'
        ],
    },
)