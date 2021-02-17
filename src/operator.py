# NOTE: THIS REQUIRES FURTHER INVESTIGATION... NOT COMPLETELY UNDERSTOOD.
# ============>>>> Operator &= <<<=========
# This returns common/matching elements from both objects.
a = {1,2,3,4,'a','b'}
b = {2,3,'a','k'}
a &= b
#print(a)

a = 6
b = 5
a &= b
#print(a)
# ===============Operator |= =========================

# ===============Operator x ^= 3 =========================

# ===============Operator x <<= 3 =========================

# ===============Operator x >>= 3 =========================

# ===============Operator is =========================
a = 10
b = 10

if a == b:
    #print('same value')
    None

if a is b:
    #print('value matching')
    None

a = 'srujan'
b = 'Srujan'

if a is b:
    print('matching')
else:
    print('Not matchied')


