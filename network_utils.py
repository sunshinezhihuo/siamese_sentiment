"""
Created by John P Cavalieri on 6/3/16

"""
from exceptions import RuntimeError

import keras.backend as K


def get_network_layer_output(model, dataInput, layerNum, **kwargs):
    """

    :param model:
    :param dataInput:
    :param layerNum:
    :param kwargs:
    :return:
    """
    get_output = K.function([model.layers[0].input, K.learning_phase()],
                            [model.layers[layerNum].output])

    phase = kwargs.get('phase', None)

    if phase is None or phase == 'test':
        # output in test mode = 0
        layer_output = get_output([dataInput, 0])[0]

    elif phase == 'train':
        # output in train mode = 1
        layer_output = get_output([dataInput, 1])[0]

    else:
        raise RuntimeError("invalid phase passed to get_network_layer_output")

    return layer_output
