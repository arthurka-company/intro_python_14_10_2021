"""
Касса для магазина.
CLI - start, report
"""

'''
pip install pandas
pip install openpyxl

'''

import argparse
import pickle
import os
import pandas as pd


OPERATIONS_STORAGE = 'operations_data.pkl'


class CashBox:

    def __init__(self):
        self.data = []
        if os.path.isfile(OPERATIONS_STORAGE):
            with open(OPERATIONS_STORAGE, 'rb') as f:
                self.data = pickle.load(f)
        print(self.data)

    def _save_data(self):
        pickle.dump(self.data, open(OPERATIONS_STORAGE, 'wb'))

    def _add_payment(self):
        while True:
            print('Add amount or "back"')
            print('Amount format: order_id, order_sum, payment"')
            payment_case = input()
            if payment_case == 'back':
                break
            else:
                try:
                    input_data = payment_case.split()
                    value = float(input_data[2])
                    order_sum = float(input_data[1])
                    order_id = int(input_data[0])
                    self.data.append({
                        'id': order_id,
                        'order_sum': order_sum,
                        'payment': value,
                   })
                    print(f'Change is: {value - order_sum}')
                    break
                except:
                    print('ERROR: you must enter int or float in format <order_id, order_sum, payment>!')

    def _get_total(self):
        return sum([i['order_sum'] for i in self.data])

    def run_session(self):
        while True:
            print('Menu:\n1 - PAYMENT (p);\n2 - TOTAL (t);\n3 - EXIT (e).')
            case = input()
            if case == 'p':
                self._add_payment()
                self._save_data()
            elif case == 't':
                print(self._get_total())
            elif case == 'e':
                self._save_data()
                break
            else:
                print('Choose correct command!')

    def save_report(self, report_path, report_file_type):
        df = pd.DataFrame(self.data)
        df = df.set_index('id')
        df.loc['Total'] = df.sum(numeric_only=True)
        if report_file_type == 'xls':
            df.to_excel(f'{report_path}.xlsx')
        else:
            df.to_csv(f'{report_path}.csv')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Store cashbox')
    parser.add_argument('mode', type=str, help='Mode of the cashbox work')
    parser.add_argument('--report_path', type=str, default='report', help='Path for report file')
    parser.add_argument('--report_file_type', type=str, default='csv', help='Type of report file')
    args = parser.parse_args()

    if args.mode == 'START':
        cashbox = CashBox()
        cashbox.run_session()
    elif args.mode == 'REPORT':
        cashbox = CashBox()
        cashbox.save_report(report_path=args.report_path, report_file_type=args.report_file_type)
    else:
        raise ValueError('Wrong value for mode argument! Choices: START, REPORT')
