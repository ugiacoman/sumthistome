from setuptools import setup

dependecies = [
    "beautifulsoup4",
    "requests",
    "Flask",
    "selenium"
]

setup(
	name = "sumthistome",
	verison = "0.0.1",
	install_requires=dependecies
)