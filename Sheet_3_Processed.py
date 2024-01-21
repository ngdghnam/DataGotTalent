import pandas as pd 
import re 

df = pd.read_excel("DATA SET.xlsx", sheet_name='film')

# Fill rating
df.loc[2, 'rating'] = 'TV-PG'
df['country'] = df['country'].fillna("United States - and other countries (If any)")

# Thay thế giá trị NaN
df = df.fillna('Undefined')

# Hàm loại bỏ ký tự đặc biệt từ một chuỗi
def loai_bo_ky_tu_dac_biet(chuoi):
    return re.sub(r'[^a-zA-Z0-9 ]', '', str(chuoi))

df['description'] = df['description'].apply(loai_bo_ky_tu_dac_biet)
df['cast'] = df['cast'].apply(loai_bo_ky_tu_dac_biet)
print(df)

