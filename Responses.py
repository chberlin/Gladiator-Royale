import abc

class ResponseStrategy(abc.ABC):
    @abc.abstractmethod
    def response(self):
        pass


class NegativeResponse(ResponseStrategy):

    def response(self, event):
        reaction = {'health':'Yay ', 'death':'Yay ', 'win': 'Boo '}
        print(reaction[event], end=" ")


class PostiveResponse(ResponseStrategy):

    def response(self, event):
        reaction = {'health': 'Boo ', 'death': 'Boo ', 'win': 'Yay '}
        print(reaction[event], end=" ")



class NeutralResponse(ResponseStrategy):

    def response(self, event):
        reaction = {'health': 'Gasp ', 'death': 'Gasp ', 'win': 'Ehh '}
        print(reaction[event], end=" ")

