import re
from app.exceptions import (
    UnableGetExpenseException, UnableGetBodyMessageException
)
from app.models import Expense
from app import utils
from bs4 import BeautifulSoup
from datetime import datetime


def get_clean_html_body(raw_message: str) -> str:
    html_index = raw_message.find('<html')
    if html_index < 0:
        raise UnableGetBodyMessageException
    html_content = raw_message[html_index:]
    soup = BeautifulSoup(html_content, 'html.parser')
    body_tag = soup.find('body')
    if not body_tag:
        raise UnableGetBodyMessageException
    return str(body_tag)


def get_itau_cc_expense(message_body: str) -> Expense:
    """
    Function to return an expense filtering the info from an Itau
    credit card expense
    """
    soup = BeautifulSoup(message_body, 'html.parser')
    expense = Expense(0, '')
    tables = soup.find_all('table')
    expense_value = ''
    expense_description = None
    expense_date = None
    if not tables:
        raise UnableGetExpenseException
    try:
        if len(tables) <= 2:
            raise UnableGetExpenseException
        expense_description = tables[0].tr.td.get_text()
        expense_value = tables[1].find_all('tr')[0] \
                                 .find_all('td')[1] \
                                 .get_text()
        expense_date = tables[1].find_all('tr')[1] \
                                .find_all('td')[1] \
                                .get_text()
    except (AttributeError, IndexError):
        raise UnableGetExpenseException
    expense.description = utils.remove_spaces(expense_description)
    expense_value = re.sub(r"[$\,]*", "", utils.remove_spaces(expense_value))
    try:
        expense.expense_value = float(expense_value)
    except ValueError:
        raise UnableGetExpenseException
    expense_date = utils.remove_spaces(expense_date)
    try:
        expense.date_expense = datetime.strptime(
            expense_date, '%Y/%m/%d %H:%M:%S'
        )
    except ValueError:
        raise UnableGetExpenseException
    return expense
