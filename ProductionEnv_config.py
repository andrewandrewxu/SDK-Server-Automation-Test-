# -*- coding: utf-8 -*-
from ApiClass import *
import re

DemoApi_url                 = "https://opendemo.v5.cn"

# changed by Xu Zhaoxuan
# define a user who has all the parameters needed below
App_a = {"app_key": 201713,
         "app_secret": "da5d63d9972765587888d1925c875e3a",
         "grant_type": "client_credentials",
         "accounts":
             {"account_01": { "account": "TEST_testAccount111",
                                "user_id": 10047,
                                "user_v5_id": "b3d590c0595c11e6afa2819403d79ace",
                                "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/b999baff-45b4-4147-957e-8c05d2c55b16.jpg",
                                "correct_err_code": 2000,
                                "nickName": "Iam_login_05"
                              },
              "account_03": { "account": "TEST_testAccount222",
                                "user_id": 10049,
                                "user_v5_id": "643a2d6059f611e6afa2819403d79ace",
                                "user_avatar": "http://cn.file.chatgame.me/api/file/download/2016/7/26/2/5c3d14cc-9fc0-40d5-8b04-9b02ca69f5ff.jpg",
                                "correct_err_code": 2000,
                                "nickName": "Iam_login_03"
                                }
             },
         "groups":
             {"group_01": {"members": "b3d590c0595c11e6afa2819403d79ace" + "," + "643a2d6059f611e6afa2819403d79ace",
                            "creator": "b3d590c0595c11e6afa2819403d79ace",
                            "group_name": "defaultGroupName",
                            "group_desc": "defaultGroupDesc",
                            "group_avatar": "http://new.image.chatgame.me/api/file/avatar/2015/11/24/8/9d6463ab-4083-4b01-a416-65e4e382ad00",
                            "group_id": "82b0a9005a0911e6afa2819403d79ace"
                            },
              "group_02": {"group_id": "20a783105b0211e690b2fb907fee57ba",
                            "group_name": "chen",
                            "group_desc": "testtesttest",
                            "creator": "b3d590c0595c11e6afa2819403d79ace"
                            }
             }
        }

#1.##########登录##########
#********** TESTCASE **********
DemoApi_login_01            = login()
# input
DemoApi_login_01.url        = DemoApi_url + "/users/login"
DemoApi_login_01.account    = App_a["accounts"]["account_01"]["account"]
DemoApi_login_01.nickName   = App_a["accounts"]["account_01"]["nickName"]

# expect
DemoApi_login_01.err_code                = App_a["accounts"]["account_01"]["correct_err_code"]
DemoApi_login_01.user_id                 = App_a["accounts"]["account_01"]["user_id"]
DemoApi_login_01.user_v5_id              = App_a["accounts"]["account_01"]["user_v5_id"]
DemoApi_login_01.user_account            = App_a["accounts"]["account_01"]["account"]
DemoApi_login_01.user_sessionId          = "len of expect = 32"
DemoApi_login_01.user_nickName           = App_a["accounts"]["account_01"]["nickName"]
DemoApi_login_01.user_createTimeMillis   = "expect is not None"
DemoApi_login_01.user_avatar             = App_a["accounts"]["account_01"]["user_avatar"]

#********** TESTCASE **********
DemoApi_login_03            = login()
# input
DemoApi_login_03.url        = DemoApi_url + "/users/login"
DemoApi_login_03.account    = App_a["accounts"]["account_03"]["account"]
DemoApi_login_03.nickName   = App_a["accounts"]["account_03"]["nickName"]

# expect
DemoApi_login_03.err_code                = App_a["accounts"]["account_03"]["correct_err_code"]
DemoApi_login_03.user_id                 = App_a["accounts"]["account_03"]["user_id"]
DemoApi_login_03.user_v5_id              = App_a["accounts"]["account_03"]["user_v5_id"]
DemoApi_login_03.user_account            = App_a["accounts"]["account_03"]["account"]
DemoApi_login_03.user_sessionId          = "len of expect = 32"
DemoApi_login_03.user_nickName           = App_a["accounts"]["account_03"]["nickName"]
DemoApi_login_03.user_createTimeMillis   = "expect is not None"
DemoApi_login_03.user_avatar             = App_a["accounts"]["account_03"]["user_avatar"]

#2.##########查找账户##########
#********** TESTCASE **********
DemoApi_FindAccountTest_01         = FindAccountTest()
# input
DemoApi_FindAccountTest_01.url     = DemoApi_url + "/users"
DemoApi_FindAccountTest_01.account = App_a["accounts"]["account_01"]["account"]

# expect
DemoApi_FindAccountTest_01.err_code               = App_a["accounts"]["account_01"]["correct_err_code"]
DemoApi_FindAccountTest_01.user_id                = App_a["accounts"]["account_01"]["user_id"]
DemoApi_FindAccountTest_01.user_v5_id             = App_a["accounts"]["account_01"]["user_v5_id"]
DemoApi_FindAccountTest_01.user_account           = App_a["accounts"]["account_01"]["account"]
DemoApi_FindAccountTest_01.user_sessionId         = "len of expect = 32"
DemoApi_FindAccountTest_01.user_nickName          = App_a["accounts"]["account_01"]["nickName"]
DemoApi_FindAccountTest_01.user_createTimeMillis  = "expect is not None"
DemoApi_FindAccountTest_01.user_avatar            = App_a["accounts"]["account_01"]["user_avatar"]



#3.##########创建群组##########
#********** TESTCASE **********
DemoApi_createGroup_01                  = createGroup()
# input
DemoApi_createGroup_01.url              = DemoApi_url + "/groups/"
#DemoApi_createGroup_01.members_v5_id    = App_a["accounts"]["account_01"]["user_v5_id"] + "," + App_a["accounts"]["account_03"]["user_v5_id"]
DemoApi_createGroup_01.members_v5_id    = App_a["groups"]["group_01"]["members"]

# expect
DemoApi_createGroup_01.err_code             = App_a["accounts"]["account_01"]["correct_err_code"]
DemoApi_createGroup_01.result_id            = "not None"
DemoApi_createGroup_01.result_v5_id         = "not None"
DemoApi_createGroup_01.result_number        = 3
DemoApi_createGroup_01.result_creator       = App_a["groups"]["group_01"]["creator"]
DemoApi_createGroup_01.result_name          = App_a["groups"]["group_01"]["group_name"]
DemoApi_createGroup_01.result_createTime    = "not None"
DemoApi_createGroup_01.result_updateTime    = "not None"
DemoApi_createGroup_01.result_desc          = App_a["groups"]["group_01"]["group_desc"]
DemoApi_createGroup_01.result_avatar        = App_a["groups"]["group_01"]["group_avatar"]
DemoApi_createGroup_01.result_member_v5_id  = DemoApi_createGroup_01.members_v5_id  #will be add the creator when run the testcase

#4.##########拉人进群##########
DemoApi_joinGroup_01                = joinGroup()
# input
DemoApi_joinGroup_01.url            = DemoApi_url + "/groups/join"
DemoApi_joinGroup_01.groupId        = App_a["groups"]["group_01"]["group_id"]
#DemoApi_joinGroup_01.members_v5_id  = "194178805a0b11e690b2fb907fee57ba"
DemoApi_joinGroup_01.members_v5_id  = App_a["accounts"]["account_01"]["user_v5_id"]

# expect
DemoApi_joinGroup_01.err_code           = 2000
DemoApi_joinGroup_01.result_id          = 10024
DemoApi_joinGroup_01.result_v5_id       = App_a["groups"]["group_01"]["group_id"]

DemoApi_joinGroup_01.join_members_v5_id = []


CoreServer_url                  = "https://cloudcn.v5.cn"
#1.##########获取token##########
#********** TESTCASE **********
CoreServer_getToken_01                 = getToken()
# input
CoreServer_getToken_01.url             = CoreServer_url + "/oauth/token"
CoreServer_getToken_01.client_id       = App_a["app_key"]
CoreServer_getToken_01.client_secret   = App_a["app_secret"]
CoreServer_getToken_01.grant_type      = App_a["grant_type"]

# expect
CoreServer_getToken_01.access_token    = "len of expect = 36"
CoreServer_getToken_01.token_type      = "bearer"
CoreServer_getToken_01.expires_in      = "not None"
CoreServer_getToken_01.scope           = "read"

#2.##########获取v5_id with sessionId##########
#********** TESTCASE **********
CoreServer_getUserIdSessionId_01    = getUserIdSessionId()
# input
CoreServer_getUserIdSessionId_01.app_user_id         = App_a["accounts"]["account_01"]["account"]
CoreServer_getUserIdSessionId_01.app_user_nick_name  = App_a["accounts"]["account_01"]["nickName"]
CoreServer_getUserIdSessionId_01.url                 = CoreServer_url + "/open/api/user/auth?"
CoreServer_getUserIdSessionId_01.header              = {}    #need Token

# expect
CoreServer_getUserIdSessionId_01.error_code          = 2000
CoreServer_getUserIdSessionId_01.user_id             = "len of expect = 32"
CoreServer_getUserIdSessionId_01.user_session_id     = "len of expect = 32"

#3.##########获取sessionId##########
#********** TESTCASE **********
CoreServer_getSessionID_01              = getSessionID()
# input
CoreServer_getSessionID_01.app_user_id  = App_a["accounts"]["account_01"]["user_v5_id"]
CoreServer_getSessionID_01.url          = CoreServer_url + "/open/api/session/auth?"
CoreServer_getSessionID_01.header       = {}        #need Token

# expect
CoreServer_getSessionID_01.error_code       = 2000
CoreServer_getSessionID_01.user_id          = "len of expect = 32"
CoreServer_getSessionID_01.user_session_id  = "len of expect = 32"

###########更新用户昵称#########
#********** TESTCASE ************
CoreServer_UpdateNicknameTest_01           = UpdateNicknameTest()
#input
CoreServer_UpdateNicknameTest_01.url       = CoreServer_url + "/open/api/user/update"
CoreServer_UpdateNicknameTest_01.app_user_id = App_a["accounts"]["account_01"]["user_v5_id"]
CoreServer_UpdateNicknameTest_01.app_user_nick_name = App_a["accounts"]["account_01"]["account"]

#expect
CoreServer_UpdateNicknameTest_01.error_code   = 2000


##########创建群组##########
#********** TESTCASE **********
CoreServer_CreatGroupTest_02                    =CreatGroupTest()
# input
CoreServer_CreatGroupTest_02.url                = CoreServer_url + "/open/api/group/create"
CoreServer_CreatGroupTest_02.members_user_id    = App_a["groups"]["group_01"]["group_id"]
CoreServer_CreatGroupTest_02.name               = App_a["groups"]["group_01"]["group_name"]
CoreServer_CreatGroupTest_02.desc               = App_a["groups"]["group_01"]["group_desc"]

# expect
CoreServer_CreatGroupTest_02.result_id            = "not None"
CoreServer_CreatGroupTest_02.result_number        = 3
CoreServer_CreatGroupTest_02.result_creator       = App_a["groups"]["group_01"]["creator"]
CoreServer_CreatGroupTest_02.result_name          = App_a["groups"]["group_01"]["group_name"]
CoreServer_CreatGroupTest_02.result_createTime    = "not None"
CoreServer_CreatGroupTest_02.result_updateTime    = "not None"
CoreServer_CreatGroupTest_02.result_desc          = App_a["groups"]["group_01"]["group_desc"]
CoreServer_CreatGroupTest_02.result_member_user_id  = CoreServer_CreatGroupTest_02.result_member_user_id

##########更新群组##########
#********** TESTCASE **********
CoreServer_UpdateGroupTest_01                =UpdateGroupTest()
#input
CoreServer_UpdateGroupTest_01.groupId     =App_a["groups"]["group_02"]["group_id"]
#CoreServer_UpdateGroupTest_01.groupId     ="635a79905ec911e690b2fb907fee57ba"
CoreServer_UpdateGroupTest_01.url          =CoreServer_url + "/open/api/group/update"
CoreServer_UpdateGroupTest_01.desc         =App_a["groups"]["group_02"]["group_desc"]
CoreServer_UpdateGroupTest_01.name         =App_a["groups"]["group_01"]["group_name"]

#expect
CoreServer_UpdateGroupTest_01.error_code   = 2000

###########获取群组信息##########
#********** TESTCASE *************
CoreServer_GetGroupInforTest_01                      =GetGroupInforTest()
#input
CoreServer_GetGroupInforTest_01.url                  = CoreServer_url + "/open/api/group/get?"
CoreServer_GetGroupInforTest_01.groupId              = App_a["groups"]["group_02"]["group_id"]
#expect
CoreServer_GetGroupInforTest_01.err_code             = 2000
CoreServer_GetGroupInforTest_01.result_id            = "not None"
CoreServer_GetGroupInforTest_01.result_creator       = App_a["groups"]["group_02"]["creator"]
CoreServer_GetGroupInforTest_01.result_create_time   = "not None"
CoreServer_GetGroupInforTest_01.result_update_time   = "not None"
CoreServer_GetGroupInforTest_01.result_desc          = "testtesttest"
CoreServer_GetGroupInforTest_01.result_name          = "liujieGroup"
CoreServer_GetGroupInforTest_01.result_number        = 3
CoreServer_GetGroupInforTest_01.result_memeber_user_id = CoreServer_GetGroupInforTest_01.result_memeber_user_id

##########加入群组##########
#********** TESTCASE **********
CoreServer_JoinGroupTest_01                 =JoinGroupTest()

# input
CoreServer_JoinGroupTest_01.url             = CoreServer_url + "/open/api/group/join"
CoreServer_JoinGroupTest_01.groupId         = App_a["groups"]["group_01"]["group_id"]
CoreServer_JoinGroupTest_01.members_user_id = App_a["accounts"]["account_03"]["user_v5_id"]

# expect
CoreServer_JoinGroupTest_01.error_code            = 2000
CoreServer_JoinGroupTest_01.join_members_user_id  = App_a["accounts"]["account_03"]["user_v5_id"]
#CoreServer_JoinGroupTest_01.nickname            = "TEST_testAccount114"
#CoreServer_JoinGroupTest_01.createTime          = "1470387712169"

#########移除群成员#########
#*********TESTCASE************
CoreServer_removeGroupMember_01                     = RemoveGroupMemberTest()
#input
CoreServer_removeGroupMember_01.url                 = CoreServer_url + "/open/api/group/remove"
CoreServer_removeGroupMember_01.group_id            = App_a["groups"]["group_02"]["group_id"]
CoreServer_removeGroupMember_01.member_v5_id        = App_a["accounts"]["account_03"]["user_v5_id"]

#expect
CoreServer_removeGroupMember_01.err_code            = 2000
CoreServer_removeGroupMember_01.error               = None

##########解散群组##########
#********** TESTCASE **********
CoreServer_DissolveGroupTest_01                 = DissolveGroupTest()

# input
CoreServer_DissolveGroupTest_01.url             = CoreServer_url + "/open/api/group/remove"
CoreServer_DissolveGroupTest_01.groupId         = App_a["groups"]["group_02"]["group_id"]

# expect
CoreServer_DissolveGroupTest_01.error_code            = 2000