import pandas as pd
import sys
import xlwt

from sqlalchemy import create_engine, MetaData, Table, select, engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("postgres://postgres:admin@localhost:5432")

db = scoped_session(sessionmaker(bind=engine))

def main():

    #Load all the flights from flights2 database
    result = db.execute("SELECT * FROM flights2")

    #Load the data from postgres database into pandas dataframe
    df = pd.DataFrame(data = list(result), columns = result.keys())
    
    #print("Done")
    print(df)
    df.to_excel('flights2_table.xls', index=False)
    print('Data exported to excel file !')

if __name__ == "__main__":
    main()
