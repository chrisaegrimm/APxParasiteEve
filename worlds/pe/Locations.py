from BaseClasses import Location
import typing


class PELoctData(typing.NamedTuple):
    code: int
    region: str
    name: str
