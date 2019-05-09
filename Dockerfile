# Cizsle Server - Development Docker Image
FROM python:3.6-alpine

ARG user=cizsle
ARG uid=25639
ARG group=cizsle
ARG gid=25639
ARG app_dir=/home/$user/app
ARG admin_dir=/admin


ENV LC_ALL=C.UTF-8 \
    LANG=C.UTF-8


# Install system packages
# Needed for development-only
RUN apk add --no-cache bash make


# Ensure Python package installation tools are up-to-date
RUN pip install -q --upgrade --no-cache-dir pip setuptools wheel


# Setup directories and non-priviledged user
RUN mkdir -p $app_dir $admin_dir && \
    addgroup -g $gid $group && \
    adduser -D -G $group -u $uid $user
ENV PATH=/home/$user/.local/bin:$PATH
USER $user


# Install app dependencies
COPY requirements.txt requirements-dev.txt $app_dir/
RUN pip install --user -q --no-cache-dir -r $app_dir/requirements.txt -r $app_dir/requirements-dev.txt


# Copy Application Code
COPY ./ $app_dir/


# Fix Permissions
USER root
RUN chown -R $user:$group $app_dir $admin_dir && \
    chmod 755 $app_dir $admin_dir
USER $user


# Install App
RUN pip install --user --no-cache-dir -e $app_dir/


# Expose Volume(s) and set the working directory
VOLUME $admin_dir $app_dir
WORKDIR $app_dir


# Start the cizsle server
CMD ["cizsle-server"]
