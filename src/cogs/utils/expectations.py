from discord.ext import commands
from. import emote

class error(commands.CheckFailure):
    pass

class InvalidColor(error):
    def __init__(self, argument):
        super().__init__(
            f"{emote.error} | `{argument}` doesn't seem to be a valid color, \nPick a correct colour from [here](https://duckduckgo.com/?t=ffab&q=colour+picker&atb=v280-1&ia=answer)"
        )

class PastTime(error):
    def __init__(self):
        super().__init__(
            f"{emote.error} |The time you entered seems to be in past.\nKindly try again, use times like: `tomorrow` , `friday 9pm`"
        )


TimeInPast = PastTime


class InvalidTime(error):
    def __init__(self):
        super().__init__(f"{emote.error} |The time you entered seems to be invalid.\nKindly try again.")

class NotSetup(error):
    def __init__(self):
        super().__init__(
            f"{emote.error} | This command requires you to have Zenith Setup In This Server.\nKindly setup the bot and try again."
        )


class ScrimsManagerNotSetup(error):
    def __init__(self):
        super().__init__(
            f"{emote.error} | This command requires you to have Scrim Manager Setup In This Server.\nKindly setup the Scrim manager and try again."
        )