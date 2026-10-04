class EmptyFileException(Exception):
    def __init__(self, file_name: str):
        message = f'An error occured, the file {file_name} is empty'
        super().__init__(message)


class MissingSegmentsException(ValueError):
    def __init__(self, file_name: str):
        message = f'An error occured, the file {file_name} must have 3 segments (major.minor.patch)'
        super().__init__(message)


class NotFoundPipelinePathException(FileNotFoundError):
    def __init__(self):
        message = 'An error occured, pipeline path was not found'
        super().__init__(message)


class VersionUnderflowError(Exception):
    def __init__(self, file_name: str, version_part: str = "versão"):
        super().__init__(f"An error occured, It is not possible to decrease the {version_part} in {file_name}: the minimum value is 0.")