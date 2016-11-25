# -*- coding: utf-8 -*-

#每一个接口动作写一个类
#……………………………………………………………… client to demoServer ………………………………………………………………
#登录类
class login():
    ''' request '''
    url                 = ""
    account             = ""
    nickName            = ""

    # expect
    err_code                    = None
    user_id                     = None
    user_v5_id                  = None
    user_account                = None
    user_sessionId              = None
    user_nickName               = None
    user_createTimeMillis       = None
    user_avatar                 = None

class FindAccountTest:
    '''request'''
    url                 = ""
    account             = ""
    #expect
    error_code          = 2000
    user_id             = None
    user_v5_id          = None
    user_account        = None
    user_sessionId      = None
    user_nickName       = None
    user_createTimeMillis  = None
    user_avatar         = None

class createGroup():
    ''' request '''
    url             = ""
    members_v5_id   = ""

    # expect
    err_code                    = None
    result_id                   = None
    result_v5_id                = None
    result_number               = None
    result_creator              = None
    result_name                 = None
    result_createTime           = None
    result_updateTime           = None
    result_desc                 = None
    result_avatar               = None
    result_member_v5_id         = None

class joinGroup:
    ''' request '''
    url             = ""
    groupId         = ""
    members_v5_id   = ""

    # expect
    err_code                        = None
    result_id                       = None
    result_v5_id                    = None
    join_members_v5_id              = None


#……………………………………………………………… client to demoServer ………………………………………………………………
class getToken:
    '''request'''
    url             = ""
    client_id       = None
    client_secret   = ""
    grant_type      = ""

    # expect
    access_token    = None
    token_type      = None
    expires_in      = None
    scope           = None

class getUserIdSessionId:
    '''request'''
    app_user_id         = ""
    app_user_nick_name  = ""
    url                 = ""
    header              = {}

    # expect
    error_code      = None
    user_id         = None
    user_session_id = None

class getSessionID:
    '''request'''
    app_user_id = ""
    url         = ""
    header      = {}

    # expect
    error_code      = None
    user_id         = None
    user_session_id = None

class UpdateNicknameTest:
    '''request'''
    app_user_id         = ""
    app_user_nick_name  = ""
    url                 = ""


    # expect
    error_code          = None

class CreatGroupTest():
    ''' request '''
    url                 = ""
    members_user_id     = ""
    result_name         = ""
    desc                = ""

    # expect
    result_id                   = None
    result_number               = None
    result_creator              = None
    result_name                 = None
    result_create_time          = None
    result_update_time          = None
    result_desc                 = None
    result_member_user_id       = None
    result_conversation         = None


class UpdateGroupTest:
    '''request'''
    url                 =""
    groupId            =""
    result_name         =""
    desc                =""

    #expect
    error_code         =None

class GetGroupInforTest:
    """request"""
    url             = ""
    groupId         = ""

    #expect
    err_code                        = None
    result_id                       = None
    result_creator                  = None
    result_create_time              = None
    result_update_time              = None
    result_desc                     = None
    result_name                     = None
    result_number                   = None
    result_memeber_user_id          = None
    result_conversation             = None


class JoinGroupTest:
    ''' request '''
    url                   = ""
    groupId               = ""
    join_members_user_id  = ""

    # expect
    error_code                       = None
    result_join_members_user_id      = None
    #join_members_nickname           = None
    #join_members_createTime         = None

class RemoveGroupMemberTest:
    '''request'''
    url                 = ""
    group_id            = ""
    member_v5_id        = ""

    #expect
    err_code            = None
    error               = ""


class DissolveGroupTest:
    ''' request '''
    url                   = ""
    groupId               = ""

    # expect
    error_code                       = None