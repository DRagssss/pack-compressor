## What does this do?
In many cases, you may be working on a Minecraft texture pack by editing a base. Often, the base is the default Minecraft texture pack for that version. Minecraft uses the default pack as a fallback for all textures when you use your edit pack.

So your edited pack can often be much larger than it needs to be because it has a bunch of copies of textures from your base pack (which is used as a fallback anyway.) This script automatically removes the copied textures/files and only keeps the ones you edited.

## How to use?
1. Put your base texture pack in the packs folder with the name `base.zip`.
2. Put a copy of your edited texture pack in the packs folder with the name `edit.zip`.
3. Run `main.py` by running `python3 main.py` or any other way.

Your compressed pack will now be in `compressed-edit.zip`.
