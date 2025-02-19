from setuptools import setup

setup(
    name="fastapi-dash",
    version="0.1.0",
    py_modules=["app"],
    entry_points={
        "console_scripts": [
            "main=app:app",
        ]
    },
    python_requires=">=3.13",
)
