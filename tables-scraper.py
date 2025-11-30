import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import camelot 


def main():
    pdf_path = './data/water.pdf'
    tables = camelot.read_pdf(pdf_path)
    tables[0].to_csv('./data/water.csv')

if __name__ == '__main__':
    main()