import os


def get_files_info(working_directory, directory="."):
    try:
        base_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(base_path, directory))

        if not target_path.startswith(base_path):
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        if not os.path.isdir(target_path):
            return f'Error: "{directory}" is not a directory'

        entries = os.listdir(target_path)
        lines = []

        for entry in entries:
            entry_path = os.path.join(target_path, entry)
            size = (
                os.path.getsize(entry_path)
                if os.path.isfile(entry_path)
                else os.path.getsize(entry_path)
            )
            is_dir = os.path.isdir(entry_path)
            lines.append(f"- {entry}: file_size{size} bytes, is_dir={is_dir}")

        return "\n".join(lines)

    except Exception as e:
        return f"Error: {str(e)}"
