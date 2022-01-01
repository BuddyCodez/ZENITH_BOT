xmark = '❌'
tick = '👍'
voice_channel = '📞'
text_channel = '📱'
error = '🤕'
questionmark = '❓'
info = '❗'
youtube = '▶'
loading = '🔃'
number_emojis = {
    1: "\u0031\ufe0f\u20e3",
    2: "\u0032\ufe0f\u20e3",
    3: "\u0033\ufe0f\u20e3",
    4: "\u0034\ufe0f\u20e3",
    5: "\u0035\ufe0f\u20e3",
    6: "\u0036\ufe0f\u20e3",
    7: "\u0037\ufe0f\u20e3",
    8: "\u0038\ufe0f\u20e3",
    9: "\u0039\ufe0f\u20e3"
}
x = "\U0001f1fd"
o = "\U0001f1f4"
switch_on ='🔛'
switch_off ='📴'

def regional_indicator(c: str) -> str:
    """Returns a regional indicator emoji given a character."""
    return chr(0x1F1E6 - ord("A") + ord(c.upper()))
    

