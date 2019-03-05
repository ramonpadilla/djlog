"""Classes create sentence objects based on the array received from the event class"""


class SimpleProposition():
    """Creates a sentence object of the form (Subject Verb Object)"""
    def __init__(self, array):
        self.subject = array[0]
        self.verb = array[1]
        self.file_type = array[3]
        last_dot = self.file_type.rfind('.')
        self.object = self.file_type[last_dot+1:]
        self.det = "a"
        self.sentence = self.subject+' '+self.verb+' '+self.det+' '+self.object
        self.array_words = [self.subject, self.verb, self.det, self.object, self.sentence]
        self.array_categories = ['subject', 'verb', 'determiner', 'object', 'sentence']


class NameProposition(SimpleProposition):
    """Creates a sentence object of the form (Subject Verb Object Modifier Name)"""
    def __init__(self, array):
        SimpleProposition.__init__(self, array)
        self.modifier = "called"
        self.name = array[4]
        self.det = array[2]
        self.sentence = self.subject+' '+self.verb+' '+self.det+' '+self.object+' '+self.modifier+' '+self.name
        self.array_words = [self.subject, self.verb, self.det, self.object, self.modifier, self.name, self.sentence]
        self.array_categories = ['subject', 'verb', 'determiner', 'object', 'modifier', 'name', 'sentence']


class PlaceProposition(NameProposition):
    """Creates a sentence object of the form (Subject Verb Object Modifier Name Place)"""
    def __init__(self, array):
        NameProposition.__init__(self, array)
        self.place = " in drive"
        self.sentence = self.subject+' '+self.verb+' '+self.det+' '+self.object+' '+self.modifier+' '+self.name+' '+self.place
        self.array_words = [self.subject, self.verb, self.det, self.object, self.modifier, self.name, self.place, self.sentence]
        self.array_categories = ['subject', 'verb', 'determiner', 'object', 'modifier', 'name', 'place', 'sentence']


class TimeProposition(PlaceProposition):
    """Creates a sentence object of the form (Subject Verb Object Modifier Name Place Time)"""
    def __init__(self, array):
        PlaceProposition.__init__(self, array)
        self.time = 'at ' + array[6]
        self.sentence = self.subject+' '+self.verb+' '+self.det+' '+self.object+' '+self.modifier+' '+self.name+' '+self.place+' '+self.time
        self.array_words = [self.subject, self.verb, self.det, self.object, self.modifier, self.name, self.place, self.time, self.sentence]
        self.array_categories = ['subject', 'verb', 'determiner', 'object', 'modifier', 'name', 'place', 'time', 'sentence']
