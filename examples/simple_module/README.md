# VIAM Simple Module Example
This example goes through how to create custom modular resources using Viam's python SDK, and how to connect it to a Robot.

This is a limited document. For a more in-depth understanding of modules, see the [documentation](https://docs.viam.com/program/extend/modular-resources/).

## Purpose
Modular resources allow you to define custom components and services, and add them to your robot. Viam ships with many component types, but you're not limited to only using those types -- you can create your own using modules.

For more information, see the [documentation](https://docs.viam.com/program/extend/modular-resources/). For a more complex example, take a look at the [complex module example](https://github.com/viamrobotics/viam-python-sdk/tree/main/examples/complex_module), which contains multiple new APIs and custom resource models.

## Project structure
The definition of the new resources are in the `main` file of the `src` directory.

The `run.sh` script is the entrypoint for a module and calls the `main.py` file. The `main.py` file contains the definition of a new sensor model and code to register it. When called, the program creates and starts the module. Read further to learn how to connect this module to your robot.

Outside the `src` directory, there is a `client.py` file. You can use this file to test the module once you have connected to your robot and configured the module. You will have to update the credentials and robot address in that file.

## Configuring and using the module
These steps assume that you have a robot available at [app.viam.com](app.viam.com).

The `run.sh` script is the entrypoint for this module. To connect this module with your robot, you must add this module's entrypoint to the robot's config. For example, the entrypoint file may be at `/home/viam-python-sdk/examples/simple_module/run.sh` and you must add this file path to your configuration. See the [documentation](https://docs.viam.com/program/extend/modular-resources/#use-a-modular-resource-with-your-robot) for more details.

Once the module has been added to your robot, add a new component that uses the `MySensor` model. See the [documentation](https://docs.viam.com/program/extend/modular-resources/#configure-a-component-instance-for-a-modular-resource) for more details.

An example configuration for a Sensor component could look like this:
```json
{
  "components": [
    {
      "name": "sensor1",
      "type": "sensor",
      "model": "acme:demo:mysensor",
      "attributes": {},
      "depends_on": []
    }
  ],
  "modules": [
    {
      "name": "my-module",
      "executable_path": "/home/viam-python-sdk/examples/simple_module/run.sh"
    }
  ]
}
```

After the robot has started and connected to the module, you can use the provided `client.py` to connect to your robot and make calls to your custom, modular resources.
