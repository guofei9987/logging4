from setuptools import setup, find_packages
import os
import logging4

this_directory = os.path.abspath(os.path.dirname(__file__))


def read_file(filename):
    with open(os.path.join(this_directory, filename), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


def read_requirements(filename):
    return [line.strip() for line in read_file(filename).splitlines()
            if not line.startswith('#')]


setup(
    name='logging4',  # 包的名字，也是将来用户使用 pip install scikit-opt 来安装
    version=logging4.__version__,
    packages=find_packages(),
    python_requires='>=3.5',
    install_requires=[],  # 指定此包的依赖
    description='A tiny logging tool',
    long_description=read_file('README.md'),
    long_description_content_type="text/markdown",
    url='https://github.com/guofei9987/logging4',  # 随意填写，一般是项目的 github 地址
    author='Guo Fei',
    author_email='guofei9987@foxmail.com',
    license='MIT',
    platforms=['linux', 'windows', 'macos'],
    zip_safe=False,  # 为了兼容性，一般填 False
)
