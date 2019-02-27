import sys, pygame

class FakeStrip():
    pix_wh = 0
    def __init__(self, screen, row_num, width, pix_wh):
        self.screen = screen
        self.row_num = row_num
        self.internal_list = [0 for _ in range(width)]
        self.pix_wh = pix_wh

    def __getitem__(self, key):
        return self.internal_list[key]

    def __setitem__(self, key, value):
        self.internal_list[key] = value

    def __len__(self):
        return len(self.internal_list)

    def fill(self, v):
        self.internal_list = [v for _ in self.internal_list]

    def show(self):
        for i, v in enumerate(self.internal_list):
            pygame.draw.rect(self.screen, v,
                (i * self.pix_wh,
                    self.row_num * self.pix_wh,
                    self.pix_wh,
                    self.pix_wh))
        update_rect = (0, self.row_num * self.pix_wh, self.pix_wh * len(self.internal_list), self.pix_wh)
        pygame.display.update(update_rect)
