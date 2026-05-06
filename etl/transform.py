def transform(df):

    # remove duplicates
    df = df.drop_duplicates()

    # split salary column
    salary_split = df["salary"].str.split("-", expand=True)
    df["salary_min"] = salary_split[0].astype(int)
    df["salary_max"] = salary_split[1].astype(int)

    # split location column
    location_split = df["location"].str.split(" ", expand=True)
    df["city"] = location_split[0]
    df["state"] = location_split[1]

    # drop original columns
    df = df.drop(columns=["salary", "location"])

    return df