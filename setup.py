import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.1"

Repo_name = "WebNest"
Author_name = "Vedant Gulhane"
Author_email = "vedantgulhane203@gmail.com"
SRC_DIR = "WebNest"

setuptools.setup(
    name=Repo_name,
    version=__version__,
    author=Author_name,
    author_email=Author_email,
    description="A home for web resources inside notebooks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{Author_name}/{Repo_name}",
    project_urls={      
        
        "Bug Tracker": f"https://github.com/{Author_name}/{Repo_name}/issues"
    },
    package_dir={"": f"src/{SRC_DIR}"},
    packages=setuptools.find_packages(where=f"src/{SRC_DIR}"),
)
