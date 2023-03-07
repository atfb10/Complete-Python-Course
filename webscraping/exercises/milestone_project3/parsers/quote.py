from locators.quote_locators import QuoteLocators

class QuoteParser:
    '''
    given a specific quote div, find out data about the quote
    '''
    def __init__(self, parent):
        '''
        parent is parent tag that all other tags fall under
        '''
        self.parent = parent

    def __repr__(self) -> str:
        '''
        print of QuoteParser object returns a string of the quote with the author
        '''
        return f'\"{self.content}\" - {self.author}'

    @property
    def content(self):
        '''
        return quote content as a string
        '''
        return self.parent.select_one(QuoteLocators.CONTENT).string
    
    @property
    def author(self):
        '''
        return quote's author as a string
        '''
        return self.parent.select_one(QuoteLocators.AUTHOR).string
    
    @property
    def tags(self):
        '''
        return tags as a list of strings
        '''
        return [tag.string for tag in self.parent.select_one(QuoteLocators.TAGS)]