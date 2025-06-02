from setuptools import setup, find_packages

setup(
    name="ecommerce-analysis",
    version="1.0.0",
    author="Dinesh Royal",
    author_email="dineshroyal9121687814@gmail.com",
    description="E-commerce Sales Performance Analysis with Customer Segmentation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dineshroyal9121687814/Ecommerce-Data-Analysis",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "scikit-learn>=1.0.0",
        "scipy>=1.7.0",
    ],
)
