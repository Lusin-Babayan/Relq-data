import pandas as pd
import matplotlib.pyplot as plt

with open("retail_sales_dataset.csv", "r", encoding='utf8') as file:
    # Load the Dataset:Use pandas to load the “House Dataset” CSV into a DataFrame named houses.
    file_csv = pd.read_csv(file)
    df = pd.DataFrame(file_csv) 
    print(df.columns)
    duplicate_rows = df.duplicated()
    df['is_duplicated'] = df.duplicated()
    print(df['is_duplicated'].unique)
    # df_unique = df.drop_duplicates()
    df['Total Amount'] = df['Total Amount'].astype(float)
    df["Age Category"] = pd.cut(df['Age'],
                      bins=[0, 19, 39, 59, 100],
                      labels=['Teen', 'Adult', 'Middle Age Adult', 'Senior Adult'])
    
    print(df['Age Category'].unique)
    df.to_csv('newret.csv')

    # df.plot(kind="hist", x='Age Category', y="Total Amount")
    print(df. groupby(['Age Category'])['Total Amount'].sum())

    (df.
 groupby(['Age Category'])['Total Amount']
 .sum()
).plot.bar(width=0.7)
    # plt.show()


    print(df.groupby(['Gender'])['Total Amount'].sum())

    (df.
 groupby(['Gender'])['Total Amount']
 .sum()
).plot.bar(width=0.7)
    # plt.show()


    df.groupby(['Product Category'])['Total Amount'].sum().to_csv('product_category_distribution.csv')

    (df.
 groupby(['Product Category'])['Total Amount']
 .sum()
).plot.bar(width=0.7)
    # plt.show()

    df['date_month'] = pd.to_datetime(df['Date'], format='mixed') - pd.to_timedelta(1, unit='m')
    month = df.groupby([pd.Grouper(key='date_month', freq='M')])['Transaction ID'].count()
    df.groupby([pd.Grouper(key='date_month', freq='M')])['Transaction ID'].count().to_excel('sales_count_monthly.xlsx')
    df.groupby([pd.Grouper(key='date_month', freq='M')])['Total Amount'].sum().to_excel('sales_sum_monthly.xlsx')
    df_month = pd.DataFrame({'Month': month.index, 'Count': month.values})
    df_month.plot(kind = 'bar', x = 'Month', y = 'Count')
    print(df_month)
    # plt.show()


    df['date_week'] = pd.to_datetime(df['Date'], format='mixed') - pd.to_timedelta(7, unit='d')
    week = df.groupby([pd.Grouper(key='date_week', freq='W')])['Transaction ID'].count()
    df_week = pd.DataFrame({'Week': week.index, 'Count': week.values})
    df_week.plot(kind = 'bar', x = 'Week', y = 'Count')
    print(df_week)
    # plt.show()


    print(df.groupby(['Age Category','Gender'])['Total Amount'].sum())

    (df.
 groupby(['Age Category','Gender'])['Total Amount']
 .sum()
).plot.bar(width=0.7)
    # plt.show()
    

    df.groupby(['Age Category','Gender'])['Total Amount'].sum().to_csv('age_gender_dependency.csv')
    df.groupby(['Product Category','Gender', 'Age Category'])['Total Amount'].sum().to_csv('age_gender_product_dependency.csv')

    (df.
 groupby(['Age Category','Product Category'])['Total Amount']
 .sum()
).plot.bar(width=0.7)
    # plt.show()


    # df.plot(kind="density", x='Quantity', y="Price per Unit")
    # plt.show()
    # df_unique.hist()
    # plt.show()
    # df_unique.boxplot(by ='Elevator', column =['Price(USD)'], grid = False) 
    # plt.show()