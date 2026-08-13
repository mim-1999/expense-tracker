from app.services.expense_service import (
    get_all_expenses,
    create_expense,
    delete_expense,
    update_expense,
    get_expense
)
from flask import Blueprint, render_template, request, redirect, url_for, flash

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
        try:
            amount = float(request.form["amount"])
        except ValueError:
            flash("Please enter a valid amount.")
            return redirect(url_for("main.add_expense"))

        if amount < 0:
            flash("Amount cannot be negative.")
            return redirect(url_for("main.add_expense"))
        
        
        create_expense(
            title=request.form["title"],
            amount=amount,
            category=request.form["category"]
        )

        flash("Expense added successfully!")

        return redirect(url_for("main.home"))

    return render_template("add_expense.html")


@main_bp.route("/delete-expense/<int:id>")
def remove_expense(id):
    expense = get_expense(id)

    delete_expense(expense)

    flash("Expense deleted successfully!")

    return redirect(url_for("main.home"))


@main_bp.route("/edit-expense/<int:id>", methods=["GET", "POST"])
def edit_expense(id):

    expense = get_expense(id)

    if request.method == "POST":
        
        if float(request.form["amount"]) < 0:
                flash("Amount cannot be negative.")
                return redirect(url_for("main.edit_expense", id=id))

        update_expense(
            expense,
            title=request.form["title"],
            amount=float(request.form["amount"]),
            category=request.form["category"]
        )

        flash("Expense updated successfully!")

        return redirect(url_for("main.home"))

    return render_template("edit_expense.html", expense=expense)