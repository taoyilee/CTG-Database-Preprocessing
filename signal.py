from lark import Transformer


class EvaluateSignal(Transformer):
    def signal_description(self, args):
        self._signal_description = args[0].value
        return self._signal_description

    def signal_format(self, args):
        self._signal_format = args[0].value
        return self._signal_format

    def signal_spec(self, args):
        return Signal(self._signal_description, signal_format=self._signal_format, dat_file=self._dat_name,
                      adc_spec=args[2])

    def adc_zero(self, args):
        args[0] = {"adc_zero": args[0].value}
        if len(args) == 2:
            args[0].update(args[1])
        return args[0]

    def dat_name(self, args):
        self._dat_name = f"dat/{args[0].value}.dat"
        return self._dat_name

    def adc_units(self, args):
        args[0] = {"adc_units": args[0].value}
        return args[0]

    def baseline_adc(self, args):
        args[0] = {"baseline_adc": args[0].value}
        if len(args) > 1:
            for a in args[1:]:
                args[0].update(a)
        return args[0]

    def adc_gain(self, args):
        args[0] = {"adc_gain": args[0].value}
        if len(args) > 1:
            for a in args[1:]:
                args[0].update(a)
        return args[0]

    def adc_resol(self, args):
        args[0] = {"adc_resol": args[0].value}
        if len(args) == 2:
            args[0].update(args[1])
        return args[0]

    def adc_block_size(self, args):
        return {"adc_block_size": args[0].value}

    def adc_checksum(self, args):
        args[0] = {"adc_checksum": args[0].value}
        if len(args) == 2:
            args[0].update(args[1])
        return args[0]

    def adc_init_val(self, args):
        args[0] = {"adc_init_val": args[0].value}
        if len(args) == 2:
            args[0].update(args[1])
        return args[0]


class Signal:
    def __init__(self, signal_name="", signal_format=16, dat_file=None, adc_spec=None):
        self.signal_name = signal_name
        self.signal_format = signal_format
        self.dat_file = dat_file
        self.adc_spec = adc_spec

    @classmethod
    def from_subtree(cls, subtree):
        return EvaluateSignal().transform(subtree)

    def read_dat(self):
        if self.dat_file is None:
            raise FileNotFoundError("dat_file is not defined")

    def __repr__(self):
        return f"Signal {self.signal_name}(FMT{self.signal_format})"
