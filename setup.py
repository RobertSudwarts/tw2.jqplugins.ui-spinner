from setuptools import setup, find_packages

major=0
minor=1
micro=0

f = open('README.rst')
long_description = f.read().strip()
f.close()

# Requirements to install buffet plugins and engines
_extra_genshi = ["Genshi >= 0.3.5"]
_extra_mako = ["Mako >= 0.1.1"]

setup(
    name='tw2.jqplugins.ui_spinner',
    version='%d.%d.%d' % (major, minor, micro),
    description='toscawidgets2 widget for TextField with spinner',
    long_description=long_description,
    author='Robert Sudwarts',
    author_email='robert.sudwarts@gmail.com',
    url='https://github.com/RobertSudwarts/tw2.jqplugins.ui-spinner',
    install_requires=[
        "tw2.core",
        "tw2.jquery",
        "tw2.jqplugins.ui",
        ],
    extras_require = {
        'genshi': _extra_genshi,
        'mako': _extra_mako,
    },
    tests_require = ['BeautifulSoup', 'nose', 'FormEncode', 'WebTest',] \
                     + _extra_genshi + _extra_mako,
    packages=find_packages(exclude=['ez_setup', 'tests']),
    namespace_packages = ['tw2'],
    zip_safe=False,
    include_package_data=True,
    test_suite = 'nose.collector',
    entry_points="""
        [tw2.widgets]
        # Register your widgets so they can be listed in the WidgetBrowser
        widgets = tw2.jqplugins.ui_spinner
    """,
    keywords = [
        'toscawidgets.widgets',
    ],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Environment :: Web Environment :: ToscaWidgets',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Widget Sets',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
