from kimera_core.components.tools.serializers._pickle import Pickle
from kimera_core.components.tools.serializers.custom import KimeraSerializer


def pickle():
    return Pickle()


def custom():
    return KimeraSerializer()
