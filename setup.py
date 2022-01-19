from setuptools import setup, find_packages


def read_file(file):
	with open(file, "r") as fh:
		return fh.read()

VERSION = "0.0.1"

setup(
	name="dexscreener",
	packages=find_packages(),
	version=VERSION,
	license="MIT",

	description="Query the dexscreener.com site",
	long_description=read_file("README.md"),
	long_description_content_type="text/markdown",

	author="Joshua Nixon",
	author_email="joshuanixonofficial@gmail.com",

	url="https://github.com/nixonjoshua98/dexscreener",

	download_url=f"https://github.com/nixonjoshua98/dexscreener/archive/{VERSION}.tar.gz",

	keywords=[
		"dexscreener",
		"crypto",
		"cryptocurrency"
	],

	install_requires=read_file("requirements.txt").splitlines(),

	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Software Development :: Build Tools",
	],

	python_requires='>=3.9'
)
