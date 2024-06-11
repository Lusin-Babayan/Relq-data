import pandas as pd
import matplotlib.pyplot as plt

with open("retail_sales_dataset.csv", "r", encoding='utf8') as file:
    file_csv = pd.read_csv(file)
    df = pd.DataFrame(file_csv) 
    print(df.columns)
    duplicate_rows = df.duplicated()
    df['is_duplicated'] = df.duplicated()
    # print(df['is_duplicated'].unique)
    # df_unique = df.drop_duplicates()
    df['Total Amount'] = df['Total Amount'].astype(float)
    df["Age Category"] = pd.cut(df['Age'],
                      bins=[df['Age'].min()-1, 19, 39, 59, df['Age'].max()],
                      labels=['Teen', 'Adult', 'Middle Age Adult', 'Senior Adult'])
    
    print(df['Age Category'].unique)
    # df.to_excel("new_retail_data.xlsx")
    # 1.How does customer age and gender influence their purchasing behavior?
    
    # print(df.groupby(['Age Category'])['Total Amount'].sum())
    (df.groupby(['Age Category'])['Total Amount'].sum()).to_excel("age_spentamount_dependency.xlsx")
    (df.groupby(['Age Category'])['Total Amount'].sum()).plot.bar(width=0.7, color='green')
    plt.xlabel('Age Category')
    plt.ylabel('Total Amount')
    plt.title('Adults spend more')
    plt.grid(True)
    plt.show()
    (df.groupby(['Age Category'])['Transaction ID'].count()).plot.bar(width=0.7)
    (df.groupby(['Age Category'])['Transaction ID'].count()).to_excel("age_ordercount_dependency.xlsx")
    plt.xlabel('Age Category')
    plt.ylabel('Placed order count')
    plt.title('Middle Age Adults shop more often')
    plt.grid(True)
    plt.show()

    print(df.groupby(['Gender'])['Total Amount'].sum())

    (df.groupby(['Gender'])['Total Amount'].sum()).plot.bar(width=0.7)
    (df.groupby(['Gender'])['Total Amount'].sum()).to_excel("gender_spentamount_dependency.xlsx")
    plt.show()
    (df.groupby(['Gender'])['Transaction ID'].count()).plot.bar(width=0.7)
    (df.groupby(['Gender'])['Transaction ID'].count()).to_excel("gender_ordercount_dependency.xlsx")

    print(df.groupby(['Age Category','Gender'])['Total Amount'].sum())
    (df.groupby(['Age Category','Gender'])['Total Amount'].sum()).plot.bar(width=0.7)
    (df.groupby(['Age Category','Gender'])['Total Amount'].sum()).to_excel("age_gender_spentamount_dependency.xlsx")
    plt.show()
    print(df.groupby(['Age Category','Gender'])['Transaction ID'].count())
    (df.groupby(['Age Category','Gender'])['Transaction ID'].count()).plot.bar(width=0.7)
    (df.groupby(['Age Category','Gender'])['Transaction ID'].count()).to_excel("age_gender_ordercount_dependency.xlsx")
    plt.show()

    # 2.Which product categories hold the highest appeal among customers?


    (df.groupby(['Product Category'])['Total Amount'].sum()).plot.bar(width=0.7)
    (df.groupby(['Product Category'])['Total Amount'].sum()).to_excel('product_category_price_distribution.xlsx')
    plt.show()
    (df.groupby(['Product Category'])['Transaction ID'].count()).plot.bar(width=0.7)
    (df.groupby(['Product Category'])['Transaction ID'].count()).to_excel('product_category_sale_distribution.xlsx')
    plt.show()

    
    # 3.What are the relationships between age, spending, and product preferences?

    (df.groupby(['Product Category', 'Age Category'])['Total Amount'].sum()).to_excel('age_product_spentamount_dependency.xlsx')
    (df.groupby(['Age Category', 'Product Category'])['Total Amount'].sum()).plot.bar(width=0.7)
    plt.show()
    (df.groupby(['Product Category', 'Age Category'])['Transaction ID'].count()).to_excel('age__product_ordercount_dependency.xlsx')
    (df.groupby(['Age Category','Product Category'])['Transaction ID'].count()).plot.bar(width=0.7)
    plt.show()

    (df.groupby(['Product Category','Gender', 'Age Category'])['Total Amount'].sum()).to_excel('age_gender_product_spentamount_dependency.xlsx')
    (df.groupby(['Age Category','Gender','Product Category'])['Total Amount'].sum()).plot.bar(width=0.7)
    plt.show()
    (df.groupby(['Product Category','Gender', 'Age Category'])['Transaction ID'].count()).to_excel('age_gender_product_ordercount_dependency.xlsx')
    (df.groupby(['Age Category','Gender','Product Category'])['Transaction ID'].count()).plot.bar(width=0.7)
    plt.show()

    df['date_month'] = pd.to_datetime(df['Date'], format='mixed') - pd.to_timedelta(1, unit='m')
    month = df.groupby([pd.Grouper(key='date_month', freq='M')])['Transaction ID'].count()
    df.groupby([pd.Grouper(key='date_month', freq='M')])['Transaction ID'].count().to_excel('sales_count_monthly.xlsx')
    df.groupby([pd.Grouper(key='date_month', freq='M')])['Total Amount'].sum().to_excel('sales_sum_monthly.xlsx')
    df_month = pd.DataFrame({'Month': month.index, 'Count': month.values})
    df_month.plot(kind = 'bar', x = 'Month', y = 'Count')
    # print(df_month)
    plt.show()


    df['date_week'] = pd.to_datetime(df['Date'], format='mixed') - pd.to_timedelta(7, unit='d')
    week = df.groupby([pd.Grouper(key='date_week', freq='W')])['Transaction ID'].count()
    df_week = pd.DataFrame({'Week': week.index, 'Count': week.values})
    df_week.plot(kind = 'bar', x = 'Week', y = 'Count')
    # print(df_week)
    plt.show()


    # Load your dataset (replace 'your_data.csv' with your actual file)
    

    # Convert 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Extract month from 'Date'
    df['Month'] = df['Date'].dt.month
    df['Week'] = df['Date'].dt.weekday
    # df.to_excel("retail_donotoverrite.xlsx")

    # Group by month and calculate average total amount
    monthly_summary = df.groupby('Month')['Total Amount'].mean()

    # Plot the trends
    plt.figure(figsize=(8, 6))
    plt.plot(monthly_summary.index, monthly_summary.values, marker='o')
    plt.xlabel('Month')
    plt.ylabel('Average Total Amount')
    plt.title('Seasonal Trends: Average Total Amount per Month')
    plt.grid(True)
    plt.show()


    

    # Group by category and plot histograms
    plt.figure(figsize=(8, 6))
    for category, group in df.groupby('Product Category'):
        plt.hist(group['Price per Unit'], bins=10, alpha=0.7, label=category)

    plt.xlabel('Price per Unit')
    plt.ylabel('Frequency')
    plt.title('Price Distribution by Product Category')
    plt.legend()
    plt.show()



