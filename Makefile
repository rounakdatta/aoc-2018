aoc:
	python3 main.py $(day) $(part)

clean:
	find . -name "__pycache__" | xargs rm -rf