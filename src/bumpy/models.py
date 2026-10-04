from enum import Enum


class VersionPart(str, Enum):
    major = 'major'
    minor = 'minor'
    patch = 'patch'
