Testing with Locust:

**Getting Started:**

[https://docs.locust.io/en/latest/installation.html](https://docs.locust.io/en/latest/installation.html)

**Useful files:**

[https://gist.github.com/skyrocknroll/9d434a76400f64b7947bf9ae0b6128ed](https://gist.github.com/skyrocknroll/9d434a76400f64b7947bf9ae0b6128ed)

(Sample file for gRPC testing with Locust)

[https://docs.locust.io/en/latest/writing-a-locustfile.html](https://docs.locust.io/en/latest/writing-a-locustfile.html)

(Breaks down different parts of Locustfile)

[https://docs.locust.io/en/latest/testing-other-systems.html](https://docs.locust.io/en/latest/testing-other-systems.html)

(Done in xml but provides good explanation on how working with non-HTTP clients works)

**Overview**

1. Create a locustfile.py
2. In the ApiUser class add test functions,
3. Testing works with try methods:

try:

        CLIENT\_SERVICE\_REQUEST

cxcept xmlrpclib.Fault as e

        events.request\_failure.fire(…) #Test Fails

else:

        events.request\_success.fire(…) #Test Succeeds

1. Both methods take 4 parameters which are inputted manually:
  1. request\_type
  2. name
  3. response\_time
  4. exception (for failures), response length (for success)

1. To run, make sure the server side is running on a different tab, and then input locust --host=http://example.com
2. Go to [http://127.0.0.1:8089/](http://127.0.0.1:8089/) on your browser, and runTesting with Locust:

**Getting Started:**

[https://docs.locust.io/en/latest/installation.html](https://docs.locust.io/en/latest/installation.html)

**Useful files:**

[https://gist.github.com/skyrocknroll/9d434a76400f64b7947bf9ae0b6128ed](https://gist.github.com/skyrocknroll/9d434a76400f64b7947bf9ae0b6128ed)

(Sample file for gRPC testing with Locust)

[https://docs.locust.io/en/latest/writing-a-locustfile.html](https://docs.locust.io/en/latest/writing-a-locustfile.html)

(Breaks down different parts of Locustfile)

[https://docs.locust.io/en/latest/testing-other-systems.html](https://docs.locust.io/en/latest/testing-other-systems.html)

(Done in xml but provides good explanation on how working with non-HTTP clients works)

**Overview**

1. Create a locustfile.py
2. In the ApiUser class add test functions,
3. Testing works with try methods:

try:

        CLIENT\_SERVICE\_REQUEST

cxcept xmlrpclib.Fault as e

        events.request\_failure.fire(…) #Test Fails

else:

        events.request\_success.fire(…) #Test Succeeds

1. Both methods take 4 parameters which are inputted manually:
  1. request\_type
  2. name
  3. response\_time
  4. exception (for failures), response length (for success)

1. To run, make sure the server side is running on a different tab, and then input locust --host=http://example.com
2. Go to [http://127.0.0.1:8089/](http://127.0.0.1:8089/) on your browser, and run