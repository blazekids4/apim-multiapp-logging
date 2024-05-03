# Round Robin APIM Policy

This Azure API Management (APIM) policy XML file, round-robin-policy.xml, implements a round-robin load balancing strategy between two backend services. It does this by storing and updating a "backend-counter" variable in cache.

Here is a detailed explanation of the policy:

## Inbound section: This is where the request processing starts

- `<base />` applies the base policy (default behaviour) in the inbound section.

- `<cache-lookup-value key="backend-counter" variable-name="backend-counter" />` tries to get the value of the "backend-counter" from the cache.
- The first `<choose>` block checks if the "backend-counter" variable exists. If it doesn't, it sets the "backend-counter" to 0 and stores it in the cache for 100 seconds.

- The second `<choose>` block checks the value of the "backend-counter". If it's 0, it sets the backend service to "OpenAIUKS", increments the "backend-counter" to 1, and stores this value in the cache. If it's not 0 (i.e., 1 in this case), it sets the backend service to "OpenAIWUS", resets

- `<authentication-managed-identity>` is used to authenticate with Azure Cognitive Services using a Managed Identity.

- `<set-header>` sets the "Authorization" header to the bearer token obtained from the managed identity authentication.

- `<rewrite-uri>` keeps the original request URI path.

## Backend section: This section is used to handle any retries in case of a failure

- `<retry>` is set to retry the request up to 3 times if the response status code is 400 or above. It uses the same round-robin mechanism as the inbound section to switch between the backend services for each retry.

- `<forward-request buffer-request-body="true" />` forwards the request to the backend, buffering the request body.

## Outbound section: This is where the response processing starts

- `<base />` applies the base policy (default behavior) in the outbound section.

## On-error section: This section handles any errors that occur during processing

- `<base />` applies the base policy (default behavior) in the on-error section.

Overall, this policy is effective at distributing load across two backend services in a round-robin fashion. It also includes error handling and retry mechanisms to ensure robustness.
