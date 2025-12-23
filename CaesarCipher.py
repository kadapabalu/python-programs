def encrypt(text,shift):
    result=""
    for ch in text:
        if ch.isalpha():
            result+=chr(ord(ch)+shift)
        else:
            result+=ch
    return result
msg=input("Message:")
shift=2
encrypted=encrypt(msg,shift)
print("Encrypted:",encrypted)
