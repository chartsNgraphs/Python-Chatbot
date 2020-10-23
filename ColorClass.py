import numpy as np

class Midnight():
    navy = '#%02x%02x%02x' % (46, 61, 89)
    orange = '#%02x%02x%02x' % (242, 82, 68)
    red = '#%02x%02x%02x' % (217, 65, 65)
    blood = '#%02x%02x%02x' % (166, 51, 51)
    grey = '#%02x%02x%02x' % (242, 242, 242)
    ghostwhite = '#%02x%02x%02x' % (248, 248, 255)
    gunsmoke = '#%02x%02x%02x' % (117, 115, 116)
    woodsmoke = '#%02x%02x%02x' % (223, 227, 229)
    white = '#%02x%02x%02x' % (255, 255, 255)
    teal = '#%02x%02x%02x' % (54, 164, 176)
    hiacynth = '#%02x%02x%02x' % (151, 127, 204)
    seaweed = '#%02x%02x%02x' % (132, 181, 89)
    fadednavy = '#%02x%02x%02x' % (71, 137, 182)
    pumpkin = '#%02x%02x%02x' % (239, 135, 20)
    brightdenim = '#%02x%02x%02x' % (44, 147, 225)
    salmon = '#%02x%02x%02x' % (246, 108, 78)
    dark = '#%02x%02x%02x' % (56, 56, 56)

    def lighter(self, color, percent):
        '''
        color: python color format string
        percent: decimal-format value (ex: 0.5) for how much lighter to make the passed color value. 

        The higher the value passed for the "percent" argument, the lighter the returned color will be.
        '''
        value = color.lstrip('#')
        lv = len(value)
        lv2= tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        _color = np.array(lv2)
        white = np.array([255, 255, 255])
        vector = white-_color
        finaltuple =  _color + vector * percent
        finalvalue = '#%02x%02x%02x' % (int(finaltuple[0]), int(finaltuple[1]), int(finaltuple[2]))
        return finalvalue
    
    @staticmethod
    def staticLighter(color, percent):
        '''
        color: python color format string
        percent: decimal-format value (ex: 0.5) for how much lighter to make the passed color value. 

        The higher the value passed for the "percent" argument, the lighter the returned color will be.
        '''
        value = color.lstrip('#')
        lv = len(value)
        lv2= tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        _color = np.array(lv2)
        white = np.array([255, 255, 255])
        vector = white-_color
        finaltuple =  _color + vector * percent
        finalvalue = '#%02x%02x%02x' % (int(finaltuple[0]), int(finaltuple[1]), int(finaltuple[2]))
        return finalvalue
    
    @staticmethod
    def darkOrLight(color, cutoff=225):
        '''
        color: python color format string
        cutoff: the sum of the rgb values to consider the cutoff for "dark" and "light". Default is 225. 

        The higher the value passed for the "percent" argument, the lighter the returned color will be.
        '''
        value = color.lstrip('#')
        lv = len(value)
        lv2= tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        _color = np.array(lv2)
        _sum = sum(_color)
        if _sum <= cutoff:
            return 'dark'
        else:
            return 'light'



    

