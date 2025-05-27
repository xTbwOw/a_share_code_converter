from a_share_code_converter import *
import pandas as pd
import polars as pl

# Pandas Series
ser = pd.Series(["000001", 600519.0,'300519.SZ']*10)
CodeConverter.to_suffix(ser)
a=(CodeConverter.to_name(ser, with_code=True, code_format='suffix'))
# DataFrame: columns ['code_code','code_short']
CodeConverter.to_str(ser)
# Polars DataFrame
df = pl.DataFrame({"code": ["000001", "600519"]})
b=(CodeConverter.to_name(df, with_code=True, code_format='str'))
# Polars DataFrame: columns ['code_code','code_short']

