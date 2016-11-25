# -*- coding: utf-8 -*-
import urllib
import urllib2

#PART 1------------------------- 功能性函数包括 http处理，字符串处理等-------------------------
def get(url, header):
    # request headers
    req = urllib2.Request(url, None, header)
    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    # send request and get response handle
    res = urllib2.urlopen(req)

    # response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    # response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    # response body
    res_body = res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def post(url, data, header):
    #request headers
    req_header = header

    #request body
    data = urllib.urlencode(data)

    #pre--request
    req = urllib2.Request(url, data, req_header)

    #req_header_tmp = req.get_header("User-agent")
    #print "***request header_tmp = *** %s" % req_header_tmp

    req_header_get = req.header_items()
    print "***request header_get = ***\n%s" % req_header_get

    req_body = req.get_data()
    print "***request body = ***\n%s" % req_body
    #send request and get response handle
    res = urllib2.urlopen(req)

    #response code
    res_code = res.getcode()
    print "***response code = ***\n%s" % res_code
    #response header
    res_header = res.info()
    print "***response header = ***\n%s" % res_header
    #response body
    res_body =  res.read()
    print "***response body = ***\n%s" % res_body
    res.close()

    return res_body

def null2None2dict(res=""):
    res = res.replace("null", "None")
    return eval(res)


# PART 2------------------------- CLIENT -----> SERVER -------------------------
def login(url="", account="", nick_name=None):
    # PARAMETER:        url和account不可以为空  nick_name可以为空(不传)   3个都是string类型
    # OUTPUT:           http response body----->dict类型输出
    login_url               = url
    data                    = {}
    data["account"]         = account
    if nick_name:
        data["nickName"]    = nick_name
    header                  = {}

    response = post(login_url, data, header)
    return null2None2dict(response)


def findAccount(sessionID="", url="", account=""):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = {"session": sessionID}
    full_url        = url + "?account=" + account

    response        = get(full_url, header)
    return null2None2dict(response)

def createGroup(sessionID="", url="", members=""):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = {"session": sessionID}
    data            = {"members": members}

    response        = post(url, data, header)
    return null2None2dict(response)

def joinGroup(sessionID="", url="",groupId="", members=""):
    # PARAMETER:        4个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = {"session": sessionID}
    data            = {"groupId":groupId, "members": members}

    response        = post(url, data, header)
    return null2None2dict(response)


# PART 3------------------------- SERVER -----> SERVER -------------------------
def get_token(url="", client_id=0, client_secret="",grant_type="", ret_type=""):
    # PARAMETER:        4个参数（string,int,string,string,string），只有最后一个可以为空
    # 特别说明:         ret_type 为header时，return 鉴权头
    # OUTPUT:           http response body----->dict类型输出
    url         = url
    data        = {"client_id":client_id, "client_secret":client_secret, "grant_type":grant_type}
    header      = {}

    res         = post(url, data, header)

    if ret_type == "header":
        res             = null2None2dict(res)
        access_token    = res["access_token"]
        token_type      = res["token_type"].capitalize()
        return {"Authorization": token_type + " " + access_token}
    else:
        return  null2None2dict(res)

def getUserIdSessionId(token={}, url="", app_user_id="", app_user_nick_name=""):
    # PARAMETER:        token -- dict类型，其他3个string类型参数，只有最后一个可以为空
    #  OUTPUT:           http response body----->dict类型输出
    url_pre         = url
    if app_user_nick_name:
        url_full    = url_pre + "app_user_id=%s&app_user_nick_name=%s" %(app_user_id,app_user_nick_name)
    else:
        url_full    = url_pre + "app_user_id=%s" % app_user_id

    header = token

    res             = get(url_full, header)
    return null2None2dict(res)

def getSeesionId(token={}, url="", app_user_id=""):
    # PARAMETER:        token -- dict类型，其他2个string类型参数
    # OUTPUT:           http response body----->dict类型输出
    url_pre         = url
    url_full        = url_pre + "user_id=%s" % app_user_id
    header          = token

    res             = get(url_full, header)
    return null2None2dict(res)


def updateNickname(token={}, getSession="", url="",app_user_id="", app_user_nick_name=""):
    # PARAMETER:        token -- dict类型，其他4个string类型参数
    #  OUTPUT:           http response body----->dict类型输出
    data        = {"user_id":app_user_id,"nick_name":app_user_nick_name}
    header      = token
    header_ext  = {"client-session":getSession}
    header.update(header_ext)

    res         = post(url, data, header)
    return null2None2dict(res)

def create_group_test(token={}, sessionID="", url="", members="", name="", desc=""):
    # PARAMETER:        3个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header      = token
    header_ext  = {"client-session":sessionID}
    header.update(header_ext)

    #header          = {"session": sessionID}
    data            = {"member": members, "name":name, "desc":desc}

    response        = post(url, data, header)
    return null2None2dict(response)

def update_group(token={}, sessionID="", url="", groupId="",name="", desc=""):
    # PARAMETER:        token -- dict类型，其他4个string类型参数
    #  OUTPUT:           http response body----->dict类型输出
    header      = token
    data        = {"groupId":groupId,"name":name,"desc":desc}

    header_ext  = {"client-session":sessionID}
    header.update(header_ext)

    res         = post(url, data, header)
    return null2None2dict(res)

def get_group_infor(token={}, sessionID="", url="",groupId=""):
    header     = token
    url        = url+"groupId=%s" %(groupId)
    header_ext ={"client-session":sessionID}
    header.update(header_ext)
    res        =get(url, header)
    return null2None2dict(res)

def join_group_test(token={}, getSession="", url="",groupId="", members=""):
    # PARAMETER:        4个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {"groupId": groupId, "member": members}

    res             = post(url, data, header)
    return null2None2dict(res)

# changed by AndrewXU
def removeGroupMember(token={}, sessionid="", url="", groupID="", members="", ):
    header          = token
    header_ext      = {"client-session":sessionid}
    header.update(header_ext)
    data            = {"groupId": groupID, "member": members}
    response        = post(url, data, header)
    return null2None2dict(response)

def dissolve_group_test(token={}, getSession="", url="",groupId=""):
    # PARAMETER:        4个string类型参数，都不可以为空
    # OUTPUT:           http response body----->dict类型输出
    header          = token
    header_ext      = {"client-session": getSession}
    header.update(header_ext)
    data            = {"groupId": groupId}

    res             = post(url, data, header)
    return null2None2dict(res)