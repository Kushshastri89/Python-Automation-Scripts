import os
import shutil
from pathlib import Path

# Define file categories
FILE_CATEGORIES = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xls", ".xlsx", ".ppt", ".pptx", ".odt"],
    "Pictures": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".heic"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv"],
    "Music": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Programs": [".exe", ".msi", ".apk", ".bat", ".sh", ".deb"],
    # "Code": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".json", ".xml", ".php", ".rb", ".go"],
    "Others": []
}


def get_category(file_ext):
    for category, extensions in FILE_CATEGORIES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"


def organize_directory(directory):
    directory = Path(directory)

    if not directory.exists():
        print(f"Directory {directory} does not exist.")
        return

    for item in directory.iterdir():
        if item.is_file() and not item.name.startswith('.'):
            category = get_category(item.suffix)
            category_folder = directory / category

            if not category_folder.exists():
                category_folder.mkdir()

            try:
                shutil.move(str(item), str(category_folder / item.name))
                print(f"Moved {item.name} to {category}/")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")


if __name__ == "__main__":
    # You can change this to any folder you want to organize
    folder_to_organize = str(Path.home() / "Downloads")  # or "Desktop" or any path
    print(f"Organizing folder: {folder_to_organize}")
    organize_directory(folder_to_organize)
