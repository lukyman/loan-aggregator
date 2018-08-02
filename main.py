import csv

import util
import loan_aggregator

class Main():
    """ Entry to loan aggregator program execution """
    
    def __init__(self):
        self.data_list = []
        self.read_loans_from_csv()
        self.aggregate_loan()

    def write_to_csv(self, data, filename, delimiter):
        csv.register_dialect('simple_dialect', 
                             quoting=csv.QUOTE_NONE,
                             escapechar=' ', 
                             delimiter=delimiter)

        with open(filename, 'w') as outputcsv:
            writer = csv.writer(outputcsv, dialect='simple_dialect')
            writer.writerow(data)
    
    def read_loans_from_csv(self):
        with open('Loans.csv') as loansfile:
            loandata = csv.reader(loansfile)
            self.data_list = util.csv_to_list_dict(loandata)
           
    def aggregate_loan(self):
         #Aggrgate by month
        grouped_by_Date =loan_aggregator.groupby_column(
            self.data_list,'Date', util.getMonthName)
        aggregate_month = loan_aggregator.aggregate_by_column(
            grouped_by_Date,['Month', 'Total Amount','Counts'])
        #Aggregate by product
        grouped_by_product = loan_aggregator.groupby_column(
            self.data_list,'Product', util.removeExtraDoubleQuotation)
        aggregate_product = loan_aggregator.aggregate_by_column(
            grouped_by_product,['Product', 'Total Amount','Counts'])
        #Aggregate by Network
        grouped_by_network = loan_aggregator.groupby_column(
            self.data_list,'Network', util.removeExtraDoubleQuotation)
        aggregate_network = loan_aggregator.aggregate_by_column(
            grouped_by_network,['Network', 'Total Amount','Counts'])
        output_data = (aggregate_network, aggregate_product, aggregate_month)
        #call the method to write to csv file
        self.write_to_csv(output_data,'Output.csv', ',')

if __name__=="__main__":
    Main()