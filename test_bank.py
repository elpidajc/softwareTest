import pytest
from bank import transfer
from unittest.mock import MagicMock


def test_transfer_normal():
    a = {"balance": 100}
    b = {"balance": 50}
    assert transfer(a, b, 30) is True
    assert a["balance"] == 70
    assert b["balance"] == 80


def test_transfer_negative():
    a, b = {"balance": 100}, {"balance": 50}
    with pytest.raises(ValueError):
        transfer(a, b, -10)


def test_transfer_insufficient_balance():
    a, b = {"balance": 20}, {"balance": 50}
    with pytest.raises(ValueError):
        transfer(a, b, 50)


def test_transfer_with_mock():
    # 使用MagicMock模拟账户对象
    accountA = MagicMock()
    accountB = MagicMock()
    accountA.__getitem__.side_effect = lambda k: 100 if k == "balance" else None
    accountB.__getitem__.side_effect = lambda k: 50 if k == "balance" else None
    accountA.__setitem__ = MagicMock()
    accountB.__setitem__ = MagicMock()

    # 正常转账
    assert transfer(accountA, accountB, 40) is True
    accountA.__setitem__.assert_any_call("balance", 60)
    accountB.__setitem__.assert_any_call("balance", 90)

    # 余额不足
    accountA.__getitem__.side_effect = lambda k: 30 if k == "balance" else None
    with pytest.raises(ValueError):
        transfer(accountA, accountB, 40)

    # 负数金额
    with pytest.raises(ValueError):
        transfer(accountA, accountB, -20)
