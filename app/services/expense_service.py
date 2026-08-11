from app.extensions import db
from app.models.expense import Expense


def get_all_expenses():
    return Expense.query.all()

def create_expense(title, amount, category):
    expense = Expense(
        title=title,
        amount=amount,
        category=category
    )

    db.session.add(expense)
    db.session.commit()

    return expense

def delete_expense(expense):
    db.session.delete(expense)
    db.session.commit()

def update_expense(expense, title, amount, category):
    expense.title = title
    expense.amount = amount
    expense.category = category

    db.session.commit()