from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pyame.image.load(os.path.join('maps', 'map1.png'))
        self.rect = self.image.get_rect(topleft = pos)
