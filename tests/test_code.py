# encoding=utf-8
from pprint import pprint

from kyototycoon import KyotoTycoon


# connect
db = KyotoTycoon()
db.open(host='127.0.0.1', port=1978, timeout=5)

# set
db.set('name', 'alen')  # no expire
db.set('vip', 1, 31 * 24 * 60 * 60)     # a month expire

# get
print('get from db')
keys = ['name', 'vip']
for key in keys:
    print('key={}, value={}'.format(key, db.get(key)))


# bulk set
key_dict = {
    'age': 29,
    'no': 1001
}
db.set_bulk(key_dict)   # no expire


# bulk get
print('\nbulk get from db')
keys = ['name', 'age', 'no', 'vip']
res = db.get_bulk(keys)     # dict
pprint(res)
