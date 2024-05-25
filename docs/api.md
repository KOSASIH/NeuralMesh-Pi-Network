# api.md

NeuralMesh-Pi-Network provides a REST API for generating 3D meshes from 2D images.

## Here are the available API endpoints:

- `POST /predict`: Generates a 3D mesh from a 2D image.

The `POST /predict` endpoint accepts a POST request with an image field containing the 2D image.

The response contains a mesh field with the generated 3D mesh in STL format.

Here is an example request using curl:

```bash
1. $ curl -X POST -F image=@path/to/image.png http://localhost:5000/predict
```

The response will contain the generated 3D mesh in STL format.

Please note that the `POST /predict` endpoint requires authentication. To authenticate, you can use the Authorization header with a valid API key.

To obtain an API key, please contact the NeuralMesh-Pi-Network team.

For more information on the API, please refer to the OpenAPI specification in the docs directory.
