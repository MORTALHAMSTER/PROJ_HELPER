import pickle as pi
import openpyxl as opx
import pandas as pd


def opening(way, sheet):
    book = pd.read_excel(way, sheet_name=sheet)
    return book


def make_lists(opening):
    pass
