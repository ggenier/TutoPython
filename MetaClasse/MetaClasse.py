trace_classes = {}  # Notre dictionnaire vide


class MetaWidget(type):
    """Notre métaclasse pour nos Widgets.

    Elle hérite de type, puisque c'est une métaclasse.
    Elle va écrire dans le dictionnaire trace_classes à chaque fois
    qu'une classe sera créée, utilisant cette métaclasse naturellement."""

    def __init__(cls, nom, bases, dict):
        """Constructeur de notre métaclasse, appelé quand on crée une classe."""
        type.__init__(cls, nom, bases, dict)
        trace_classes[nom] = cls


class Widget(metaclass=MetaWidget):
    """Classe mère de tous nos widgets."""

    def __init__(self):
        print("Widget init")


class bouton(Widget):
    """Une classe définissant le widget bouton."""

    pass

print(trace_classes)
w = Widget()