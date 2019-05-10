# Cizsle Server - Docker Image

FROM python:3.6-alpine AS builder

# Install the system packages needed to build the Python application and its dependencies
RUN apk add --no-cache --virtual .build-deps build-base && \
    pip install -q --upgrade --no-cache-dir pip setuptools wheel


# Install the application and its dependencies to /root/.local
RUN pip install -q --user --no-cache-dir cizsle[server]




FROM python:3.6-alpine
ARG user=cizsle
ARG uid=25639
ARG group=cizsle
ARG gid=25639
ARG admin_dir=/admin


ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8


# Ensure Python package installation tools are up-to-date
RUN pip install -q --upgrade --no-cache-dir pip setuptools wheel


# Setup directories and non-priviledged user
RUN mkdir -p $admin_dir && \
    addgroup -g $gid $group && \
    adduser -D -G $group -u $uid $user && \
    chown -R $user:$group $admin_dir
ENV PATH=/home/$user/.local/bin:$PATH
USER $user


# Copy the installed application and its dependencies from the builder stage
COPY --from=builder /root/.local /home/$user/.local


# Fix Permissions
USER root
RUN chown -R $user:$group /home/$user $admin_dir
USER $user


# Expose Volume(s) and set the working directory
VOLUME $admin_dir
WORKDIR $admin_dir


# Start the cizsle server
CMD ["cizsle-server"]
