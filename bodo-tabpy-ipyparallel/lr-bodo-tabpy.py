
import numpy as np
import bodo
import pandas as pd
import ipyparallel as ipp
import snowflake.connector
from sqlalchemy.dialects import registry
import inspect
import os
import tabpy
from tabpy.tabpy_tools.client import Client


@bodo.jit
def lr_from_sql(conn, sql, response_col):
    df = pd.read_sql(sql, conn)

    X = df.drop(columns=[response_col]).to_numpy()
    Y = df[response_col].to_numpy()
    D = X.shape[1]
    w = np.ones(D) - 0.5
    for i in range(10):
        w -= np.dot(((1.0 / (1.0 + np.exp(-Y * np.dot(X, w))) - 1.0) * Y), X)
    return w


def lr_from_sql_wrapper(args):
    table, response_col = args
    sql = f"select * from {table} limit 100"
    return lr_from_sql(os.environ['SNOWFLAKE_URL'], sql, response_col).tolist()


def lr_snowflake(args=["lr_points","response"]):
    client = ipp.Client(profile="default")
    dview = client[:]

    ar = dview.apply(lr_from_sql_wrapper, args)
    res = ar.get()
    return res[0]


def main():
    client = ipp.Client(profile="default")
    dview = client[:]
    dview.execute("import bodo")
    dview.execute("import numpy as np")
    dview.execute("import pandas as pd")
    dview.execute("import os")
    dview.execute(inspect.getsource(lr_from_sql))

    tp_client = Client('http://localhost:8080/')
    tp_client.deploy('lr_snowflake',
                     lr_snowflake,
                     'Logistic regression from Snowflake table', override=True)


if __name__ == "__main__":
    main()
