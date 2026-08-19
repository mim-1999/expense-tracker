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

def get_expense(id):
    return Expense.query.get_or_404(id)

def update_expense(expense, title, amount, category):
    expense.title = title
    expense.amount = amount
    expense.category = category

    db.session.commit()

def get_expenses_by_category(category):
    return Expense.query.filter_by(category=category).all()

def search_expenses(search):
    return Expense.query.filter(
        Expense.title.ilike(f"%{search}%")
    ).all()

def filter_expenses(search=None, category=None, sort=None):
    query = Expense.query

    if search:
        query = query.filter(Expense.title.ilike(f"%{search}%"))

    if category:
        query = query.filter_by(category=category)

    if sort == "amount_asc":
        query = query.order_by(Expense.amount.asc())

    elif sort == "amount_desc":
        query = query.order_by(Expense.amount.desc())

    return query.all()