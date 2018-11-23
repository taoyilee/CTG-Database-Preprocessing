from lark import Lark

from lark import Tree, Transformer, Token
from lab_measurment import LabMeasurment
from block import Block
from hea import Hea
from signal import Signal


class EvaluateHea(Transformer):
    _record_name = ""
    _number_of_signals = 1
    _sampling_frequency = 250
    _hea = None

    def record(self, args):
        self._hea = Hea(record_name=self._record_name, number_of_signals=self._number_of_signals,
                        sampling_frequency=self._sampling_frequency)
        return args

    def record_name(self, args):
        self._record_name = args[0].value
        return self._record_name

    def number_of_signals(self, args):
        self._number_of_signals = args[0].value
        return self._number_of_signals

    def signal_spec(self, args):
        s = Signal.from_subtree(Tree("signal_spec", args))
        self._hea.add_signal(s)
        return s

    def sampling_frequency(self, args):
        self._sampling_frequency = args[0].value
        return self._sampling_frequency

    def signal_block(self, args):
        return Block("Signal", args)

    def neonatal_oc_block(self, args):
        self._hea.add_blocks(Block("Neonatal Outcome", args))

    def outcome_block(self, args):
        self._hea.add_blocks(Block("Outcome", args))

    def maternal_block(self, args):
        self._hea.add_blocks(Block("Maternal", args))

    def fetus_block(self, args):
        self._hea.add_blocks(Block("Fetus", args))

    def delivery_block(self, args):
        self._hea.add_blocks(Block("Delievery", args))

    def lab_meas_field(self, args):
        return " ".join([a.value for a in args])

    def addi_block(self, args):
        return args[1:]

    def start(self, args):
        return self._hea

    def lab_meas_number(self, args):
        return float(args[0].value)

    def lab_meas(self, args):
        return LabMeasurment(args[0], args[1])


def print_hea(file_name):
    with open(file_name, "r") as f:
        line = f.readline()
        while line != "":
            print(line, end="")
            line = f.readline()


def read_hea(file_name):
    with open(file_name, "r") as f:
        lines = f.read()

    with open("grammar/hea.g", "r") as f:
        grammar = f.read()

    parser = Lark(grammar, parser="lalr")
    tree = parser.parse(lines)
    return EvaluateHea().transform(tree)
