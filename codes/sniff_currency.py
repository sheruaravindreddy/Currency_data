import quandl
import pandas as pd
import csv
import copy
from datetime import datetime, timedelta

## obtaining currency data of last N days

i = 4001
while i<=8000:
    date = (datetime.now() - timedelta(i+1)).strftime('%Y-%m-%d')
    currency = pd.read_html('http://www.xe.com/currencytables/?from=INR&date='+date,attrs={'id':'historicalRateTbl'})
    ##currency = pd.read_html('http://www.x-rates.com/historical/?from=INR&amount=1&date=2017-02-05')

    ##This is a dataframe
    dataframe =(currency[0])
##    dataframe = dataframe.convert_objects(convert_numeric = True)
    
    dataframe.columns = ['country_symbol',
                              'country',
                              'rupee_to_foreign',
                              'foreign_to_rupee']


##    ##converting data frame to csv data frame
##    dataframe.to_csv('CSVdataframe'+str(i)+'.csv', header = False)
##    
##    df = pd.read_csv('CSVdataframe'+str(i)+'.csv', encoding='latin-1',
##                     names = [
##                              'country_symbol',
##                              'country',
##                              'rupee_to_foreign',
##                              'foreign_to_rupee',
##                              'YYYYMMDD'], index_col = 0)


####converting column to list
    col_country_symbol = ['USD', 'EUR', 'GBP', 'INR', 'AUD', 'CAD', 'SGD', 'CHF', 'MYR', 'JPY', 'CNY', 'NZD', 'THB', 'HUF', 'AED', 'HKD', 'MXN', 'ZAR', 'PHP', 'SEK', 'IDR', 'SAR', 'BRL', 'TRY', 'KES', 'KRW', 'EGP', 'IQD', 'NOK', 'KWD', 'RUB', 'DKK', 'PKR', 'ILS', 'PLN', 'QAR', 'XAU', 'OMR', 'COP', 'CLP', 'TWD', 'ARS', 'CZK', 'VND', 'MAD', 'JOD', 'BHD', 'XOF', 'LKR', 'UAH', 'NGN', 'TND', 'UGX', 'RON', 'BDT', 'PEN', 'GEL', 'XAF', 'FJD', 'VEF', 'BYN', 'HRK', 'UZS', 'BGN', 'DZD', 'IRR', 'DOP', 'ISK', 'XAG', 'CRC', 'SYP', 'LYD', 'JMD', 'MUR', 'GHS', 'AOA', 'UYU', 'AFN', 'LBP', 'XPF', 'TTD', 'TZS', 'ALL', 'XCD', 'GTQ', 'NPR', 'BOB', 'ZWD', 'BBD', 'CUC', 'LAK', 'BND', 'BWP', 'HNL', 'PYG', 'ETB', 'NAD', 'PGK', 'SDG', 'MOP', 'NIO', 'BMD', 'KZT', 'PAB', 'BAM', 'GYD', 'YER', 'MGA', 'KYD', 'MZN', 'RSD', 'SCR', 'AMD', 'SBD', 'AZN', 'SLL', 'TOP', 'BZD', 'MWK', 'GMD', 'BIF', 'SOS', 'HTG', 'GNF', 'MVR', 'MNT', 'CDF', 'STD', 'TJS', 'KPW', 'MMK', 'LSL', 'LRD', 'KGS', 'GIP', 'XPT', 'MDL', 'CUP', 'KHR', 'MKD', 'VUV', 'MRO', 'ANG', 'SZL', 'CVE', 'SRD', 'XPD', 'SVC', 'BSD', 'XDR', 'RWF', 'AWG', 'DJF', 'BTN', 'KMF', 'WST', 'SPL', 'ERN', 'FKP', 'SHP', 'JEP', 'TMT', 'TVD', 'IMP', 'GGP', 'ZMW']
##    print (len(dataframe['country_symbol']))
##    print (len(col_country_symbol))

#### checking whether country is present or not
    l= m = 0
    foreign_currency = []
    while m<(len(col_country_symbol)-1):
        if dataframe['country_symbol'][l] == col_country_symbol[m]:
            foreign_currency.append(dataframe['foreign_to_rupee'][l])
            l+=1
            m+=1
        else:
            foreign_currency.append(0)
            l=l
            m+=1
##        print ([l-1,dataframe['country_symbol'][l-1]],[m-1,col_country_symbol[m-1]])
    print (i)
    foreign_currency.append(0)
####adding elements of list to a CSV data frame
    with open('currency_output.csv', 'a', newline='') as csvfile:
        A = col_country_symbol
        A.append('DATE')
        B = foreign_currency
        B.append(date)
        d = csv.writer(csvfile, delimiter=',', quotechar='|', 
        quoting=csv.QUOTE_MINIMAL)  
        if i == 1:
            d.writerow(A)
            d.writerow(B)
        else:
            d.writerow(B)
    i+=1
