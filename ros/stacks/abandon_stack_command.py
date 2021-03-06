# coding=utf-8
#
# Copyright (c) 2017 Aliyun.com All right reserved. This software is the
# confidential and proprietary information of Aliyun.com ("Confidential
# Information"). You shall not disclose such Confidential Information and shall
# use it only in accordance with the terms of the license agreement you entered
# into with Aliyun.com .
#
# created by quming on 07/18/2017

from aliyunsdkros.request.v20150901 import AbandonStackRequest

import ros.apps.config as connect
import ros.apps.utils as utils
import json
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def setup(subparsers):
    parser = subparsers.add_parser('abandon-stack', help='Abandon the specified stack')
    parser.add_argument('--region-id', help='The region that is associated with the stack', required=True)
    parser.add_argument('--stack-name', help='The name that is associated with the stack', required=True)
    parser.add_argument('--stack-id', help='The id that is associated with the stack', required=True)

    parser.set_defaults(func=abandon_stack)


def abandon_stack(args):
    req = prepare_request(args)
    status, headers, body = utils.send_req(req)
    utils.deal_resp(status, headers, body, print_response)


def prepare_request(args):
    req = AbandonStackRequest.AbandonStackRequest()

    req.set_headers({'x-acs-region-id': args.region_id})
    req.set_StackName(args.stack_name)
    req.set_StackId(args.stack_id)

    return req


def print_response(data):
    #if connect.JSON_FORM:
    jsonDumpsIndentStr = json.dumps(data, indent=connect.JSON_INDENT, ensure_ascii=False, sort_keys=True)
    print(jsonDumpsIndentStr)