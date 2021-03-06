"""
Contains Flag class
"""

class Flag:
    def __init__(self, name, short = None, long = None, type = None, help = "", default = None):
        self._name = name
        self._short = short
        self._long = long
        self._type = type
        self._help = help
        self._default = default
    
    def parse(self, text):
        if self._type:
            return self._type(text)
        else:
            return True
    
    def __str__(self):
        if self._short and self._long:
            return f"-{self._short} --{self._long} {self._help}"
        elif self._short:
            return f"-{self._short} {self._help}"
        elif self._long:
            return f"--{self._long} {self._help}"
    
    def _splitOnLongLine(self, text, length, indent):
        out         = []
        buf         = []
        length     -= 2
        totalindent = 0
        totalchars  = 0

        for pos, char in enumerate(text):
            buf.append(char)
            if ( pos - totalchars > length - totalindent ) or ( char == "\n" ):
                out.append("".join(buf))
                totalchars += len(buf)
                buf = []
                totalindent = indent

        out.append("".join(buf))
        return out

    def pretty(self, indent = 8, longest_long = 2, screen_width = 10):
        longest_long = longest_long - 5
        if self._short and self._long:
            return f"\n{' '*(indent*2)}".join(self._splitOnLongLine(f"{' ' * indent}-{self._short} --{self._long}{' ' * (longest_long - len(self._long))} | {self._help}".replace("\n", f"\n{' '*indent}"), screen_width, indent*2))
        elif self._short:
            return f"\n{' '*(indent*2)}".join(self._splitOnLongLine(f"{' ' * indent}-{self._short}{' ' * (longest_long+3)} | {self._help}".replace("\n", f"\n{' '*indent}"), screen_width, indent*2))
        elif self._long:
            return f"\n{' '*(indent*2)}".join(self._splitOnLongLine(f"{' ' * indent}   --{self._long}{' ' * (longest_long - len(self._long))} | {self._help}".replace("\n", f"\n{' '*indent}"), screen_width, indent*2))