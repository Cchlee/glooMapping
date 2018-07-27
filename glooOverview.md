Working With Gloo

  

Gloo Overview:

Gloo serves as a gateway that connects client requests to any backend interface. It serves as the “glue” between clients and their service requests. This makes it able to map REST API to gRPC.

  

Quicklinks:

  

-Gloo’s Home Website 

[https://gloo.solo.io/](https://gloo.solo.io/)

  

-Video Tutorial for Running Gloo

[https://medium.com/solo-io/new-in-gloo-connect-json-clients-to-your-grpc-services-4724656ed15f](https://medium.com/solo-io/new-in-gloo-connect-json-clients-to-your-grpc-services-4724656ed15f)

  

-Git Tutorial for Gloo

[https://github.com/solo-io/gloo/tree/master/example/grpc](https://github.com/solo-io/gloo/tree/master/example/grpc)

  

-Gloo Basic Steps for mapping HTTP Requests to gRPC

  

1. Deploy the Service 
    1. Kubectl  apply -f &lt;DEPLOYMENT&gt; 

2. Create a route for upstream to backend 
    1. Glooctl route create  
        1. --path-exact /REQUEST-NAME 
        2. --http-method METHOD-TYPE (GET, POST, DELETE, .etc) 
        3. --upstream DEPLOYMENT-NAME 
        4. --function NAME-OF-FUNCTION 

3. Get URL of Gateway 
4. Run curl method in terminal with URL 
  

Upstreams

- [https://gloo.solo.io/introduction/concepts/#Upstreams](https://gloo.solo.io/introduction/concepts/#Upstreams) 
- Define destinations for routes, to connect gloo to services 
- Spec field defines where to route to  
- Essential for Gloo architecture 
- Created when deploying .yaml files 
- [https://github.com/solo-io/glooctl](https://github.com/solo-io/glooctl) 
    - Gives guides on using upstreams