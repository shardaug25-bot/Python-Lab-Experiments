from model import LibraryModel
from view import LibraryView
from controller import LibraryController

if __name__ == "__main__":
    model = LibraryModel()
    view = LibraryView()
    controller = LibraryController(model, view)
    controller.run()