install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=wikiphrases --cov=nlplogic test_corenlp.py

format:
	black *.py nlplogic

run:
	#jupyter nbconvert --execute --to notebook --inplace my_collab_notebook.ipynb &&\
	#python get_url_data.py &&\
	#python dask_kmeans.py


lint:
	pylint --disable=R,C *.py nlplogic/*.py

all: install format lint test run