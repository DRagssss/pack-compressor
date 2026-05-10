from zipfile import ZipFile
import shutil
from pathlib import Path
from os import mkdir

mkdir("packs/compressed-edit")

with ZipFile("packs/base.zip", "r") as base_zip:
    base_files = [
        info.filename
        for info in base_zip.infolist()
        if not info.is_dir()
    ]

    with ZipFile("packs/edit.zip", "r") as edit_zip:
        for file_name in base_files:
            with base_zip.open(file_name) as base_content:
                with edit_zip.open(file_name) as edit_content:
                    if edit_content != base_content:
                        with open(f"packs/compressed-edit/{file_name}", "wb") as f:
                            f.write(edit_content.read())
                    else:
                        print(f"Detected copy file: `{file_name}`")

folder = Path("packs/compressed-edit")
files = []

for path in folder.rglob("*"):
    if path.is_file():
        files.append(path)

with ZipFile("packs/compressed-edit.zip", "w") as zip_ref:
    for file_path in files:
        zip_ref.write(file_path, arcname=file_path.relative_to(folder))

shutil.rmtree(folder)
