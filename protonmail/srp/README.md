# Secure Remote Password submodule
This submodule provides the interface to the custom implementation of ProtonMail's SRP API.
It automatically tries to load the constant time ctypes + OpenSSL implementation, 
and on failure it uses the native long int implementation.
It is based on [pysrp](https://github.com/cocagne/pysrp).

## Examples
### Authenticate against the API
```python
from proton.srp import User
usr = User(password, modulus)
client_challenge = usr.get_challenge()

# Get server challenge and user salt...

client_proof = usr.process_challenge(salt, server_challenge, version)

# Send client proof...

usr.verify_session(server_proof)
if usr.authenticated():
    print("Logged in!")
```

### Generate new random verifier
```python
from proton.srp import User
usr = User(password, modulus)
generated_salt, generated_v = usr.compute_v()
```

### Generate verifier given salt
```python
from proton.srp import User
usr = User(password, modulus)
generated_salt, generated_v = usr.compute_v(salt)
```
