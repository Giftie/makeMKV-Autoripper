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
from sys import platform
from os import popen

class eject(object):


    def eject(drive, debug):
        """
            Ejects the DVD drive
        """
        log = logger.logger("Eject", debug)

        log.debug("Ejecting drive: " + drive)
        log.debug("Attempting OS detection")

        try:
            if platform == 'win32':
                log.debug("OS detected as Windows")
                import ctypes
                ctypes.windll.winmm.mciSendStringW("set cdaudio door open", None, drive, None)

            elif platform == 'darwin':
                log.debug("OS detected as OSX")
                p = popen("drutil eject " + drive)

                while 1:
                    line = p.readline()
                    if not line: break
                    log.debug(line.strip())

            else:
                log.debug("OS detected as Unix")
                p = popen("eject -vr " + drive)

                while 1:
                    line = p.readline()
                    if not line: break
                    log.debug(line.strip())

        except:
            log.info("Could not detect OS or eject CD tray")


