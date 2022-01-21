# Python workshop, sockets, echo

Simple echo console apps.

* One message:
    * <winpty> python echoServer.py <address> <port> <buffer>
    * <winpty> python echoClient.py <address> <port> <buffer> <messages>
* Endless messages, a kinda one-way chat:
    * <winpty> python echoServerThreading.py <address> <port> <buffer>
    * <winpty> python echoClientThreading.py <address> <port> <buffer>
