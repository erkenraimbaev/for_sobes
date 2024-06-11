class EmailMixin:
    """
    make email from name
    """

    @staticmethod
    def make_email(name: str):
        return name.lower() + '@gmail.com'


class Human(EmailMixin):
    """
    Iam human
    """

    def __init__(self, name: str):
        self.name = name

    def print_about_me(self):
        return f'{self.name}I am human'


instance = Human(name='Victor')
print(instance.make_email(instance.name))
