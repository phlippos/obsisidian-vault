PX4 uses _MAVLink_ to communicate with ground stations and MAVLink SDKs, such as _QGroundControl_


consisting of a name (e.g. [ATTITUDE](https://mavlink.io/en/messages/common.html#ATTITUDE)), id, and fields containing relevant data.

no semantics for resending and acknowledgement.

MAVLink messages, commands and enumerations are defined in [XML definition files](https://mavlink.io/en/guide/define_xml_element.html).


Note that most generated libraries do not create code to implement microservices. ??? 


If you use a custom definition you will need maintain the definition in PX4, your ground station, and any other SDKs that communicate with it. Generally you should use (or add to) the standard definitions if at all possible to reduce the maintenance burden.


Custom definitions can be added in a new dialect file in the same directory as the standard XML definitions. For example, create `PX4-Autopilot/src/modules/mavlink/mavlink/message_definitions/v1.0/custom_messages.xml`, and set `CONFIG_MAVLINK_DIALECT` to build the new file for SITL. This dialect file should include `development.xml` so that all the standard definitions are also included.

For initial prototyping, or if you intend your message to be "standard", you can also add your messages to `common.xml` (or `development.xml`). This simplifies building, because you don't need to modify the dialect that is built.


### Adding Messages to `development.xml` (or `common.xml`)

#### Advantages:

1. **Simpler Build Process**:
    
    - You don't need to modify the build configuration, as `development.xml` is already included in the build process.
    - This approach avoids additional configuration steps, making it easier for initial prototyping.
2. **Immediate Availability**:
    
    - Messages added to `development.xml` (or `common.xml`) are immediately available to all MAVLink components that use these files.
    - Ensures compatibility with existing systems and tools that rely on the standard definitions.

#### Considerations:

1. **Standardization**:
    
    - If the message is intended to be widely used and become part of the official MAVLink standard, adding it to `development.xml` can streamline the process.
    - This approach requires a more formal review and acceptance process if you plan to contribute back to the MAVLink community.
2. **Maintenance**:
    
    - Changes to `development.xml` (or `common.xml`) affect all systems that use these files. This requires careful consideration to avoid breaking existing functionality.
    - Directly modifying these files can lead to conflicts when pulling updates from the upstream MAVLink repository.

### Creating a New Dialect File

#### Advantages:

1. **Isolation**:
    
    - Custom messages are isolated in a separate file, reducing the risk of conflicts with the standard MAVLink definitions.
    - Provides a clean separation between standard and custom messages.
2. **Flexibility**:
    
    - You can define and use custom messages specific to your application without impacting the standard MAVLink definitions.
    - Allows for more flexibility in development, as changes are localized to your dialect file.
3. **Custom Build Configuration**:
    
    - Allows for specific build configurations tailored to your custom messages and dialect.
    - Facilitates the management of custom messages as your project evolves.

## Streaming MAVLink Messages

### Define the Streaming Class[​](https://docs.px4.io/main/en/middleware/mavlink.html#define-the-streaming-class)

First create a file named `BATTERY_STATUS_DEMO.hpp` for your streaming class (named after the message to stream) inside the [/src/modules/mavlink/streams](https://github.com/PX4/PX4-Autopilot/tree/main/src/modules/mavlink/streams) directory.

`configure_stream_local()` is a function used within the PX4 autopilot firmware to set up the streaming of MAVLink messages. It configures how often specific MAVLink messages are sent to the ground control station (GCS) or other MAVLink-compatible systems.

When you want to stream a custom or standard MAVLink message at a specific rate, you use the `configure_stream_local()` function within the `mavlink_main.cpp` file. This function is called within a switch statement that sets up different streaming modes (e.g., `MAVLINK_MODE_NORMAL`, `MAVLINK_MODE_ONBOARD`, etc.).

### Understanding `configure_stream_local()`

The `configure_stream_local()` function takes two parameters:

1. **Stream Name**: The name of the message stream you want to configure.
2. **Rate**: The rate at which the message should be streamed, in Hertz (Hz)

### Streaming on Request[​](https://docs.px4.io/main/en/middleware/mavlink.html#streaming-on-request)

Some messages are only needed once, when particular hardware is connected, or under other circumstances. In order to avoid clogging communications links with messages that aren't needed you may not stream all messages by default, even at low rate.

If you needed, a GCS or other MAVLink API can request that particular messages are streamed at a particular rate using [MAV_CMD_SET_MESSAGE_INTERVAL](https://mavlink.io/en/messages/common.html#MAV_CMD_SET_MESSAGE_INTERVAL). A particular message can be requested just once using [MAV_CMD_REQUEST_MESSAGE](https://mavlink.io/en/messages/common.html#MAV_CMD_REQUEST_MESSAGE).




![[Pasted image 20241102010313.png]]