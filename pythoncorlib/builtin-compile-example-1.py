NAME = "script.py"
BODY = """print 'owl-stretching time' """
code = compile(BODY,NAME,"exec")
print code
exec code

