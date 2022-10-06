REGISTRY = {}

from .rnn_agent import RNNAgent
from .rnn_msg_agent import RnnMsgAgent
from .immac_agent import ImmacAgent
from .srmac_agent import SRMACAgent

REGISTRY["rnn"] = RNNAgent
REGISTRY['rnn_msg'] = RnnMsgAgent
REGISTRY['immac_agent'] = ImmacAgent
REGISTRY['immac-vffac'] = RnnMsgAgent
REGISTRY['srmac_agent'] = SRMACAgent