from enum import Enum


class VersionPart(str, Enum):
    major = 'major'
    minor = 'minor'
    patch = 'patch'

    def get_index_position(self):
        return {'major': 0, 'minor': 1, 'patch': 2}[self.value]
