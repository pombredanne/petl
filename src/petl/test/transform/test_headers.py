__author__ = 'Alistair Miles <alimanfoo@googlemail.com>'


from petl.testutils import ieq
from petl.util import fieldnames
from petl.transform.headers import setheader, extendheader, pushheader, skip,\
    rename, prefixheader, suffixheader


def test_setheader():

    table1 = (('foo', 'bar'),
              ('a', 1),
              ('b', 2))
    table2 = setheader(table1, ['foofoo', 'barbar'])
    expect2 = (('foofoo', 'barbar'),
               ('a', 1),
               ('b', 2))
    ieq(expect2, table2)
    ieq(expect2, table2)  # can iterate twice?


def test_setheader_empty():

    table1 = (('foo', 'bar'),)
    table2 = setheader(table1, ['foofoo', 'barbar'])
    expect2 = (('foofoo', 'barbar'),)
    ieq(expect2, table2)


def test_extendheader():

    table1 = (('foo',),
              ('a', 1, True),
              ('b', 2, False))
    table2 = extendheader(table1, ['bar', 'baz'])
    expect2 = (('foo', 'bar', 'baz'),
               ('a', 1, True),
               ('b', 2, False))
    ieq(expect2, table2)
    ieq(expect2, table2)  # can iterate twice?


def test_extendheader_empty():

    table1 = (('foo',),)
    table2 = extendheader(table1, ['bar', 'baz'])
    expect2 = (('foo', 'bar', 'baz'),)
    ieq(expect2, table2)


def test_pushheader():

    table1 = (('a', 1),
              ('b', 2))
    table2 = pushheader(table1, ['foo', 'bar'])
    expect2 = (('foo', 'bar'),
               ('a', 1),
               ('b', 2))
    ieq(expect2, table2)
    ieq(expect2, table2)  # can iterate twice?


def test_pushheader_empty():

    table1 = (('a', 1),)
    table2 = pushheader(table1, ['foo', 'bar'])
    expect2 = (('foo', 'bar'),
               ('a', 1))
    ieq(expect2, table2)

    table1 = tuple()
    table2 = pushheader(table1, ['foo', 'bar'])
    expect2 = (('foo', 'bar'),)
    ieq(expect2, table2)


def test_skip():

    table1 = (('#aaa', 'bbb', 'ccc'),
              ('#mmm',),
              ('foo', 'bar'),
              ('a', 1),
              ('b', 2))
    table2 = skip(table1, 2)
    expect2 = (('foo', 'bar'),
               ('a', 1),
               ('b', 2))
    ieq(expect2, table2)
    ieq(expect2, table2)  # can iterate twice?


def test_skip_empty():

    table1 = (('#aaa', 'bbb', 'ccc'),
              ('#mmm',),
              ('foo', 'bar'))
    table2 = skip(table1, 2)
    expect2 = (('foo', 'bar'),)
    ieq(expect2, table2)


def test_rename():

    table = (('foo', 'bar'),
             ('M', 12),
             ('F', 34),
             ('-', 56))

    result = rename(table, 'foo', 'foofoo')
    assert fieldnames(result) == ['foofoo', 'bar']

    result = rename(table, 0, 'foofoo')
    assert fieldnames(result) == ['foofoo', 'bar']

    result = rename(table, {'foo': 'foofoo', 'bar': 'barbar'})
    assert fieldnames(result) == ['foofoo', 'barbar']

    result = rename(table)
    result['foo'] = 'spong'
    assert fieldnames(result) == ['spong', 'bar']


def test_rename_empty():
    table = (('foo', 'bar'),)
    expect = (('foofoo', 'bar'),)
    actual = rename(table, 'foo', 'foofoo')
    ieq(expect, actual)


def test_prefixheader():

    table1 = (('foo', 'bar'),
              (1, 'A'),
              (2, 'B'))

    expect = (('pre_foo', 'pre_bar'),
              (1, 'A'),
              (2, 'B'))

    actual = prefixheader(table1, 'pre_')
    ieq(expect, actual)
    ieq(expect, actual)


def test_suffixheader():

    table1 = (('foo', 'bar'),
              (1, 'A'),
              (2, 'B'))

    expect = (('foo_suf', 'bar_suf'),
              (1, 'A'),
              (2, 'B'))

    actual = suffixheader(table1, '_suf')
    ieq(expect, actual)
    ieq(expect, actual)
