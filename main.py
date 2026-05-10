from zipfile import ZipFile
import shutil
from pathlib import Path
from os import mkdir

mkdir("packs/compressed-edit")
folder = Path("packs/compressed-edit")
try:
    with ZipFile("packs/base.zip", "r") as base_zip:
        base_files = [
            info.filename for info in base_zip.infolist() if not info.is_dir()
        ]

        with ZipFile("packs/edit.zip", "r") as edit_zip:
            edit_files = [
                info.filename for info in edit_zip.infolist() if not info.is_dir()
            ]

            common_files = set(base_files) & set(edit_files)
            edit_only_files = set(edit_files) - set(base_files)

            for file_name in common_files:
                if any(blocked in file_name for blocked in ["pack.mcmeta"]):
                    continue
                with base_zip.open(file_name) as base_content:
                    with edit_zip.open(file_name) as edit_content:
                        if edit_content.read() != base_content.read():
                            Path(f"packs/compressed-edit/{file_name}").parent.mkdir(
                                parents=True, exist_ok=True
                            )
                            with open(f"packs/compressed-edit/{file_name}", "wb") as f:
                                f.write(edit_zip.read(file_name))
                        else:
                            print(f"Detected copy file: `{file_name}`")

            for file_name in edit_only_files:
                Path(f"packs/compressed-edit/{file_name}").parent.mkdir(
                    parents=True, exist_ok=True
                )
                with open(f"packs/compressed-edit/{file_name}", "wb") as f:
                    f.write(edit_zip.read(file_name))

    files = []

    for path in folder.rglob("*"):
        if path.is_file():
            files.append(path)

    with ZipFile("packs/compressed-edit.zip", "w") as zip_ref:
        for file_path in files:
            zip_ref.write(file_path, arcname=file_path.relative_to(folder))
except Exception as e:
    print(e)  # don't crash so it...

# ...always removes compressed-edit folder
shutil.rmtree(folder)
