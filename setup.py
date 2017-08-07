from setuptools import setup, find_packages

setup(
    name='mapbpoxgl',
    version='0.1.0',
    description=u"MapboxGL plugin for Jupyter Notebooks",
    long_description="Use Mapbox GL natively in your Jupyter Notebook workflows",
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Scientific/Engineering :: GIS'],
    author=u"Ryan Baumann",
    url='https://github.com/mapbox/mapboxgl-jupyter',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=['jupyter'],
    extras_require={
        'test': ['pytest', 'pytest-cov', 'codecov']})
