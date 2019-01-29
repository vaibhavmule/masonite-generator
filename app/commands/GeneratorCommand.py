"""A GeneratorCommand Command"""

from cleo import Command


class GeneratorCommand(Command):
    """Scaffold CRUD controller.

    gen
        {model : model name}
        {table_name : plural table name}
        {fields* : fields for model}
    """

    def handle(self):
        model = self.argument('model')
        table_name = self.argument('table_name')
        fields = self.argument('fields')
        print(model, table_name, fields)
