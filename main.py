def extract_Zip_Folders(root=None):
    """take a path to folder and extract all zip files even nested ones"""
    if root is None:
        root = "."

    zip_files = glob.glob(os.path.join(root, "*.zip"))
    sub_folders = [f.path for f in os.scandir(root) if f.is_dir()]
    if len(zip_files) == 0 and len(sub_folders) == 0:
        return
    else:
        for zip_file in zip_files:
            with zipfile.ZipFile(zip_file) as zip:
                file_name, _ = os.path.splitext(os.path.basename(zip_file))
                new_path = os.path.join(root, file_name)
                zip.extractall(new_path)
                extract_Zip_Folders(new_path)

        for sub_folder in sub_folders:
            extract_Zip_Folders(sub_folder)
