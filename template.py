import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name1 = "Harvestify"
project_name2 = "Fertilizer"



list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name1}/__init__.py",
    f"src/{project_name1}/components/__init__.py",
    f"src/{project_name1}/utils/__init__.py",
    f"src/{project_name1}/utils/common.py",
    f"src/{project_name1}/config/__init__.py",
    f"src/{project_name1}/config/configuration.py",
    f"src/{project_name1}/pipeline/__init__.py",
    f"src/{project_name1}/entity/__init__.py",
    f"src/{project_name1}/entity/config_entity.py",
    f"src/{project_name1}/constants/__init__.py",
    f"src/{project_name2}/__init__.py",
    f"src/{project_name2}/components/__init__.py",
    f"src/{project_name2}/utils/__init__.py",
    f"src/{project_name2}/utils/common.py",
    f"src/{project_name2}/config/__init__.py",
    f"src/{project_name2}/config/configuration.py",
    f"src/{project_name2}/pipeline/__init__.py",
    f"src/{project_name2}/entity/__init__.py",
    f"src/{project_name2}/entity/config_entity.py",
    f"src/{project_name2}/constants/__init__.py",
    f"src/__init__.py",
    "DATABASE1/1.py",
    "DATABASE2/2.py",
    "config/config1.yaml",
    "config/config2.yaml",
    "params1.yaml",
    "schema1.yaml",
    "params2.yaml",
    "schema2.yaml",
    "main1.py",
    "main2.py",
    "app.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]




for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)


    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    else:
        logging.info(f"{filename} is already exists")