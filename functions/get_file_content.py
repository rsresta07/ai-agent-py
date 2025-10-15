import os
from functions import config  # assumes config.py is in functions directory


def get_file_content(working_directory, file_path):
    try:
        base_path = os.path.abspath(working_directory)
        target_path = os.path.abspath(os.path.join(base_path, file_path))

        # Guard: must be inside working directory
        if not target_path.startswith(base_path):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        # Guard: must be a file
        if not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        # Read file
        with open(target_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Truncate if longer than configured limit
        limit = getattr(config, "MAX_FILE_READ_LENGTH", 10000)
        if len(content) > limit:
            return (
                content[:limit]
                + f'\n[...File "{file_path}" truncated at {limit} characters]'
            )

        return content

    except Exception as e:
        return f"Error: {str(e)}"
