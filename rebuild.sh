podman image build . --tag sicprodmodel:latest
podman run -dt --name sicprodmodel localhost/sicprodmodel:latest /bin/bash
podman container cp sicprodmodel:/tmp/index.html .
podman container cp sicprodmodel:/tmp/index.docx .
podman container cp sicprodmodel:/tmp/index.svg .

# clean up after yourself

podman stop sicprodmodel
podman container rm sicprodmodel