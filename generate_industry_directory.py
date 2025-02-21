import os

# List of categories
categories = [
    "Technology", "Healthcare", "Finance", "Insurance", "Manufacturing", 
    "Retail", "Energy", "Media", "Agriculture", "Construction"
]

# List of file types
file_types = ["Images", "Audio", "Videos", "FlatFiles", "SemiStructuredFiles"]

# Create the folder structure and text files
def create_folders_and_files():
    # Create the category folders and their subfolders
    for category in categories:
        category_path = os.path.join(os.getcwd(), category)  # Use the current directory
        os.makedirs(category_path, exist_ok=True)
        
        for file_type in file_types:
            file_type_path = os.path.join(category_path, file_type)
            os.makedirs(file_type_path, exist_ok=True)
            
            # Create a .txt file in each subfolder
            txt_file_path = os.path.join(file_type_path, f"{file_type}.txt")
            with open(txt_file_path, 'w') as f:
                f.write(f"This is the {file_type} folder in the {category} category.\n")

# Run the function to create the folders and text files
create_folders_and_files()

print("Folder structure and text files created successfully!")