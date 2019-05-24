from setuptools import setup, find_packages


setup(
      name='colorpool',
      version='1.0.0',
      url='https://github.com/gudeqing/colorpool',
      license='MIT',
      author='gudeqing',
      author_email='822466659@qq.com',
      description='Generate a distinct color pool for plot',
      packages=find_packages(exclude=['tests', 'docs']),
      long_description=open('README.md').read(),
      zip_safe=False,
      classifiers = [
            "Development Status :: 1 - Alpha",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
            "Intended Audience :: Science/Research",
            "Topic :: Scientific/Engineering :: bio informatics"
        ],
      install_requires=["colorlover", "colorsys"],
      setup_requires=[],
)
