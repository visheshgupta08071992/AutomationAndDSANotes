## TestingMiniBytes Automation

### What is Rest
Rest is Representational State Transfer. Wheneve we send request from service to another,we dont send the object instead we send the representational state of that
object(eg Json,xm,yaml) at that particular time.

### Serialization/Marshelling
Conversion of Java Object into Json is know as Serialization or Marshelling.

### DeSerialization/UnMarshelling
Conversion of  Json into Java Object is know as DeSerialization or UnMarshelling.

### Json rules
1. {} - Json Object</br>
2. [] - Json Array</br>
3. Key-Value pair</br>
4. Each Key-Value pair is separated by commma</br>
5. All the Keys are of type String</br>
6. Values can be String,Integer,Boolean,JsonObject,JsonArray

### Rest API's are StateLess?
It means that while sending any request from client to server,One must ensure to send complete details within the request and not rely on the server remembering previous requests, REST applications require each request to contain all of the information necessary for the server to understand it. Storing session state on the server violates the REST architecture's stateless requirement.

As per the REST (REpresentational “State” Transfer) architecture, the server does not store any state about the client session on the server-side. This restriction is called Statelessness.

Each request from the client to the server must contain all of the necessary information to understand the request. The server cannot take advantage of any stored context on the server.

The application’s session state is therefore kept entirely on the client. The client is responsible for storing and handling the session related information on its own side.

This also means that the client is responsible for sending any state information to the server whenever it is needed. There should not be any session affinity or sticky session between the client and the server.


### PostMan Terminologies

 **Collection(Folder)** - Collection is a folder which is a group of similar request
