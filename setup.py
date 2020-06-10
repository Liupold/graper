import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="graper",
    version="0.0.1",
    author="Rohn Chatterjee",
    author_email="rohn.ch@gmail.com",
    description="Making paper graph a breeze",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Liupold/graper",
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=['numpy', 'click', 'pyyaml', 'pillow'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3 or later (AGPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
    ],
    python_requires='>=3.5',
)
