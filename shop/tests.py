from django.test import TestCase

# Create your tests here.


# ye question krna hai 28/2/2021 1:34 AM
# password increption

def decryptPassword(s):
    temp = ""
    v = s[-1::-1]

    for x, c in enumerate(s, 0):
        if ord("1") <= ord(c) <= ord("9"):
            for y, i in enumerate(v, 0):
                if i == "0":
                    v.replace("0",c,1)
                    v=v[1::]
                    v = s[-1::-1]
                    v[x] = c
                    s = v[-1::-1]

                    s = s[1::]

        if ord("A") <= ord(c) <= ord("Z") and ord("a") <= ord(s[x + 1]) <= ord("z") and ord(s[x + 2] == ord("*")):
            temp = s[x + 1]

            s[x + 1] = s[x]
            s[x] = temp
    return s


print(decryptPassword("43Ah*ck0rr0nk"))