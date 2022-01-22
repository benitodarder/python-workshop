# Python workshop, sockets, echo

Simple echo console apps.

* One message:
    * &lt;winpty&gt; python echoServer.py &lt;address&gt; &lt;port&gt; &lt;buffer&gt;
    * &lt;winpty&gt; python echoClient.py &lt;address&gt; &lt;port&gt; &lt;buffer&gt; &lt;messages&gt;
* Endless messages, a kinda one-way chat:
    * &lt;winpty&gt; python echoServerEndless.py &lt;address&gt; &lt;port&gt; &lt;buffer&gt;
    * &lt;winpty&gt; python echoClientEndless.py &lt;address&gt; &lt;port&gt; &lt;buffer&gt;
