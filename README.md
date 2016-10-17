# Description
core functions for the pygate application. This package contains the shared functionality of the gateway.

# supported functionality
- manage all the plugins:
	- load the required plugins
	- sync devices and assets for each plugin with the cloud
	- route actuator commands to the correct plugin
	- run and stop plugins
- manage all the processor plugins
- Cashing of asset states so that a minimum of queries have to be launched to the server.
- provide a thread secure connection to the cloud for plugins in the form of:
	- a gateway interface for plugins that support multiple devices
	- a device interface for plugins that implement a single device
- provide a common interface to the pygate configuration 
- provide a common flask interface for plugins that have a web interface
- provide a common device counter object for plugins that need to generate unique device names.

# installation
This module is available from pip and can be installed with the following command:

`pip install pygate-core`

Note: this module is automatically installed through the requirements.txt of the main pygate application. 
