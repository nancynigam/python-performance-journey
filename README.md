# python-performance-journey

## Steps
1. python3.11 -m venv .venv311
2. source .venv311/bin/activate
3. pip install -U py-spy
4. sudo py-spy record -o profile.svg -- python slow_app.py
