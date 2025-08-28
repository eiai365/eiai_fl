import os
import re
import json

from eiai_fl import run_curl

github_token = os.environ["GHCR_GITHUB_TOKEN"]


def search_issue_comment(*, issue_number, identification_string, github_api_url_prefix, log):
    url = github_api_url_prefix + '/' + str(issue_number) + '/comments'
    issue_comments_flag, issue_comments = run_curl.RunCurl().github(operation='GET', url=url, github_token=github_token, body='', log=log)

    issue_comments_dict = json.loads(issue_comments)
    for issue_comment in issue_comments_dict:
        if re.search(identification_string, issue_comment['body']):
            comment_id = issue_comment['id']
            print(comment_id)
            print(issue_comment)
            return False, comment_id, issue_comment['body']
        else:
            pass
    return True, None, None


def update_issue_comment(*, comment_id, github_api_url_prefix, body, log):
    url = github_api_url_prefix + 'comments/' + str(comment_id)
    flag, rtn_txt = run_curl.RunCurl().github(operation='PATCH', url=url, github_token=github_token, body=body, log=log)
    return flag, rtn_txt
