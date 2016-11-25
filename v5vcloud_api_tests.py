# -*- coding: utf-8 -*-
import unittest
import modules
#import apiconfig.TestEnv_config as apimgr
import apiconfig.ProductionEnv_config as apimgr
import datetime

class demo_api_tests(unittest.TestCase):
    test = modules.test_demo_api()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass

    def test0001_login(self):
        print "B----------------------------------test0001_login-------------------------------------B"
        login = apimgr.DemoApi_login_01
        self.test.test_login(login)
        print "E----------------------------------test0001_login-------------------------------------E"

    def test0003_login(self):
        print "B----------------------------------test001_login-------------------------------------B"
        login = apimgr.DemoApi_login_03
        self.test.test_login(login)
        print "E----------------------------------test001_login-------------------------------------E"

    def test0004_find_account(self):
        print "B----------------------------------test0002_find_account----------------------------------B"
        login_info  = apimgr.DemoApi_login_01
        info        = apimgr.DemoApi_FindAccountTest_01
        self.test.test_find_account(login_info, info)
        print "E----------------------------------test0002_find_account----------------------------------E"

    def test0201_create_group(self):
        print "B----------------------------------test0201_create_group----------------------------------B"
        login_info  = apimgr.DemoApi_login_03
        info        = apimgr.DemoApi_createGroup_01
        self.test.test_create_group(login_info, info)
        print "E----------------------------------test0201_create_group----------------------------------E"

    def test0301_join_group(self):
        print "B----------------------------------test0301_joinGroup_01----------------------------------B"
        login_info  = apimgr.DemoApi_login_03
        info        = apimgr.DemoApi_joinGroup_01
        self.test.test_join_group(login_info, info)
        print "E----------------------------------test0301_joinGroup_01----------------------------------E"

class core_server_tests(unittest.TestCase):
    test = modules.test_core_server()
    def setUp(self):
        currentTime = str(datetime.datetime.now())[0:19]
        print "@@@@@@@@@@-- RUN TESTCASE --%s@@@@@@@@@@" % currentTime
        pass

    def tearDown(self):
        pass

    def test0001_get_token(self):
        print "B----------------------------------test0001_get_token----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        self.test.test_get_token(auth)
        print "E----------------------------------test0001_get_token----------------------------------E"

    def test0101_get_userId_sessionId(self):
        print "B----------------------------------test0101_get_userId_sessionId----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        info = apimgr.CoreServer_getUserIdSessionId_01
        self.test.test_get_userId_sessionId(auth, info)
        print "E----------------------------------test0101_get_userId_sessionId----------------------------------E"

    def test0201_get_sessionID(self):
        print "B----------------------------------test0201_get_sessionID----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        info = apimgr.CoreServer_getSessionID_01
        self.test.test_get_sessionID(auth, info)
        print "E----------------------------------test0201_get_sessionID----------------------------------E"

    def test0301_update_nickname(self):
        print "B----------------------------------test0301_update_nickname----------------------------------B"
        auth    = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info    = apimgr.CoreServer_UpdateNicknameTest_01
        self.test.test_update_nickname(auth, session, info)
        print "E----------------------------------test0301_update_nickname----------------------------------E"

    def test0401_create_group_test(self):
        print "B----------------------------------test0401_create_group_test----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_CreatGroupTest_02
        self.test.test_create_group_test(auth, session, info)
        print "E----------------------------------test0401_create_group_test----------------------------------E"

    def test0501_update_group(self):
        print "B----------------------------------test0501_update_group----------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_UpdateGroupTest_01
        self.test.test_update_group(auth, session, info)
        print "E----------------------------------test0501_update_group----------------------------------E"

    def test0601_get_group_infor_test(self):
        print "B----------------------------------test0601_get_group_infor----------------------------------B"
        auth    = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_GetGroupInforTest_01
        self.test.test_get_group_infor(auth, session, info)
        print "E----------------------------------test0601_get_group_infor----------------------------------E"

    def test0701_join_group_test(self):
        print "B----------------------------------test0701_join_group_test---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_JoinGroupTest_01
        self.test.test_join_group_test(auth, session, info)
        print "E----------------------------------test0701_join_group_test-----------------------------------E"

    def test0801_remove_group_member(self):
        print "B----------------------------------test 0801_create_group----------------------------------B"
        session    = apimgr.CoreServer_getSessionID_01
        token      = apimgr.CoreServer_getToken_01
        Info       = apimgr.CoreServer_removeGroupMember_01
        self.test.test_remove_group_member(token,session,Info)
        print "E----------------------------------test 0801_create_group----------------------------------E"

    def test0901_dissolve_group_test(self):
        print "B----------------------------------test0901_dissolve_group_test---------------------------------B"
        auth = apimgr.CoreServer_getToken_01
        session = apimgr.CoreServer_getSessionID_01
        info = apimgr.CoreServer_DissolveGroupTest_01
        self.test.test_dissolve_group_test(auth, session, info)
        print "E----------------------------------test0901_dissolve_group_test-----------------------------------E"