import pandas as pd
import requests
from bs4 import BeautifulSoup
import re


def get_questions(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    content = soup.body.find_all(string=re.compile('var FB'))

    match = re.findall('[,]["][\w\s]+["][,]', str(content))
    # It will match all the questions in the form
    question_strings = [x.strip('"') for x in match]

    match_ids = re.findall('(?<=\[\[)(\d+)', str(content))
    # It will find all the numbers in the content
    question_ids = ['entry.' + x for x in match_ids[1:]]
    # It will leave the first numbers (they are not the ids)
    return question_ids


def send_answers(url, list):

    ids = get_questions(url)

    response = dict(zip(ids, list))

    if 'viewform' in url:
        s = url.index('viewform')
        response_url = url.replace(
            url[s::], 'formResponse?&pageHistory=0,1,2,3,4')

    try:
        r = requests.post(response_url, response)
        if r.status_code == 200:
            return '[!] Attendence posted !'
        # In case an error happens, it will raise an exception
        else:
            raise Exception

    # After raising the exception it will retry to submit using url reconstruction with prefilled values
    except:
        try:
            ans_list = [x + '=' + y for x, y in zip(ids, list)]

            for i in range(0, len(ans_list)):
                response_url += ans_list[i]
                response_url += '&'

            response_url.strip("&")
            r = requests.get(response_url)
            status = r.status_code

            if status == 200:
                return '[!] Attendance sent !'
            else:
                raise Exception
        # If still an error happens, it will print out a message.
        except:
            return '[!] Attendance not sent !'


# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'responses.xlsx'
# Read the Excel file with 'sheet1' only
df = pd.read_excel(file_path, sheet_name='sheet1')


def remove_starting_space(strings):
    return [string.lstrip() for string in strings]


def get_row_to_list(i):
    first_row_values = df.iloc[i].tolist()
    if "Các quán cafe, shop thời trang, mỹ phẩm mang phong cách Hàn Quốc" not in first_row_values[5]:
        first_row_values[5] = first_row_values[5].split(",")
    else:
        first_row_values[5] = first_row_values[5].replace(
            ", Các quán cafe, shop thời trang, mỹ phẩm mang phong cách Hàn Quốc", '')
        first_row_values[5] = first_row_values[5].split(",")
        first_row_values[5].append(
            "Các quán cafe, shop thời trang, mỹ phẩm mang phong cách Hàn Quốc")
        first_row_values[5] = remove_starting_space(first_row_values[5])

    if "Bao bì, thiết kế sản phẩm đẹp và bắt mắt" not in first_row_values[10]:
        first_row_values[10] = first_row_values[10].split(",")
    else:
        first_row_values[10] = first_row_values[10].replace(
            ", Bao bì, thiết kế sản phẩm đẹp và bắt mắt", '').split(",")
        first_row_values[10].append("Bao bì, thiết kế sản phẩm đẹp và bắt mắt")
        first_row_values[10] = remove_starting_space(first_row_values[10])
    return first_row_values


# Display the DataFrame
# print(first_row_values)
url = "https://docs.google.com/forms/d/e/1FAIpQLScTwLezedgT7psCzC3mQbO7y4C9PUiAgg03ltuDR87pTZKE_A/viewform"
count = 0
for i in range(df.shape[0]):
    row_values = get_row_to_list(i)
    send_answers(url, row_values)
    print(count)
    count += 1
print("success")

# print(get_row_to_list(23))
