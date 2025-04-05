clean::
	rm -rf venv

build::
	python3 -m venv venv \
	&& . venv/bin/activate \
	&& python3 -m pip install --no-cache-dir -r requirements.txt \
	&& python3 databaseBuild.py

run::
	python3 app.py
