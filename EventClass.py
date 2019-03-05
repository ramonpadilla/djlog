"""Crates an event object based on a Drive file JSON"""
import json


class Event():
    """This object is characterize as taking a json as argument and Returns
    a linguistic and non-linguistic array"""
    def __init__(self, data):
        """Takes a json (Drive File Json) as argument, coverts it into a dictionary
        and teases apart all the information we need for the natural language
        generation"""
        self.data = data
        self.dicts = json.loads(data)
        self.agent = self.dicts["lastModifyingUser"]["displayName"]
        self.object = self.dicts["mimeType"]
        self.object_name = self.dicts["name"]
        self.place = self.dicts["kind"]
        self.link = self.dicts["webViewLink"]
        self.email = self.dicts["lastModifyingUser"]["emailAddress"]
        self.file_id = self.dicts["id"]
        self.created_time = self.dicts["createdTime"]
        self.mod_time = self.dicts["modifiedTime"]
        self.date_ct = self.created_time[0:9]
        self.date_mt = self.mod_time[0:9]
        #Below is the non-linguistic array.
        self.array_non_ling = [self.file_id, self.link, self.email]
    def action(self):
        """This method distinguishes between created or modified file"""
        if self.date_ct == self.date_mt:
            self.verb = "created"
            self.time = self.date_ct
        else:
            self.verb = "modified"
            self.time = self.date_mt    
        return self.verb
        return self.time
    def article(self):
        """Returns the appropiate article depending on the verb return by
        def action()"""
        Event.action(self)
        if self.verb == "created":
            self.det = "a"
        else:
            self.det = "the"
    def array(self):
        """This method returns the ordered linguistic array"""
        Event.action(self)
        Event.article(self)
        self.array_nlg = [self.agent, self.verb, self.det, self.object, self.object_name, self.place, self.time]
        return self.array_nlg
