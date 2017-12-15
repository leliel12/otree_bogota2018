#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
import hashlib
import time

cmd = "pandoc --filter pandoc-latex-fontsize --highlight-style tango -t beamer slides.md -o slides.pdf"

checksum = None

print("\n".join(os.listdir("imgs")))
print("*" * 10)

while True:

    with open("slides.md") as fp:
        code = fp.read().encode("utf8")
        newchecksum = hashlib.sha1(code).hexdigest()

    if newchecksum != checksum:
        print("building")
        os.system(cmd)
        checksum = newchecksum

    time.sleep(2)
