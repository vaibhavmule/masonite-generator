"""A GeneratorProvider Service Provider"""
from masonite.provider import ServiceProvider
from app.commands.GeneratorCommand import GeneratorCommand


class GeneratorProvider(ServiceProvider):

    def register(self):
        self.app.bind('GeneratorCommand', GeneratorCommand())

    def boot(self):
        pass
