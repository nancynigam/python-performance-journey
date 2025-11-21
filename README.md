# python-performance-journey

## Summary

## Steps
1. python3.11 -m venv .venv311
2. source .venv311/bin/activate
3. pip install -U py-spy
4. sudo py-spy record -o profile.svg -- python slow_app.py
5. Move venv to gitignore before committing (echo ".venv311/" >> .gitignore)

## Output
<img width="1719" height="220" alt="Screenshot 2025-11-20 at 7 47 09 PM" src="https://github.com/user-attachments/assets/933015a3-d5a7-4c70-8834-393e1385e056" />
