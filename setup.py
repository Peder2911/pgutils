
import setuptools

with open("README.md") as f:
    long_description=f.read()

setuptools.setup(
        name = "pgutils",
        version = "0.0.1",
        author = "Peder G. Landsverk",
        author_email = "pglandsverk@gmail.com",
        description = "Tools for quick testing with Postgres DB",
        long_description = long_description,
        long_description_content_type="test/markdown",
        url = "https://www.github.com/peder2911/pgtestutils",
        packages = setuptools.find_packages(),
        python_requires=">=3.7",
        install_requires=[
            "docker==4.3.1",
            "psycopg2==2.8.6",
        ])
