from setuptools import find_packages, setup

if __name__ == "__main__":
    setup(
        name="jaffle",
        packages=find_packages(exclude=["jaffle_tests"]),
        install_requires=[
            "dagster==1.1.10",
            "pandas==1.5.3",
            "duckdb==0.6.1",
            "sqlescapy==1.0.1",
            "html5lib==1.1",
            "lxml==4.9.2",
        ],
        extras_require={
            "dev": ["dagit==1.1.10", "pytest", "localstack==1.0.4", "awscli==1.27.52", "awscli-local==0.20"]
        },
    )
