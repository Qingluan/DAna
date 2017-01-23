

from setuptools import setup, find_packages


setup(name='DAna',
    version='0.1',
    description='a lib for data computing.',
    url='https://github.com/Qingluan/.git',
    author='Qing luan',
    author_email='darkhackdevil@gmail.com',
    license='MIT',
    zip_safe=False,
    packages=find_packages(),
    install_requires=['pandas','jieba'],
)


