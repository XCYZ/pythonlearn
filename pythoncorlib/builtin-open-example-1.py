def open(filename, mode="rb"):
    import __builtin__
    file = __builtin__.open(filename, mode)
    if file.read(5) not in ("GIF87", "GIF89"):
        raise IOError, "not aGIF file"
    file.seek(0)
    return file
