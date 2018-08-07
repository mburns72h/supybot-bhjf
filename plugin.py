###
# Copyright (c) 2016, Mike Burns
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import random
try:
    from supybot.i18n import PluginInternationalization
    _ = PluginInternationalization('BHJF')
except ImportError:
    # Placeholder that allows to run the plugin on a bot
    # without the i18n module
    _ = lambda x: x


class BHJF(callbacks.Plugin):
    """brown hat jellyfish"""
    pass

    def bhjf(self, irc, msg, args):
        """ print the bhjf"""
        irc.reply("it's me!!!!")
        irc.reply(ircutils.mircColor('    ,~"""~.         ', fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor(" ,-/       \-.      ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("' '`._____.'` `.    ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("-._         _,-'    ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   `--...--'        ", fg='brown',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   .-;':':'-.       ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("  {'.'.'.'.'.}      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("   )        '`.     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("  '-. ._ ,_.-='     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    `). ( `);(      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ('. .)(,'.)     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("     ) ( ,').(      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ( .').'(').     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("    .) (' ).('      ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("     '  ) (  ).     ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("      .'( .)'       ", fg='black',
            bg='light blue'), prefixNick=False)
        irc.reply(ircutils.mircColor("        .).'        ", fg='black',
            bg='light blue'), prefixNick=False)
    bhjf = wrap(bhjf, [])

    def cheers(self, irc, msg, args):
        """not quite a full celebration"""
        irc.reply("       __________ ", prefixNick=False)
        irc.reply("      |__  __  __|", prefixNick=False)
        irc.reply("  .---|  ::  ::  |", prefixNick=False)
        irc.reply(" |  __|__;:__;:__|", prefixNick=False)
        irc.reply(" | |  |  __  __  |", prefixNick=False)
        irc.reply(" | |  |::  ::  ::|", prefixNick=False)
        irc.reply(" | |  |::__;:__;:|", prefixNick=False)
        irc.reply(" | |  |__  __  __|", prefixNick=False)
        irc.reply("  . `.|  ::  ::  |", prefixNick=False)
        irc.reply("   `..|  ::  ::  |", prefixNick=False)
        irc.reply("       \ ::  :: /", prefixNick=False)
        irc.reply("        \;:  ;:/", prefixNick=False)
        irc.reply('         """"""', prefixNick=False)
    cheers = wrap(cheers, [])
    beer = wrap(cheers, [])

    def celebrate(sef, irc, msg, args):
        """time to celebrate"""

        irc.reply(ircutils.mircColor("     ,;``',", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ;      |", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("    ;;. ;;,'", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("     `\"-'7'.   IT'S TIME TO CELEBRATE!!   _  /", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         |' >.                         .'` |\  -", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         | /  >.                   _\ /   /  |  -", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         '/  / ,`.  __..----.       .'  .'  /  _", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         ;  / /_.-'          \     /_.-`_.-'  \ ", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("          ;' .'  '`           |  - `-.-'", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("          |_/                .'   /   \_\_", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("          _|  |_    .____.-'`         / __)`\ ", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         ( `  /\`'-...__.'  \        | '\(_.'|", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("          `-\   \ `-'-'-'|   `.      -.  \(_./", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("             \   \.-.-.  \     \___ /  >-'\_\ ", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("              \   \  \ \  `/\  |_  '` /", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("           _./\    \  ' | /    /_\ .-`", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("         .' _.\'.   '.__.'    /`\`'", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("  .-.---'\_/   `.`'-..____   ;   \ ", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor(" / / .--. |,     `'-._   /`'.|    |", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor(" `| /-' / / \         `.'    \   _/", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("  '-'  '-' \ `-._            _,-' |", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("            \    `'''----''''    /", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("             >                _.'", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("            / /`'-.._____..--'\ \ ", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("           < \                / /", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("            \ `.           .'  |___ mx", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("          ___\_ `.        /__.-'   ``--..", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("   ..--''`     `-.\      (___/`'--.._____)", fg='red',
            bg='white'), prefixNick=False)
        irc.reply(ircutils.mircColor("  (_____...--'`\___) ", fg='red',
            bg='white'), prefixNick=False)
    celebrate = wrap(celebrate, [])

    def haha(self, irc, msg, args):
        """ junk """
        _r = ['have you heard the one about when tps, errata and bugzilla walked into a bar?',
              'Challenge someone to arm-wrestle me. That would be fun.',
              'I\'d sooner eat a book than read it.',
              'Fortunately, no other part of me has anything to say.',
              'I am useful. I\'m better than any fireball, that I\'m sure of.']
        irc.reply(_r[random.randint(0, len(_r)-1)])
    haha = wrap(haha, [])
    lol = wrap(haha, [])

    def tps(self, irc, msg, args):
        """ junk """
        _r = ['It has a bird-like nature to its sadism, I\'ll give it that.',
              'TPS stands for Testing Personal Sanity',
              'I was not suffering, silently or otherwise, until now.',
              'It is as if a flesh creature exploded all over the room.  Fascinating.']
        irc.reply(_r[random.randint(0, len(_r)-1)])
    tps = wrap(tps, [])

    def jenkins(self, irc, msg, args):
        """ failing job """
        _r = ['http://file.rdu.redhat.com/~slinaber/2014-10-23-112547.jpg',
              'if a job fails and no one is around to hear it...']
        irc.reply(_r[random.randint(0, len(_r)-1)])
    jenkins = wrap(jenkins, [])

    def ET(self, irc, msg, args):
        """ ET Phone Home """
        _r = ['ET phones home, gets busy signal',
              'It is rather inferior to the Avil of the Void',
              'Does it not know its job?']
        irc.reply(_r[random.randint(0, len(_r)-1)])

    et = wrap(ET, [])
    errata = wrap(ET, [])

    def silly_question(self, irc, msg, args):
        """ i have a silly question """
        irc.reply("there are no silly questions, only silly people...")
    silly = wrap(silly_question, [])
    silly_question = wrap(silly_question, [])

    def sos(self, irc, msg, args):
        """HELP!!!"""
        irc.reply(".d8888b  .d88b. .d8888b  ", prefixNick=False)
        irc.reply("88K     d88\"\"88b88K      ", prefixNick=False)
        irc.reply("\"Y8888b.888  888\"Y8888b. ", prefixNick=False)
        irc.reply("     X88Y88..88P     X88 ", prefixNick=False)
        irc.reply(" 88888P' \"Y88P\"  88888P' ", prefixNick=False)
    sos = wrap(sos, [])


    def tux(self, irc, msg, args):
        """it's TUX!!!"""
        irc.reply("                 .88888888:. ", prefixNick=False)
        irc.reply("               88888888.88888. ", prefixNick=False)
        irc.reply("              .8888888888888888. ", prefixNick=False)
        irc.reply("              888888888888888888 ", prefixNick=False)
        irc.reply("              88' _`88'_  `88888 ", prefixNick=False)
        irc.reply("              88 88 88 88  88888 ", prefixNick=False)
        irc.reply("              88_88_::_88_:88888 ", prefixNick=False)
        irc.reply("              88:::,::,:::::8888 ", prefixNick=False)
        irc.reply("              88`:::::::::'`8888 ", prefixNick=False)
        irc.reply("             .88  `::::'    8:88. ", prefixNick=False)
        irc.reply("            8888            `8:888. ", prefixNick=False)
        irc.reply("          .8888'             `888888. ", prefixNick=False)
        irc.reply("         .8888:..  .::.  ...:'8888888:. ", prefixNick=False)
        irc.reply("        .8888.'     :'    `'::`88:88888 ", prefixNick=False)
        irc.reply("      .8888        '         `.888:8888. ", prefixNick=False)
        irc.reply("     888:8         .           888:88888  ",
        prefixNick=False)
        irc.reply("   .888:88        .:           888:88888:  ",
        prefixNick=False)
        irc.reply("   8888888.       ::           88:888888  ",
        prefixNick=False)
        irc.reply("   `.::.888.      ::          .88888888  ", prefixNick=False)
        irc.reply("  .::::::.888.    ::         :::`8888'.:.  ",
        prefixNick=False)
        irc.reply(" ::::::::::.888   '         .::::::::::::  ",
        prefixNick=False)
        irc.reply(" ::::::::::::.8    '      .:8::::::::::::.  ",
        prefixNick=False)
        irc.reply(" .::::::::::::::.        .:888:::::::::::::  ",
        prefixNick=False)
        irc.reply(" :::::::::::::::88:.__..:88888:::::::::::' ",
        prefixNick=False)
        irc.reply(" `'.:::::::::::88888888888.88:::::::::' ", prefixNick=False)
        irc.reply("       `':::_:' -- '' -'-' `':_::::'`  ", prefixNick=False)
    tux = wrap(tux, [])

    def mongo(self, irc, msg, args, target=None):
        '''mongodb is webscale '''
        irc.reply("MongoDB is Web Scale! -- https://youtu.be/b2F-DItXtZs " \
            "(warning, harsh language ahead)")
    mongo = wrap(mongo, [])

    def halibut(self, irc, msg, args, target=None):
        '''throw halibut at someone
        --- or have one thrown at you'''
        if target is not None:
            irc.reply(target + ":  ><}}}*>", prefixNick=False)
        else:
            irc.reply("><}}}*>")
    halibut = wrap(halibut, [optional('nick')])

    def insane(self, irc, msg, args, target=None):
        '''in need of a laugh'''
        irc.reply("If we couldn't laugh, we would all go insane --- Jimmy Buffett", prefixNick=False)
    insane = wrap(insane)
    laugh = wrap(insane)

    def badger(self, irc, msg, args):
        """Honey Badger!!!"""
        irc.reply("                ___,,___", prefixNick=False)
        irc.reply("           _,-='=- =-  -`\"--.__,,.._", prefixNick=False)
        irc.reply("        ,-;// /  - -       -   -= - \"=.", prefixNick=False)
        irc.reply("      ,'///    -     -   -   =  - ==-=\\`.", prefixNick=False)
        irc.reply("     |/// /  =    `. - =   == - =.=_,,._ `=/|", prefixNick=False)
        irc.reply("    ///    -   -    \\  - - = ,ndDMHHMM/\\b  \\\\ ", prefixNick=False)
        irc.reply("  ,' - / /        / /\\ =  - /MM(,,._`YQMML  `|", prefixNick=False)
        irc.reply(" <_,=^Kkm / / / / ///H|wnWWdMKKK#\"\"-;. `\"0\\  |", prefixNick=False)
        irc.reply("        `\"\"QkmmmmmnWMMM\\\"\"WHMKKMM\\   `--. \\> \ ", prefixNick=False)
        irc.reply(" hjm          `\"\"'  `->>>    ``WHMb,.    `-_<@)", prefixNick=False)
        irc.reply("                                `\"QMM`.", prefixNick=False)
        irc.reply("                                   `>>>", prefixNick=False)
        irc.reply("https://www.youtube.com/watch?v=pzagBTcYsYQ",
        prefixNick=False)
    badger = wrap(badger, [])
    honeybadger = wrap(badger, [])

    def shipit(self, irc, msg, args):
        """Ship It!!!"""
        irc.reply("                    |", prefixNick=False)
        irc.reply("                    |", prefixNick=False)
        irc.reply("           |        |", prefixNick=False)
        irc.reply("         |-|-|      |", prefixNick=False)
        irc.reply("           |        |", prefixNick=False)
        irc.reply("           | {O}    |", prefixNick=False)
        irc.reply("           '--|     |", prefixNick=False)
        irc.reply("             .|]_   |", prefixNick=False)
        irc.reply("       _.-=.' |     |", prefixNick=False)
        irc.reply("      |    |  |]_   |", prefixNick=False)
        irc.reply("      |_.-='  |   __|__", prefixNick=False)
        irc.reply("       _.-='  |\\   /|\\", prefixNick=False)
        irc.reply("      |    |  |-'-'-'-'-.", prefixNick=False)
        irc.reply("      |_.-='  '========='", prefixNick=False)
        irc.reply("           `   |     |", prefixNick=False)
        irc.reply("            `. |    / \\", prefixNick=False)
        irc.reply("              ||   /   \\____.--=''''==--.._", prefixNick=False)
        irc.reply("              ||_.'--=='    |__  __  __  _.'", prefixNick=False)
        irc.reply("              ||  |    |    |\\ ||  ||  || |                        ___", prefixNick=False)
        irc.reply(" ____         ||__|____|____| \\||__||__||_/    __________________/|   |", prefixNick=False)
        irc.reply("|    |______  |===.---. .---.========''''=-._ |     |     |     / |   |", prefixNick=False)
        irc.reply("|    ||     |\\| |||   | |   |      '===' ||  \\|_____|_____|____/__|___|", prefixNick=False)
        irc.reply("|-.._||_____|_\\___'---' '---'______....---===''======//=//////========|", prefixNick=False)
        irc.reply("|--------------\\------------------/-----------------//-//////---------/", prefixNick=False)
        irc.reply("|               \\                /                 // //////         /", prefixNick=False)
        irc.reply("|                \\______________/                 // //////         /", prefixNick=False)
        irc.reply("|                                        _____===//=//////=========/", prefixNick=False)
        irc.reply("|==============================================================LGB/", prefixNick=False)
        irc.reply("'----------------------------------------------------------------`", prefixNick=False)
    shipit = wrap(shipit, [])

    def shipitgood(self, irc, msg, args):
        """Ship it Good"""
        irc.reply('     .  o ..                  ', prefixNick=False)
        irc.reply('     o . o o.o                ', prefixNick=False)
        irc.reply('          ...oo               ', prefixNick=False)
        irc.reply('            __[]__            ', prefixNick=False)
        irc.reply('         __|_o_o_o\__         ', prefixNick=False)
        irc.reply('         \""""""""""/         ', prefixNick=False)
        irc.reply('          \. ..  . /          ', prefixNick=False)
        irc.reply('     ^^^^^^^^^^^^^^^^^^^^', prefixNick=False)
    shipitgood = wrap(shipitgood, [])

    def seal(self,irc,msg,args):
        """SEALS"""
        irc.reply('                                       ___ ', prefixNick=False)
        irc.reply('                                     //   \\\\  ', prefixNick=False)
        irc.reply('                                    ||=====||  ', prefixNick=False)
        irc.reply('                                     \\\\___//  ', prefixNick=False)
        irc.reply('                                      ./O  ', prefixNick=False)
        irc.reply('                                  ___/ //|\\\\  ', prefixNick=False)
        irc.reply('                                 / o    /}  ', prefixNick=False)
        irc.reply('                                (       /  ', prefixNick=False)
        irc.reply('                                \\      /  ', prefixNick=False)
        irc.reply('                                |     (  ', prefixNick=False)
        irc.reply('                                |      \\  ', prefixNick=False)
        irc.reply('                                )       \\  ', prefixNick=False)
        irc.reply('                               /         \\  ', prefixNick=False)
        irc.reply('                             /            )  ', prefixNick=False)
        irc.reply('                           /              |  ', prefixNick=False)
        irc.reply('                         //             / /  ', prefixNick=False)
        irc.reply('                       /       ___(    ,| \\  ', prefixNick=False)
        irc.reply('                     /       /    \\     |  \\  ', prefixNick=False)
        irc.reply('                    (      /  /   /\\     \\  \\  ', prefixNick=False)
        irc.reply('                    \\\\   /___ _-_//\'|     |  |  ', prefixNick=False)
        irc.reply('                     \\\\_______-/     \\     \\  \\  ', prefixNick=False)
        irc.reply('                                      \\-_-_-_-_-  ', prefixNick=False)
        irc.reply('  ', prefixNick=False)
        irc.reply('                        "Seal of Approval"  ', prefixNick=False)
    seal = wrap(seal, [])

Class = BHJF


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
