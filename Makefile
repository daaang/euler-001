test:
	python -m unittest && git add . && git commit -v || git status
