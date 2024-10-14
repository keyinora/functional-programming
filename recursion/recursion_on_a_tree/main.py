def list_files(current_filetree, current_path=""):
    file_paths = []
    for current in current_filetree:
        if current_filetree[current] is None:
            file_paths.append(f"{current_path}/{current}")
        else:
            # Create a new path for each recursive call
            next_path = f"{current_path}/{current}"
            file_paths.extend(list_files(current_filetree[current], next_path))
    return file_paths

