""" resistors.py -- Resistors problem for Test 1 
TPRG2131 Fall 202x Test 1
"""
# Mankaran Singh Chattha
# 100944566
# test Tprg1
# in this I have given variable resistance as 1000 and kept the percentage
#  passive two-terminal electrical component that implements electrical resistance as a circuit element
class Resistor(object):
    """Model a fixed resistor."""
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms."""
        self.resistance = res
# flow of charge per unit time. 
    def current(self, voltage):
        """Given a voltage across the resistor, return the current."""
        return voltage / self.resistance

    def __str__(self):
        """Return a string representation of the resistor."""
        return "R=" + str(self.resistance)


### DEFINE class VariableResistor
    # resistor whose value of electrical resistance can be changed on demand.
class VariableResistor(Resistor):
    """Model a variable resistor that can adjust its resistance."""
    
    def __init__(self, res):
        """Constructor sets the fixed resistance in ohms and initializes actual resistance."""
        super().__init__(res)
        self.actual_resistance = res  # Start with the maximum resistance

    def set_resistance(self, percent):
        """Set the actual resistance as a percentage of the fixed resistance.
        
        Args:
            percent (float): A percentage value between 0 and 100.
        
        Raises:
            ValueError: If the percent is not between 0 and 100.
        """
        if 0 <= percent <= 100:
            self.actual_resistance = (percent / 100) * self.resistance
        else:
            raise ValueError("Percent must be between 0 and 100.")
# flow of charge per unit time. 
    def current(self, voltage):
        """Override current method to use actual_resistance."""
        if self.actual_resistance == 0:
            return "Error: Actual resistance is zero; current cannot be calculated."
        return voltage / self.actual_resistance  # Use actual_resistance for current calculation

    def __str__(self):
        """Return a string representation of the variable resistor."""
        return f"R={self.resistance}, Actual R={self.actual_resistance}"


if __name__ == "__main__": # Start with the maximum resistance
    r1 = Resistor(1000.0)
    print("R1:", r1)
    print("R1: voltage=12.0, current=", r1.current(12.0))

    # Testing VariableResistor
    vr1 = VariableResistor(1000.0)
    print("VR1:", vr1)
    
    # Set actual resistance to 50% of the fixed resistance
    vr1.set_resistance(50)  # This will set actual resistance to 50% of 1000 ohms
    print("VR1 after setting resistance to 50%:", vr1)
    print("VR1: voltage=12.0, current=", vr1.current(12.0))
    
    # Testing with different voltages
    print("VR1: voltage=24.0, current=", vr1.current(24.0))
     # Calculate and print current for a different voltage
