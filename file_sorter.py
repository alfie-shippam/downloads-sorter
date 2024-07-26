import os
import shutil

# Define the path to the downloads folder
downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')

print(f"Downloads path: {downloads_path}")

# Define file type categories
file_types = {
    'PDFs': ['.pdf'],
    'Data': ['.xlsx', '.csv', '.gsheet'],
    'Music': ['.mp3', '.flac', '.wav', '.aac'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Zips': ['.zip', '.rar', '.7z', '.tar', '.gz'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
    'Programs': ['.exe', '.msi', '.bat', '.sh'],
    'Others': []
}

# Create subfolders if they don't exist
for folder in file_types.keys():
    folder_path = os.path.join(downloads_path, folder)
    os.makedirs(folder_path, exist_ok=True)

# Scan the downloads directory and move files to appropriate folders
for item in os.listdir(downloads_path):
    item_path = os.path.join(downloads_path, item)
    
    if os.path.isfile(item_path):
        _, file_extension = os.path.splitext(item_path)
        file_extension = file_extension.lower()
        
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                target_folder = os.path.join(downloads_path, folder)
                shutil.move(item_path, os.path.join(target_folder, item))
                moved = True
                break
        
        # If file type is not categorized, move to 'Others'
        if not moved:
            others_folder_path = os.path.join(downloads_path, 'Others')
            shutil.move(item_path, os.path.join(others_folder_path, item))

print("Files sorted.")
