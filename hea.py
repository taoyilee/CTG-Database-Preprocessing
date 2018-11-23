class Hea:
    signals = []
    blocks = []

    def __init__(self, record_name="", number_of_segments=None, number_of_signals=1, sampling_frequency=250):
        self.record_name = record_name
        self.number_of_segments = number_of_segments
        self.number_of_signals = number_of_signals
        self.sampling_frequency = sampling_frequency

    def to_dataframe(self):
        pass

    def add_signal(self, signal):
        self.signals.append(signal)

    def add_blocks(self, block):
        self.blocks.append(block)

    def __repr__(self):
        return f"Hea Record {self.record_name}: {len(self.signals)} signals, {len(self.blocks)} data blocks"
