FROM ghcr.io/dasch124/modeller:v1_beta

WORKDIR /tmp

COPY ./*.xml .
RUN tree .

RUN modeller/build.sh -a generateDocs -i model.xml -o index -v -l debug.log