from setuptools import setup, find_packages

setup(
  name = 'hebpipe',
  packages = find_packages(),
  version = '3.0.0.6',
  description = 'A pipeline for Hebrew NLP',
  author = 'Amir Zeldes',
  author_email = 'amir.zeldes@georgetown.edu',
  package_data = {'':['README.md','LICENSE.md','requirements.txt'],'hebpipe':['lib/*','data/*','bin/*','models/models_go_here.txt','models/stanza/stanza_models_here.txt']},
   install_requires=['requests','numpy>=1.18.5,<2.0','gensim==4.3.3', "transformers==4.38.0", "torch==2.2.0", 'pandas', 'scipy>=1.7.0,<1.14.0', 'joblib', 'xgboost==0.81', 'rftokenizer', 'depedit', 'xmltodict', 'diaparser==1.1.2', 'flair==0.6.1', 'stanza==1.2.3', 'conllu', 'protobuf==3.20.*'],
  url = 'https://github.com/danelkay93/HebPipe',
  license='Apache License, Version 2.0',
  download_url = 'https://github.com/danelkay93/HebPipe/releases/tag/v3.0.0.6',
  keywords = ['NLP', 'Hebrew', 'segmentation', 'tokenization', 'tagging', 'parsing','morphology','POS','lemmatization'],
  classifiers = ['Programming Language :: Python',
'Programming Language :: Python :: 2',
'Programming Language :: Python :: 3',
'License :: OSI Approved :: Apache Software License',
'Operating System :: OS Independent'],
)
