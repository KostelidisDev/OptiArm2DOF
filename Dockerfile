# Build: docker build -f Dockerfile -t optiarm2dof .
# Run: docker run -it --rm optiarm2dof

FROM python:3.9 AS builder
WORKDIR /src
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY . .
RUN pyinstaller OptiArm2DOF.spec

FROM ubuntu:24.04
WORKDIR /opt/gr/ihu/robotics/OptiArm2DOF
COPY --from=builder /src/dist/OptiArm2DOF ./
COPY ./src/.env ./.env
COPY ./LICENSE .
CMD ["./OptiArm2DOF"]