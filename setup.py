from setuptools import setup

setup(name='blog-teste',
      version='0.1',
      description="Blog simples utilizando django e foundation.",
      long_description="",
      author='Alisson Barbosa Ferreira',
      author_email='contato@abftecnologia.com.br',
      license='TODO',
      packages=['blog-teste'],
      zip_safe=False,
      install_requires=[
          'Django',
          # 'Sphinx',
          # ^^^ Not sure if this is needed on readthedocs.org
          # 'something else?',
          ],
      )