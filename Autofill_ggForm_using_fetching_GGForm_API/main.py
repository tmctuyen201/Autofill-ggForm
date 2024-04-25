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
    return question_ids[:-1]

# Below are only for when you want to know the form fills with their corresponding entry ids
#    questions = dict(zip(question_strings, question_ids))
#    return questions


# arrange this as per your form requirements
def send_answers(url, name, board, question):

    ids = get_questions(url)

    answers = [name, board, question]
    response = dict(zip(ids, answers))
    print(response)

    if 'viewform' in url:
        s = url.index('viewform')
        response_url = url.replace(
            url[s::], 'formResponse?pageHistory=0,1')

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
            ans_list = [x + '=' + y for x, y in zip(ids, answers)]

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


url = 'https://docs.google.com/forms/d/e/1FAIpQLSc7GGMa0FbQVmfhtVnEoMJtXmeXGns9VXS5KrkU7tvq8c6qqA/viewform'

name = 'Your first name here 2'
board = ['Marcom Board', 'HR & Culture Board']
question = 'Chắc chắn có (100%)'

print(get_questions(url))
print(send_answers(url, name, board, question))
