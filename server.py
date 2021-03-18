from bottle import run, get, post, put, delete,request

msglist = [{'mensaje1': 'Hola'},
            {'mensaje2': 'Mundo'}]

@get('/list')
def getList():
    return {'list':msglist}

@post('/list')
def addEntry():
    new_Message = {request.json.get('index') : request.json.get('text')}
    msglist.append(new_Message)
    return {'list': msglist}

@put('/list')
def updateEntry():
    update_Message = {'index': request.json.get('index'),'text': request.json.get('text')}
    dictinlist = None
    for x in msglist:
        if update_Message["index"] == list(x.keys())[0]:
            dictinlist = x
    msglist[msglist.index(dictinlist)] = {update_Message['index']: update_Message['text']}
    return {'list': msglist}

@delete('/list')
def deleteEntry():
    remove_Entry = {'index': request.json.get('index')}
    dictinlist = None
    for x in msglist:
        if remove_Entry["index"] == list(x.keys())[0]:
            dictinlist = x
    msglist.remove(dictinlist)
    return {'list': msglist}

run(reloader=True, debug=True)
