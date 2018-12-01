aoc:
	python3 main.py $(day) $(part)

clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf