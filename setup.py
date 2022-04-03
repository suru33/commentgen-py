import setuptools

setuptools.setup(
    name='commentgen',
    version='1.0.0',
    description='Generate comments',
    url='https://github.com/suru33/commentgen',
    author='SuRu',
    author_email='33urus@gmail.com',
    license='MIT License',
    python_requires='>=3.6',
    install_requires=['Click'],
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'commentgen=commentgen:cli',
        ],
    },
)
