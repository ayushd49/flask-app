# FROM python:3.11-slim
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install -r requirements.txt
# COPY app.py .
# EXPOSE 5000
# CMD ["python", "app.py"]

# syntax=docker/dockerfile:1
FROM golang:1.25
WORKDIR /src
COPY <<EOF ./test.go ./main.go

EOF
RUN go build -o /bin/hello ./main.go

FROM scratch
COPY --from=0 /bin/hello /bin/hello
CMD ["/bin/hello"]