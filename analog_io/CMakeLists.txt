
add_executable(analog_io
	analog_io.c
	)

# Pull in our pico_stdlib which pulls in commonly used features
target_link_libraries(analog_io pico_stdlib hardware_gpio hardware_adc hardware_pwm)

# enable usb output, disabled uart output
pico_enable_stdio_usb(analog_io 1)
pico_enable_stdio_uart(analog_io 0)

#create map/bin/hex file etc
pico_add_extra_outputs(analog_io)

