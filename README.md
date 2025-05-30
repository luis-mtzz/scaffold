# Scaffolder

This project is dedicated to providing a modular scaffolding tool for starter templates for common use-cases I run into for Python and JavaScript applications. I have included template configurations, basic starter code, and util scripts for project setup.

## Directory Structure

```txt
├── assets
│   └── repomix
│       ├── instructions.md
│       └── repomix.config.json
├── mkproject
├── README.md
└── templates
    ├── javascript
    │   ├── express
    │   ├── fastify
    │   └── standard
    └── python
        ├── etl
        ├── fastapi
        └── standard
            ├── pyproject.toml
            ├── setup.sh
            ├── src
            │   ├── app
            │   │   ├── __init__.py
            │   │   └── main.py
            │   └── utils
            │       └── logger.py
            └── tests
                └── test_main.py
```

## Features

- **Prebuilt Templates:** Starter templates for FastAPI, ETL scripts, Express, Fastify, and generic projects.
- **Extensibility:** Add new language/framework templates under `templates/`.
- **Utilities:** Common utilities to skip boilerplate code.
- **Repomix Configuration:** My personal [repomix](https://repomix.com/) configuration and `instructions.md` for better results when developing with AI.

## Usage

```bash
# List available templates
mkproject list

# Output
Available project templates (language/type):
  - python/etl
  - python/standard
  - python/fastapi
  - javascript/express
  - javascript/standard
  - javascript/fastify
```

```bash
# To create a new project

mkproject python fastapi testProject

# Output
Creating new project 'testProject' using 'python/fastapi' template...
Creating .gitignore...
  Added 'repomix/' to .gitignore
Initialized empty Git repository in ./testProject/.git/
Executing project setup script...
Making Python dev environment...
Creating virtual environment using uv...
Using CPython 3.12.9 interpreter at: /opt/homebrew/opt/python@3.12/bin/python3.12
Creating virtual environment at: .venv
Activate with: source .venv/bin/activate
Activating virtual environment...
Installing development depdendencies from pyproject.toml...
Resolved 65 packages in 30ms
   Built testproject @ ./testProject
Prepared 1 package in 576ms
Installed 65 packages in 74ms
...
Installing pre-commit hooks...
pre-commit installed at .git/hooks/pre-commit
Setup complete.

Use 'source ./setup.sh' to activate environment and set PYTHONPATH.
Project setup script completed. Removing from project.
Created 'testProject' @ './testProject'
```

## Requirements

- Python 3.12+
- Node.js
- Bash

## Contributing

Feel free to fork and use for your own needs. May eventually turn this into a library, idk.

## License

MIT License. See `LICENSE` for details.
