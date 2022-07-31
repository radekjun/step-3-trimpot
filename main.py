def on_forever():
    led.plot_bar_graph(pins.analog_read_pin(AnalogPin.P0), 1023)
    #basic.show_number(pins.analog_read_pin(AnalogPin.P0), 1023)
basic.forever(on_forever)
