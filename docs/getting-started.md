# Install python
This project was written in python 3.12.3

# Install Git
If you are a windows user, run this commands in PowerShell:
```bash
winget install --id Git.Git -e --source winget
```

# Install Poetry
* **Poetry**: This project uses Poetry for dependency management.
You can install poetry running  
```bash
pip install poetry
```

# Download project
In your terminal, run 
```bash 
git clone https://github.com/codingfromrio/simple-excel-etl.git
```

# Go to project folder
```bash
cd simple-excel-etl
```

# Config python poetry version and activate venv
```bash
poetry env use 3.12.3
poetry shell
```

# Install dependencies
```bash
poetry install
```

# Run tests to check everithing is ok
```bash
task test
```

# Run main.py to run this project
```bash
python app/main.py
```