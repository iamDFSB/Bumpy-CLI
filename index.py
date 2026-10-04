import os
import sys
from pathlib import Path


for f in Path.cwd().iterdir():
    list_path_uat = list(f.glob('uat/meu-cron/version'))
    if list_path_uat:
        print(list_path_uat)

    # if "pipeline" in str(f) and f.is_dir():
    # if "prd-marketplace" in os.listdir(f):


# "pipeline" in os.listdir()


# path = Path(__file__).parent / "pipeline/prd-marketplace/meu-cron/version"

# major = None
# minor = None
# patch = None

# with open(path, "r") as file:
#     content = file.read()
#     print("Old Version: ", content)
#     version = content.split(".")
#     major = int(version[0])
#     minor = int(version[1])
#     patch = int(version[2])

#     print(major)
#     print(minor)
#     print(patch)

# with open(path, "w") as file:
#     new_version = f"{major}.{minor}.{patch + 1}"
#     file.write(new_version)
