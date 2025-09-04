from setuptools import find_packages, setup


def read_file(file):
	with open(file, "r") as fh:
		return fh.read()

# pip install build twine
# py -m build
# py -m twine upload dist/*


setup(
	name="dexscreener",
	packages=find_packages(),
	version="1.3",
	license="MIT",

	description="Python wrapper for the 'dexscreener.com' API",
	long_description=read_file("README.md"),
	long_description_content_type="text/markdown",

	author="Joshua Nixon",
	author_email="nixonjoshua98@gmail.com",

	url="https://github.com/nixonjoshua98/dexscreener",

	download_url="https://github.com/nixonjoshua98/dexscreener/releases",

	keywords=[
		"dexscreener",
		"crypto",
		"cryptocurrency",
		"bitcoin"
	],

	install_requires=[
		"requests",
		"pydantic",
		"certifi",
		"aiohttp"
	],

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
