// basic.show_number(pins.analog_read_pin(AnalogPin.P0), 1023)
basic.forever(function on_forever() {
    led.plotBarGraph(pins.analogReadPin(AnalogPin.P0), 1023)
})
