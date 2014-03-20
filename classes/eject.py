"""
Eject class

This class ejects CDs


Released under the MIT license
Copyright (c) 2012, Jason Millward

@category   misc
@version    $Id: 1.5, 2013-10-20 20:40:30 CST $;
@author     Jason Millward <jason@jcode.me>
@license    http://opensource.org/licenses/MIT
"""

import logger
import sys
import os

class eject(object):

    def __init__(self, drive, debugLevel):
        self.log = logger.logger("Eject", debugLevel)
        self.eject(drive)

    def eject(self, drive):
        """
            Ejects the DVD drive
        """
        self.log.debug("Ejecting drive: " + drive)
        self.log.debug("Attempting OS detection")


        if sys.platform == 'win32':
            self.log.debug("OS detected as Windows")
            import ctypes
            ctypes.windll.winmm.mciSendStringW("set cdaudio door open", None, drive, None)

        elif sys.platform == 'darwin':
            self.log.debug("OS detected as OSX")
            p = os.popen("drutil eject " + drive)

            while 1:
                line = p.readline()
                if not line: break
                log.debug(line.strip())

        else:
            self.log.debug("OS detected as Unix")
            p = os.popen("eject -vrn " + drive)

            while 1:
                line = p.readline()
                if not line: break
                log.debug(line.strip())

