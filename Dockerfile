FROM ebknudsen/msre-nojpnb-server:0.0.9
RUN pip install --no-cache-dir notebook
ARG NB_UID=1000
ARG NB_USER=usr
#check if uid 1000 is already set, if not set it.
USER root
RUN getent passwd ${NB_UID} && adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}
RUN getent passwd $NB_UID && NB_USER=`id -nu ${NB_UID}`

COPY . ${HOME}
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
