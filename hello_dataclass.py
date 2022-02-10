from dataclasses import dataclass


@dataclass
class Imedia:
    ''' class that contain data of media'''
    
    name: str
    location: str
    rate: float = 3

    def __str__(self) -> str:
        return f"{self.name} in {self.location} by rate: {self.rate}"


class WebMedia(Imedia):
    pass

class LocalMedia(Imedia):
    pass



media_obj = Imedia(name = "class", location="https://")
