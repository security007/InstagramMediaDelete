#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from examples.evaluation.evaluation_log import EvaluationLog
from examples.user_followers import getTotalFollowers


def evaluate_method(function, parameters, function_name=None):
    evaluation_log = EvaluationLog()
    evaluation_log.start_log(function_name)
    response = function(*parameters)
    evaluation_log.end_log(function_name)

    print('response size:', len(response))
    print('number of unique users:', len(set([user['username'] for user in response])))
    print()


if __name__ == "__main__":
    api = InstagramAPI("username", "password")
    api.login()

    # For a user with over 22k followers, use: user_id = '1461295173'
    user_id = api.username_id

    evaluate_method(api.getTotalFollowers, [user_id], 'api.getTotalFollowers')
    evaluate_method(getTotalFollowers, [api, user_id], 'getTotalFollowers')
