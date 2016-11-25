# -*- coding: utf-8 -*-
# import unittest
import actions
#import apiconfig.TestEnv_config as apimgr
import apiconfig.ProductionEnv_config as apimgr
# import datetime
import re

class test_demo_api():
    def test_login(self, login_obj):
        print "Testing logging in. Loading the configurations from login object."
        res = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
        print "Verifying the response with the expected output."
        assert res["error_code"]                == login_obj.err_code
        assert res["user"]["id"]                == login_obj.user_id
        assert res["user"]["v5_id"]             == login_obj.user_v5_id     #"%s | %s" % (res["user"]["nickName"], login_obj.user_nickName)
        assert res["user"]["account"]           == login_obj.user_account
        assert len(res["user"]["sessionId"])    == 32
        assert res["user"]["nickName"]          == login_obj.user_nickName #"%s | %s" % (res["user"]["nickName"], login_obj.user_nickName)
        assert res["user"]["createTimeMillis"] is not None
        assert res["user"]["avatar"]            == login_obj.user_avatar

    def test_find_account(self, login_obj, find_account_obj):
        print "Testing finding accounts... Trying to log in first."
        getSeesion      = actions.login(login_obj.url, login_obj.account, login_obj.nickName)["user"]["sessionId"]
        print "Login successful. Running the test."
        res             = actions.findAccount(getSeesion, find_account_obj.url, find_account_obj.account)

        print "Verifying the response with the expected output."
        assert res["error_code"]            == find_account_obj.err_code
        assert res["user"]["id"]            == find_account_obj.user_id
        assert res["user"]["v5_id"]         == find_account_obj.user_v5_id
        assert res["user"]["account"]       == find_account_obj.user_account
        assert res["user"]["sessionId"] is None
        assert res["user"]["nickName"]      == find_account_obj.user_nickName
        assert res["user"]["createTimeMillis"] is not None
        assert res["user"]["avatar"]        == find_account_obj.user_avatar

    def test_create_group(self, login_obj, create_group_obj):
        print "Testing creating a group... Trying to log in first."
        res_login   = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
        get_session = res_login["user"]["sessionId"]
        get_v5_id   = res_login["user"]["v5_id"]
        print "Login successful. Running the test."

        create_group_obj.result_creator         = get_v5_id
        create_group_obj.result_member_v5_id    = create_group_obj.result_member_v5_id + "," + get_v5_id
        create_group_obj.result_member_v5_id    = re.split(',', create_group_obj.result_member_v5_id)

        res         = actions.createGroup(get_session, create_group_obj.url, create_group_obj.members_v5_id)
        memberNum   = res["result"]["number"]

        res_result_member_v5_id     = []
        for count in (0, memberNum - 1):
            res_result_member_v5_id.append(res["result"]["member"][count]["v5_id"])

        for tmp in create_group_obj.result_member_v5_id:
            if tmp in res_result_member_v5_id:
                res_result_member_v5_id.remove(tmp)

        print "Verifying the response with the expected output."
        assert res["error_code"]            == create_group_obj.err_code
        assert res["result"]["id"] is not None
        assert res["result"]["v5_id"] is not None
        assert res["result"]["number"]      == 3
        assert res["result"]["creator"]     == create_group_obj.result_creator
        assert res["result"]["name"]        == create_group_obj.result_name
        assert res["result"]["createTime"] is not None
        assert res["result"]["updateTime"] is not None
        assert res["result"]["desc"]        == create_group_obj.result_desc
        assert res["result"]["avatar"]      == create_group_obj.result_avatar
        assert res_result_member_v5_id      == []

    def test_join_group(self, login_obj, join_group_obj):
        print "Testing inviting people into a group... Trying to log in first."
        res_login   = actions.login(login_obj.url, login_obj.account, login_obj.nickName)
        getSeesion  = res_login["user"]["sessionId"]
        print "Login successful. Running the test."

        res                 = actions.joinGroup(getSeesion, join_group_obj.url, join_group_obj.groupId, join_group_obj.members_v5_id)
        join_members_num    = len(res["result"]["join_members"])

        print "Verifying the response with the expected output."
        assert res["error_code"]        == join_group_obj.err_code
        assert res["result"]["id"]      == join_group_obj.result_id
        assert res["result"]["v5_id"]   == join_group_obj.result_v5_id

        res_result_member_v5_id             = []
        if res["result"]["join_members"]    == []:
            assert res_result_member_v5_id == join_group_obj.join_members_v5_id
        else:
            for count in (0, join_members_num - 1):
                res_result_member_v5_id.append(res["result"]["join_members"][count]["v5_id"])
            for tmp in join_group_obj.result_member_v5_id:
                if tmp in res_result_member_v5_id:
                    res_result_member_v5_id.remove(tmp)
                    assert res_result_member_v5_id == []


class test_core_server():
    def test_get_token(self, get_token_obj):
        print "Running test for getting the auth token..."
        res = actions.get_token(url=get_token_obj.url,
                                client_id=get_token_obj.client_id,
                                client_secret=get_token_obj.client_secret,
                                grant_type=get_token_obj.grant_type)

        res_access_token    = res["access_token"]
        res_token_type      = res["token_type"]
        res_expires_in      = res["expires_in"]
        res_scope           = res["scope"]

        print "Verifying the response with the expected output."
        assert len(res_access_token)    == 36
        assert res_token_type           == get_token_obj.token_type
        assert res_expires_in is not None
        assert res_scope                == get_token_obj.scope

    def test_get_userId_sessionId(self, get_token_obj, get_UserId_SessionId_obj):
        print "Running test for getting user ID and session ID from CG Cloud..."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        res = actions.getUserIdSessionId(token, get_UserId_SessionId_obj.url, get_UserId_SessionId_obj.app_user_id,
                                         get_UserId_SessionId_obj.app_user_nick_name)

        print "Verifying the response with the expected output."
        assert res["error_code"]                == get_UserId_SessionId_obj.error_code
        assert len(res["user"]["id"])           == 32
        assert len(res["user"]["session_id"])   == 32

    def test_get_sessionID(self, get_token_obj, get_sessionID_obj):
        print "Running the test for getting session ID..."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")

        res = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)

        print "Verifying the response with the expected output."
        assert res["error_code"]                == get_sessionID_obj.error_code
        assert len(res["user"]["id"])           == 32
        assert len(res["user"]["session_id"])   == 32

    def test_update_nickname(self, get_token_obj, get_sessionID_obj, update_nickname_obj):
        print "Running the test for updating nick name..."
        print "TEST**************************************"
        print update_nickname_obj.app_user_nick_name
        token       = actions.get_token(url=get_token_obj.url,
                                        client_id=get_token_obj.client_id,
                                        client_secret=get_token_obj.client_secret,
                                        grant_type=get_token_obj.grant_type,
                                        ret_type="header")
        sessionId   = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.updateNickname(token, sessionId, update_nickname_obj.url, update_nickname_obj.app_user_id,
                                    update_nickname_obj.app_user_nick_name)

        print "Verifying the response with the expected output."
        assert res["error_code"] == update_nickname_obj.error_code

    def test_create_group_test(self, get_token_obj, get_sessionID_obj, create_group_test_obj):
        print "Testing creating a group... Trying to log in first."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        sessionId = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.create_group_test(token, sessionId, create_group_test_obj.url,
                                        create_group_test_obj.members_user_id,
                                        create_group_test_obj.name,
                                        create_group_test_obj.desc, )

        assert res["creator"] == create_group_test_obj.result_creator
        #assert res["error_code"] == create_group_test_obj.error_code


    def test_update_group(self, get_token_obj, get_sessionID_obj, update_group_obj):
        print "Running the test for updating group..."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        sessionId = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"]["session_id"]
        res = actions.update_group(token, sessionId, update_group_obj.url, update_group_obj.groupId,
                                   update_group_obj.name, update_group_obj.desc)


        print "Verifying the response with the expected output."
        assert res["error_code"] == update_group_obj.error_code

    def test_get_group_infor(self, get_token_obj, get_sessionID_obj, get_group_infor_obj):
        print "Running the test for ask group information.."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        sessionId = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]
        res = actions.get_group_infor(token, sessionId, get_group_infor_obj.url, get_group_infor_obj.groupId)
        print "Verifying the response with the expected output."
        assert res["creator"] == get_group_infor_obj.result_creator

    def test_join_group_test(self, get_token_obj, get_sessionID_obj, join_group_test_obj):
        print "Testing inviting people into a group... Trying to log in first."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        sessionId = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]

        res = actions.join_group_test(token, sessionId, join_group_test_obj.url, join_group_test_obj.groupId,
                                      join_group_test_obj.join_members_user_id)

        print "Verifying the response with the expected output."
        assert res["error_code"] == join_group_test_obj.error_code

    #change by AndrewXU
    def test_remove_group_member(self, get_token_obj, get_sessionid_obj, get_group_obj):
        token = actions.get_token(get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")

        sessionId = actions.getSeesionId(token,
                                url=get_sessionid_obj.url,
                                app_user_id=get_sessionid_obj.app_user_id)

        res = actions.removeGroupMember(token,
                                        sessionId["user"]["session_id"],
                                        get_group_obj.url,
                                        get_group_obj.group_id,
                                        get_group_obj.member_v5_id)

        assert res["error_code"]        == get_group_obj.err_code
        #assert res["error"]              == get_group_obj.error

    def test_dissolve_group_test(self, get_token_obj, get_sessionID_obj, dissolve_group_test_obj):
        print "Testing inviting people into a group... Trying to log in first."
        token = actions.get_token(url=get_token_obj.url,
                                  client_id=get_token_obj.client_id,
                                  client_secret=get_token_obj.client_secret,
                                  grant_type=get_token_obj.grant_type,
                                  ret_type="header")
        sessionId = actions.getSeesionId(token, get_sessionID_obj.url, get_sessionID_obj.app_user_id)["user"][
            "session_id"]

        res = actions.dissolve_group_test(token, sessionId, dissolve_group_test_obj.url,
                                          dissolve_group_test_obj.groupId)
        print "Verifying the response with the expected output."
        assert res["error_code"] == dissolve_group_test_obj.error_code