from setuptools import setup, find_packages

setup(
    name='a-share-code-converter',  # PyPI 包名（连字符推荐）
    version='0.1.0',
    description='A lightweight Python utility to convert A-share stock codes to various formats',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Tom Baker',
    author_email='tomtang0619@gmail.com',
    url='https://github.com/yourusername/a-share-code-converter',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.20',
        'pandas>=1.3',
        'polars>=0.18',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.7',
)
