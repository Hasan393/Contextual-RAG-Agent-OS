class MemoryHierarchy:
    def __init__(self):
        self.short_term =[]
        self.working_context = ""
        self.long_term =[]

    def add_short_term(self, item):
        self.short_term.append(item)

    def get_working_context(self):
        return self.working_context

    def update_working_context(self, context):
        self.working_context = context

    def add_long_term(self, item):
        self.long_term.append(item)