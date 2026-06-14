# Automation Tool Project

This project contains two Python scripts for generating a dated log file and fetching sample data from an API.

## Files

- `generate_log.py` - Generates a timestamped log file from a list of entries.
- `script.py` - Generates a log and fetches a sample post from `jsonplaceholder.typicode.com`.
- `requirements.txt` - Lists project dependencies.
- `venv/` - Local virtual environment directory (should not be committed).

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the log generator:

```bash
python generate_log.py
```

Run the example script:

```bash
python script.py
```

Both scripts will create a file named `log_YYYYMMDD.txt` in the current directory.

## Notes

- The `venv/` directory is purposely ignored and should not be pushed to version control.
- `requirements.txt` contains only the packages required to run the scripts.
