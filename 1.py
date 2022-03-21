text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#print(chr(ord(text)+2))

decrypt = ""

for i in text:
    decrypt += chr(ord(i)+2)

#print(decrypt)

x = decrypt.replace("{", "a")
y = x.replace("|", "b")
z = y.replace("0", ".")
o = z.replace(")", "'")
oo = o.replace('"', ' ')

print(oo)
