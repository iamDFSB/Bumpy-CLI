import os
from pathlib import Path
from .exceptions.file_client_exceptions import (
    EmptyFileException,
    MissingSegmentsException,
    NotFoundPipelinePathException,
    VersionUnderflowError,
)


class FileClient:
    def __init__(self) -> None:
        self.__absolute_path = Path.cwd()
        self.__current_dir = None
        self.__segment = {}

    def __validate_pipeline_path(self, pipeline_path: str) -> None:
        for f in self.__absolute_path.iterdir():
            list_path = list(f.glob(pipeline_path))
            if list_path:
                self.__current_dir = list_path[0]
                return None
        raise NotFoundPipelinePathException()
    
    def __get_current_version(self) -> None:
        with open(self.__current_dir, 'r') as file:
            content = file.read()
            if not content:
                raise EmptyFileException(str(self.__current_dir))

            version = content.split('.')
            if len(version) < 3:
                raise MissingSegmentsException(str(self.__current_dir))

            self.__segment["major"] = int(version[0])
            self.__segment["minor"] = int(version[1])
            self.__segment["patch"] = int(version[2])

    def __update_file_version(self) -> None:
        major = self.__segment["major"]
        minor = self.__segment["minor"]
        patch = self.__segment["patch"]

        with open(self.__current_dir, 'w') as file:
            new_version = f'{major}.{minor}.{patch}'
            file.write(new_version)

    def increase(self, segment: str, pipeline_path: str) -> None:
        self.__validate_pipeline_path(pipeline_path)
        self.__get_current_version()

        self.__segment[segment] += 1

        self.__update_file_version()

    def decrease(self, segment: str, pipeline_path: str) -> None:
        self.__validate_pipeline_path(pipeline_path)
        self.__get_current_version()

        if self.__segment[segment] == 0:
            raise VersionUnderflowError(pipeline_path, segment)

        self.__segment[segment] -= 1
        
        self.__update_file_version()

    def increase_all(self, segment: str, pipeline_path: str) -> None: 
        folder_paths = self.__absolute_path / pipeline_path

        for folder_name in os.listdir(folder_paths):
            version_path = folder_paths / folder_name / "version"
            self.__current_dir = version_path
            self.__get_current_version()
            self.__segment[segment] += 1
            self.__update_file_version()

    def decrease_all(self, segment: str, pipeline_path: str) -> None: 
        folder_paths = self.__absolute_path / pipeline_path

        for folder_name in os.listdir(folder_paths):
            version_path = folder_paths / folder_name / "version"
            self.__current_dir = version_path
            self.__get_current_version()

            if self.__segment[segment] == 0:
                raise VersionUnderflowError(folder_name, segment)
            
            self.__segment[segment] -= 1
            self.__update_file_version()
    

