from setuptools import setup, find_packages

setup(
    name='scalability-optimization-framework',  # Name of the project
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        'tensorflow>=2.0.0',  # Required version of TensorFlow
        'numpy',              # Required version of NumPy
        'pandas',             # Required version of Pandas
    ],
    author='Your Name',  # Your name or team name
    author_email='your_email@example.com',  # Your email address
    description='A framework to enhance scalability and performance of machine learning models in TensorFlow.',  # Brief description of the project
    url='https://github.com/MarcoWrightk/scalability-optimization-framework',  # URL of the repository
    classifiers=[
        'Programming Language :: Python :: 3',  # Python version
        'License :: OSI Approved :: MIT License',  # License type
        'Operating System :: OS Independent',  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum required Python version
)
