# 🌟 Description
This is an assignment from Specialisterne academy. The goal was to make a Black jack app.

This app is a UV-project, and thus UV should be used instead of pip.

# 📂 Project Structure
Project structure (hidden automatically generated files and folders like .venv not included)

```text
.
├── LICENSE
├── Nikolai Sandbeck - kravspecifikation til blackjack.pdf
├── README.md
├── __init__.py
├── dist
│   ├── blackjack-0.1.0-py3-none-any.whl
│   └── blackjack-0.1.0.tar.gz
├── docs
│   └── uv_guide.md
├── pyproject.toml
├── src
│   ├── __init__.py
│   ├── __pycache__
│   │   └── __init__.cpython-314.pyc
│   └── blackjack
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-314.pyc
│       └── components
│           ├── __init__.py
│           ├── __pycache__
│           │   ├── __init__.cpython-314.pyc
│           │   └── cards.cpython-314.pyc
│           ├── cards.py
│           └── dealer_class.py
├── tests
│   ├── __init__.py
│   └── unittests
│       ├── __init__.py
│       ├── __pycache__
│       │   └── __init__.cpython-314.pyc
│       └── components
│           ├── __init__.py
│           ├── __pycache__
│           │   ├── __init__.cpython-314.pyc
│           │   └── test_cards.cpython-314.pyc
│           └── test_cards.py
└── uv.lock
```

# Installation
Clone the repository and consult the uv_guide.md in docs on how to install UV
if you haven't it install already.

Once UV is installed, activate the environment and run `uv sync`.

# Run unittests
To run all unittests, run this line
```bash
uv run python -m unittest discover -s tests
```


