from app.services.expense_service import (
    get_all_expenses,
    create_expense,
    delete_expense,
    update_expense
)
from flask import Blueprint, render_template, request, redirect, url_for
from app.models.expense import Expense
from app.extensions import db

main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def home():
    
    expenses = get_all_expenses()

    return render_template(
        "index.html",
        expenses=expenses
    )


@main_bp.route("/add-expense", methods=["GET", "POST"])
def add_expense():

    if request.method == "POST":

        create_expense(
    title=request.form["title"],
    amount=float(request.form["amount"]),
    category=request.form["category"]
)

        return redirect(url_for("main.home"))

    return render_template("add_expense.html")

@main_bp.route("/delete-expense/<int:id>")
def remove_expense(id):
    expense = Expense.query.get_or_404(id)

    delete_expense(expense)

    return redirect(url_for("main.home"))

@main_bp.route("/edit-expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    expense = Expense.query.get_or_404(id)

    if request.method == "POST":

        update_expense(
            expense,
            title=request.form["title"],
            amount=float(request.form["amount"]),
            category=request.form["category"]
        )

        return redirect(url_for("main.home"))

    return render_template("edit_expense.html", expense=expense)