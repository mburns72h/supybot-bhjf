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
        irc.reply("have you heard the one about when tps, errata and bugzilla walked into a bar?")
    haha = wrap(haha, [])
    lol = wrap(haha, [])

    def tps(self, irc, msg, args):
        """ junk """
        irc.reply("TPS stands for Testing Personal Sanity")
    tps = wrap(tps, [])

    def ET(self, irc, msg, args):
        """ ET Phone Home """
        irc.reply("ET phones home, gets busy signal")
    et = wrap(ET, [])
    errata = wrap(ET, [])

    def silly_question(self, irc, msg, args):
        """ i have a silly question """
        irc.reply("there are no silly questions, only silly people...")
    silly = wrap(silly_question, [])
    silly_question = wrap(silly_question, [])

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

    def halibut(self, irc, msg, args, target=None):
        '''throw halibut at someone
        --- or have one thrown at you'''
        if target is not None:
            irc.reply(target + ":  ><}}}*>", prefixNick=False)
        else:
            irc.reply("><}}}*>")
    halibut = wrap(halibut, [optional('nick')])

Class = BHJF


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
