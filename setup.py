import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thresholdmodeling", 
    version="0.0.1",
    author="Iago Pereira Lemos",
    author_email="lemosiago123@gmail.com",
    description="This package is intended for those who wish to conduct an extreme values analysis. It provides the whole toolkit necessary to create a threshold model in a simple and efficient way, presenting the main methods towards the Peak-Over-Threshold Method and the fit in the Generalized Pareto Distribution. For installing and use it, go to https://github.com/iagolemos1/thresholdmodeling",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/iagolemos1/thresholdmodeling",
    packages=['thresholdmodeling'],
    classifiers=[
        "Programming Language :: Python :: 3",
        'License :: OSI Approved :: GNU General Public License (GPL)',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires= ['numpy','scipy','rpy2','matplotlib','seaborn'])
