import re,string


def combined_pattern(patterns):
    p= re.compile("|".join(map(lambda x:"("+x+")")))

    def fixup(v, m=p.match, r=range(0, len(patterns))):
        try:
            regs = m(v).regs
        except AttributeError:
            return None  # no match, so m.regs will fail
        else:
            for i in r:
                if regs[i + 1] != (-1, -1):
                    return i
    return fixup