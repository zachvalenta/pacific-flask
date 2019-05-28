.PHONY: test

help:
	@echo
	@echo "🐛 UTIL"
	@echo
	@echo "run:     	start app"
	@echo "fmt:     	auto format code using Black"
	@echo "repl:    	debug using bpython"
	@echo
	@echo "�📦 DEPENDENCIES"
	@echo
	@echo "freeze:   	freeze dependencies into requirements.txt"
	@echo "install:   	install dependencies from requirements.txt"
	@echo "reset:   	remove any installed pkg *not* in requirements.txt"
	@echo

run:
	source venv/bin/activate; export FLASK_APP=pacific; export FLASK_ENV=development; flask run

drop:
	qing local.db; touch local.db

fmt:
	black src test

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

reset:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo

repl:
	bpython
