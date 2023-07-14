FROM klakegg/hugo:0.110.0-alpine

COPY . /src

RUN cd /src

CMD ["server"]