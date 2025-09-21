import pandas as pd

df = pd.read_csv(r"C:\Users\input\input\currency-rates.csv")

while True:
    
    while True:
        currency_start = input("What would you like to convert").strip()
        result_for_start = df[df['Currency'] == currency_start]
        
        if not result_for_start.empty:
            print(result_for_start)
            break
        else:
            print("No Currency Found")

    section_result_for_start = result_for_start[["Value"]].values[0]

    print(section_result_for_start)

    while True:
        currency_end = input("Currency You Would like to Convert Too").strip()
        result_for_end = df[df['Currency'] == currency_end]

        if not result_for_end.empty:
            print(result_for_end)
            break
        else:
            print("No Currency Found")

    section_result_for_end = result_for_end[["Value"]].values[0]

    print(section_result_for_end)

    product = section_result_for_start * section_result_for_end
    print("The value is $", product)

