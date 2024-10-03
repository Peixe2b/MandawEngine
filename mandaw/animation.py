import os

from typing import List, Any
from mandaw.gameobject import GameObject


__al__ = [
    "Animation"
]

class Animation(GameObject):
    def __init__(self, window: Any, anim_folder: str, anim_time: int):
        super().__init__(window)
        self.frames: List[Any] = []
        self.anim_time: int = anim_time
        self.folder: str = anim_folder
        
        for f in os.listdir(anim_folder):
            if os.path.splitext(f)[1] == ".png":
                self.frames.append(f)

        self.frames = sorted(self.frames)
        self.count: int = len(self.frames)

    def draw(self):
        pass
    
    def __update_frames(self):
        pass





