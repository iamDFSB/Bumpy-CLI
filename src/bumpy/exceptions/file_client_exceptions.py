class EmptyFileException(Exception):
    def __init__(self):
        message = 'An error occured, the file is empty'
        super().__init__(message)


class MissingSegmentsException(ValueError):
    def __init__(self):
        message = 'An error occured, the file version must have 3 segments (major.minor.patch)'
        super().__init__(message)


class NotFoundPipelinePathException(FileNotFoundError):
    def __init__(self):
        message = 'An error occured, pipeline path was not found'
        super().__init__(message)


class VersionUnderflowError(Exception):
    """Lançada ao tentar diminuir uma versão que já está em zero."""
    def __init__(self, version_part: str = "versão"):
        super().__init__(f"Não é possível diminuir a {version_part}: o valor mínimo é 0.")