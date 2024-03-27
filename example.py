import pandas as pd
import camelot
import re

def extract_table_from_pdf(pdf_path, page_number, table_area):
    """
    使用camelot提取PDF中的表格。
    :param pdf_path: PDF文件的路径。
    :param page_number: 包含表格的页码。
    :param table_area: 表格在页面上的位置，格式为"x1,y1,x2,y2"。
    :return: 提取的表格作为DataFrame。
    """
    tables = camelot.read_pdf(pdf_path, pages=str(page_number), flavor='stream', table_areas=[table_area])
    if tables:
        return tables[0].df
    else:
        return pd.DataFrame()

def auto_add_columns_and_fill_data(df, new_columns_info, text_to_search, pdf_path):
    """
    自动添加新列并根据PDF中的文本填充数据。
    :param df: 原始DataFrame。
    :param new_columns_info: 要添加的新列信息，格式为[(列名, 默认值)]。
    :param text_to_search: 在PDF文本中搜索的正则表达式。
    :param pdf_path: PDF文件的路径。
    :return: 更新后的DataFrame。
    """
    # 从PDF中提取文本
    pdf_text = extract_text(pdf_path)
    # 搜索指定的文本以提取需要的信息
    search_result = re.search(text_to_search, pdf_text)
    if search_result:
        # 如果找到匹配项，使用提取的值
        extracted_value = search_result.group(1)
    else:
        # 如果没有找到，设定一个默认值
        extracted_value = "Unknown"
    
    # 添加新列并填充数据
    for column_name, default_value in new_columns_info:
        df[column_name] = extracted_value if column_name in pdf_text else default_value
    
    return df

# 示例用法
pdf_path = "path_to_your_pdf.pdf"
page_number = 1
table_area = "x1,y1,x2,y2"  # 需要用户根据实际PDF调整
new_columns_info = [("dv_FBDB15K/FBYG15K", 4096), ("dv_Others", 2048)]
text_to_search = r"vision feature dimension 𝑑𝑣 is (\d+)"

df = extract_table_from_pdf(pdf_path, page_number, table_area)
df_updated = auto_add_columns_and_fill_data(df, new_columns_info, text_to_search, pdf_path)

# 打印或保存df_updated作为验证
print(df_updated.head())
