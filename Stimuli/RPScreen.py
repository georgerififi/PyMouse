from Stimulus import *
import os
from time import sleep

class RPScreen(Stimulus):
    """ This class handles the presentation of Movies with an optimized library for Raspberry pi"""

    def get_condition_tables(self):
        return ['Reward']

    def setup(self):
        # setup parameters
        self.size = (800, 480)     # window size
        self.color = [127, 127, 127]  # default background color
        self.set_intensity(self.params['intensity'])

        # setup pygame
        if not pygame.get_init():
            pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.unshow()
        pygame.mouse.set_visible(0)
        pygame.display.toggle_fullscreen()


    def prepare(self):
        self._get_new_cond()

    def init(self):
        self.isrunning = True
        self.timer.start()
        self.logger.log_stim()

    def present(self):
        pass

    def stop(self, color=False):
        self.logger.log_stim()
        self.unshow(color)
        self.isrunning = False

    def set_background(self, color=False):
        """update background color"""
        if not color:
            color = self.color
        self.screen.fill(color)
        self.flip()

    def flip(self):
        """ Main flip method"""
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        self.flip_count += 1

    def set_intensity(self, intensity=None):
        if intensity is None:
            intensity = self.params['intensity']
        cmd = 'echo %d > /sys/class/backlight/rpi_backlight/brightness' % intensity
        os.system(cmd)

    def close(self):
        """Close stuff"""
        pygame.mouse.set_visible(1)
        pygame.display.quit()
        pygame.quit()

