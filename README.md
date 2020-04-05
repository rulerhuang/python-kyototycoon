# python-kyototycoon

python-kyototycoon is a Python client library for [Kyoto Tycoon](http://fallabs.com/kyototycoon/).

## API

python-kyototycoon's application interface follows the preferred interface by Kyoto Tycoon's original author(s).

- http://fallabs.com/kyototycoon/kyototycoon.idl

There is currently no documentation for this software. For the time being, please see [kyototycoon.py](https://github.com/tmaesaka/python-kyototycoon/blob/master/kyototycoon/kyototycoon.py) for the available functionalities.

## Installation

```
python setup.py build
sudo python setup.py install
```

## Authors

Toru Maesaka <toru@torumk.com>

## Remark
- kyototyconn项目中源码不符合PEP8标准
- value采用pickle序列化，不利于客户端兼容(其他语言可能无法解析)
- 网络部分采用Py2的httplib标准库(Py3中该库重命名为http.client)
- tests/test_code.py为基本用法示例
- kct#opts=1#rcomp=lexdesc#bnum=1000000#msize=1g#dfunit=8,set性能在3000qps左右，get性能在3500qps左右