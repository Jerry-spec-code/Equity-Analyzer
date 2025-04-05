clean::
	rm -rf venv

venv::
	python3 -m venv venv \
	&& . venv/bin/activate

install::
	python3 -m pip install --no-deps --no-cache-dir -r requirements.txt

build_db::
	python3 databaseBuild.py

build::
	$(MAKE) venv \
	&& $(MAKE) install \
	&& $(MAKE) build_db

run::
	python3 app.py
