import pandas as pd

df1 = pd.read_csv('disease_drugs_dataset.csv')
df1 = df1.drop("SideEffects", axis=1)
df2 = pd.read_csv("disease_context.csv")
df1['Context'] = df2['Context']
df1 = df1.fillna('No Data yet')
df1["Disease"] = df1["Disease"].str.lower()

def get_disease_info(disease_name):
    disease_name = disease_name.lower()
    match = df1[df1["Disease"] == disease_name]
    if not match.empty:
        row = match.iloc[0]
        return {
            "Disease": row["Disease"].title(),
            "Context": row["Context"],
            "Drugs": row["Drugs"],
            "Supplements": row["Supplements"]
        }
    return None

