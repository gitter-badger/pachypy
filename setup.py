from setuptools import setup, find_packages

setup(
    name='pachypy',
    version='0.1.1',
    author='Simon Gurcke',
    packages=find_packages(),
    install_requires=[
        'python_pachyderm>=1.8.5',
        'python-dxf>=7.5.0',
        'boto3>=1.9.119'
        'pandas>=0.24.2',
        'pyyaml>=3.13',
        'tzlocal>=1.5.1',
        'termcolor>=1.1.0',
    ],
    extras_require={
        'docs':  [
            'sphinx_rtd_theme>=0.4.3',
            'sphinx_autodoc_typehints>=1.6.0',
        ],
        'test': [
            'pytest>=4.3.1',
            'pytest-cov>=2.6.1',
        ]
    }
)
