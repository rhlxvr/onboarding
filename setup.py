from setuptools import setup, find_packages

setup(
    name='obapp',
    version='2.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=4.2.3,<5.0',
        'asgiref==3.8.1',
        'beautifulsoup4==4.12.3',
        'crispy-bootstrap4==2024.1',
        'django-bootstrap4==24.3',
        'django-crispy-forms==2.1',
        'django-extensions==3.2.3',
        'soupsieve==2.5',
        'sqlparse==0.5.0',
    ],
    entry_points={
        'console_scripts': [
            'manage.py = myproject.manage:main',
        ],
    },
    author='Marvin Wagle',
    author_email='marvin.wagle@icloud.com',
    description='Onboarding Project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/rhlxvr/onboarding',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
