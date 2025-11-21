import pytest
from library import Library, UserNotFoundError, BookNotFoundError, OutOfStockError


@pytest.fixture
def lib():
    l = Library()
    l.add_user("alice")
    l.add_user("bob")
    l.add_book("python", 2)
    l.add_book("java", 1)
    return l


def test_borrow_success(lib):
    assert lib.borrow_book("alice", "python") is True
    assert lib.books["python"] == 1
    print("借书成功，库存减少正常。")


def test_borrow_user_not_found(lib):
    try:
        lib.borrow_book("charlie", "python")
    except UserNotFoundError:
        print("测试通过：用户不存在时正确抛出异常。")
    else:
        print("测试失败：用户不存在时未抛出异常。")
        assert False


def test_borrow_book_not_found(lib):
    try:
        lib.borrow_book("alice", "c++")
    except BookNotFoundError:
        print("测试通过：图书不存在时正确抛出异常。")
    else:
        print("测试失败：图书不存在时未抛出异常。")
        assert False


def test_borrow_out_of_stock(lib):
    lib.borrow_book("bob", "java")  # 借掉唯一一本
    try:
        lib.borrow_book("alice", "java")
    except OutOfStockError:
        print("测试通过：库存为0时正确抛出异常。")
    else:
        print("测试失败：库存为0时未抛出异常。")
        assert False


def test_borrow_stock_reduces(lib):
    lib.borrow_book("alice", "python")
    lib.borrow_book("bob", "python")
    assert lib.books["python"] == 0
    print("库存归零测试通过。")
