# import os
# import wget

# # data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# # Download the zipped dataset
# url = 'https://data.mendeley.com/public-files/datasets/yshdbyj6zy/files/6722d2a1-b669-427e-9c1e-f1360ad485b0/file_downloaded'
# csv_name = "data_raw.csv"
# wget.download(url, csv_name)

# Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)



# Xuan viet
# Đọc nội dung từ file first-data
with open('first-data.csv', 'r') as first_file:
    data = first_file.read()

# Tạo một file mới có tên là second-data và ghi nội dung vào đó
with open('data_raw.csv', 'w') as second_file:
    second_file.write(data)
    
