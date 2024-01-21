import pandas as pd
import unicodedata

customer_df = pd.read_excel("DATA SET.xlsx", sheet_name="customer")

# Address
def normalize_vietnamese(text):
    if isinstance(text, str):
        normalized_text = unicodedata.normalize('NFC', text)
        return normalized_text
    else:
        return text

def replace_abbreviations(text):
    replacements = {'Đn': 'Đà Nẵng', 'Q ': 'Quận'}
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text

def remove_unnecessary_spaces(text):
    if isinstance(text, str):
        words = text.split()
        cleaned_text = ' '.join(words)
        return cleaned_text
    else:
        return str(text)

def normalize(text):
    cleaned_text = text.replace(',', '')
    cleaned_text = cleaned_text.title()
    return cleaned_text

customer_df['address'] = customer_df['address'].apply(normalize_vietnamese)
customer_df['address'] = customer_df['address'].apply(remove_unnecessary_spaces)
customer_df['address'] = customer_df['address'].apply(normalize)
customer_df['address'] = customer_df['address'].apply(replace_abbreviations)


# Translate to Vietnamese 
job_dict = {
    'teenager':'học sinh',
    'student':'sinh viên',
    'white collar':'nhân viên văn phòng',
    'blue collar':'công nhân',
    'specialist':'chuyên viên'
}

industry_dict = {
    'Unknown':'chưa xác định',
    'finance':'tài chính',
    'health service':'dịch vụ sức khỏe',
    'computer':'công nghệ',
    'engineering':'kỹ sư',
    'social service':'dịch vụ cộng đồng',
    'economics':'kinh tế',
    'education':'giáo dục',
    'goverment agent':'nhân viên chính phủ',
    'construction':'xây dựng'
}

# changing the jobs column data type to string
customer_df.job = customer_df.job.astype('str')
# mapping the values 0-3 to the actual written jobs
customer_df.job = customer_df.job.map(job_dict)

# changing the industry column data type to string
customer_df.industry = customer_df.industry.astype('str')
# mapping the values to the actual written industrys
customer_df.industry = customer_df.industry.map(industry_dict)

# Chuyển đổi cột 'DOB' từ số seri sang ngày tháng năm
customer_df['DOB'] = pd.to_datetime(customer_df['DOB'], origin='1899-12-30', unit='D', errors='coerce')

print(customer_df)
