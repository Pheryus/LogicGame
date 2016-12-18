
class EnemiesPaths:

    def getPath(id):

        # rectangle
        if id == 0:
            return [[0, - 100], [-100, -100], [-100, 0], [0, 0]]
        # triangle
        elif id == 1:
            return [[-40, -30], [-80, 0], [0, 0]]
        elif id == 2:
            return [[0, -200], [0, 0]]
        else:
            return []

    def getSteps(id):

        if id == 0:
            return [[0, -4], [-4, 0], [0, 4], [4, 0]]
        elif id == 1:
            return [[-4, -3], [-4, 3], [4, 0]]
        elif id == 2:
            return [[0, -5], [0, 5]]
        else:
            return []

    def getEnemyPath(id):
        return EnemiesPaths.getPath(id), EnemiesPaths.getSteps(id)
