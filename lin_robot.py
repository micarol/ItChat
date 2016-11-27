#coding=utf-8
import itchat


@itchat.msg_register(['Note'])
def text_reply(msg):
    print '== msg_register(Note) begins ====='
    print msg
    print '=================================='
    itchat.add_friend(userName=msg['FromUserName'], status=2)
    itchat.add_friend(userName=msg['FromUserName'], status=3)
    print '== msg_register(Note) ends ======='
    return u"Hello !"


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print '== msg_register(TEXT) begins ====='
    print msg
    print '== msg_register(TEXT) ends ======='
    response = ''
    # print 'Text = '
    # print msg['Text']
    itchat.get_friends(update=True)
    itchat.add_friend(userName=msg['FromUserName'], status=2)
    itchat.add_friend(userName=msg['FromUserName'], status=3)
    print 'sssssssss1'
    print itchat.search_friends(userName=msg['FromUserName'])
    print 'sssssssss2'
    itchat.update_friend(userName=msg['FromUserName'])
    print 'sssssssss3'
    print itchat.search_friends(userName=msg['FromUserName'])
    print 'sssssssss4'
    if msg['Text'] == 'streaming':
        userName = itchat.search_friends(userName=msg['FromUserName'])
        userNamesToInvide = [userName]
        # ↓↓↓↓↓ 以下是邀请到群里；需要之前就有 userNamesToInvide
        roomName = itchat.search_chatrooms(name=u'Spark Streaming 交流群')[0]['UserName']
        itchat.add_member_into_chatroom(roomName, userNamesToInvide, useInvitation=True)
        # ↑↑↑↑↑ 以上是邀请到群里
        response = u'Let\'s streaming!'
    else:
        response = u'请回复如下关键字之一：\nstreaming'
    return response


@itchat.msg_register(itchat.content.FRIENDS)
def text_reply(msg):
    print '== msg_register(FRIENDS) begins ====='
    print msg
    print '== msg_register(FRIENDS) ends ======='
    itchat.add_friend(userName=msg['FromUserName'], status=2)
    itchat.add_friend(userName=msg['FromUserName'], status=3)
    return u'Hi !'


@itchat.msg_register(itchat.content.SYSTEM)
def text_reply(msg):
    # itchat.send_msg(msg='hi', toUserName=msg['Text'][0]['UserName'])
    print '== msg_register(SYSTEM) begins ====='
    print msg
    '''
    userName = msg['Text'][0]
    itchat.send_msg(msg=u'Hi!', toUserName=userName)
    userNamesToInvide=[userName]
    print 'userNamesToInvide'
    print userNamesToInvide
    # ↓↓↓↓↓ 以下是邀请到群里；需要之前就有 userNamesToInvide
    roomName = itchat.search_chatrooms(name=u'Spark Streaming 交流群')[0]['UserName']
    itchat.add_member_into_chatroom(roomName, userNamesToInvide, useInvitation=True)
    # ↑↑↑↑↑ 以上是邀请到群里
    '''
    print '== msg_register(SYSTEM) ends ======='
    return u'Hi !!!'


itchat.auto_login(hotReload=True)
# rooms = itchat.get_chatrooms(update=True)
# print rooms
itchat.run()
