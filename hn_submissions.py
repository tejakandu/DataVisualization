# import requests
# from operator import itemgetter
#
# url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
# r =requests.get(url)
# print('status code' , r.status_code)
# submission_ids = r.json()
# submission_dicts = []
# for submission_id in submission_ids [:30]:
#     url( 'https://hacker-news.firebaseio.com/v0/items/' + str(submission_id) + 'json')
#     submission_r = requests.get(url)
#     print(submission_r.status_code)
#     response_dict = submission_r.json()
#
#     submission_dict = {
#         'title' : response_dict['title']
#         'link' : 'https://
#     }