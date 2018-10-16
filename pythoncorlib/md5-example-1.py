import md5
hash = md5.new()
hash.update("sbsbsbsb")
print repr(hash.digest())
