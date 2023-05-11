#!/usr/bin/env python3
"""Circuit classes"""


class LogicGate:
    def __init__(self, lbl):
        self.label = lbl
        self.output = None

    def get_label(self):
        return self.label

    def get_output(self):
        self.output = self.perform_gate_logic()
        return self.output


class BinaryGate(LogicGate):
    def __init__(self, lbl):
        super().__init__(lbl)
        self.pin_a = None
        self.pin_b = None

    def get_pin_a(self):
        if self.pin_a == None:
            return input(
                f"Enter pin A input for gate \
                {self.get_label()}: "
            )
        else:
            return self.pin_a.get_from().get_output()

    def get_pin_b(self):
        return int(
            input(
                f"Enter pin B input for gate \
            {self.get_label()}: "
            )
        )

    def set_next_pin(self, source):
        if self.pin_a == None:
            self.pin_a = source
        else:
            if self.pin_b == None:
                self.pin_b = source
            else:
                raise RuntimeError("Error: NO EMPTY PINS")


class UnaryGate(LogicGate):
    def __init__(self, lbl):
        LogicGate.__init__(self, lbl)
        super().__init__(lbl)
        super(UnaryGate, self).__init__(lbl)
        super().__init__("UnaryGate", lbl)
        self.pin = None

    def get_pin(self):
        return int(
            input(
                f"Enter pin input for gate \
            {self.get_label()}: "
            )
        )


class AndGate(BinaryGate):
    def __init__(self, lbl):
        super().__init__(lbl)

    def perform_gate_logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class Connector:
    def __init__(self, fgate, tgate):
        self.from_gate = fgate
        self.to_gate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.from_gate

    def get_to(self):
        return self.to_gate
