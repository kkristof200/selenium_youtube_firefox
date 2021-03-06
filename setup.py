import setuptools, os

readme_path = 'README.md'

if os.path.exists(readme_path):
    with open(readme_path, 'r') as f:
        long_description = f.read()
else:
    long_description = 'selenium_youtube_firefox'

setuptools.setup(
    name='selenium_youtube_firefox',
    version='0.0.2',
    author='Kristóf-Attila Kovács',
    description='selenium_youtube_firefox',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/kkristof200/selenium_youtube_firefox',
    packages=setuptools.find_packages(),
    install_requires=[
        'kproxy>=0.0.2',
        'selenium-firefox>=2.0.7',
        'selenium-youtube>=2.0.3'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.4',
)