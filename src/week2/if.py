a = 10
b = 20
c = 30
# ==================================

if a == b:
    print('a equals to b')
else:
    print('They are not same')


if a == b:
    print('a equals to b')
elif b ==c:
    print('they are not same too')
else:
    print('non of them are matched')

# =========== Short hand IF ==============================
print('# =========== Short hand IF ==============================')

if a != b : print('a is NOT greater than b')
print('a EQUALS to b') if a == b else print('a is NOT ====Equals to b')

# ============= MULTI else condition ========================
print('# ============= MULTI else condition ========================')

a = 300
b = 400
c = 500

print('a EQUALS to b') if a == b else print('b EQUALS to c') if b == c else print('non of them are matched====')

# ================= SINGLE LINE ELSEIF ==========================
print('# ================= SINGLE LINE ELSEIF ==========================')
# NOTE: Assumption: in multi conditions 'elif' won't be accepted only else works.
print('a EQUALS to b') if a ==b else print('b EQUALS to c') if b == c else print('non of them are matched')


if a == b and b ==c :
    print('both same')

if a==b & b ==c:
    print('bth same')

if a==b or b ==c:
    print('one is matched')

if a==b | b==c:
    print('one matched')
# ====================== PASS & Continue behaves same ==================================
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

# Method 2:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

for a in myfamily.items():
    pass

for a in myfamily.items():
    continue


# ============ BREAK =================

for a in myfamily.items():
    print('break')
    break # breaks the iterations


