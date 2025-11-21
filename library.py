class UserNotFoundError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class OutOfStockError(Exception):
    pass


class Library:
    def __init__(self):
        self.users = set()
        self.books = {}  # book_name: stock

    def add_user(self, user):
        self.users.add(user)

    def add_book(self, book, stock):
        self.books[book] = stock

    def borrow_book(self, user, book):
        if user not in self.users:
            raise UserNotFoundError("用户不存在")
        if book not in self.books:
            raise BookNotFoundError("图书不存在")
        if self.books[book] <= 0:
            raise OutOfStockError("库存为0")
        self.books[book] -= 1
        return True
