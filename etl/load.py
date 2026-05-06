from sqlalchemy import create_engine

def load(df):

    username = "root"
    password = "password"
    host = "localhost"
    database = "job_pipeline"

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@{host}/{database}"
    )

    # load companies
    companies = df[["company"]].drop_duplicates()
    companies.columns = ["company_name"]

    companies.to_sql(
        "companies",
        engine,
        if_exists="append",
        index=False
    )

    # load locations
    locations = df[["city", "state"]].drop_duplicates()

    locations.to_sql(
        "locations",
        engine,
        if_exists="append",
        index=False
    )

    # load jobs table
    df.to_sql(
        "jobs",
        engine,
        if_exists="append",
        index=False
    )

    print("Data loaded successfully")