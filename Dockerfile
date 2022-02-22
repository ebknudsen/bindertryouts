FROM ebknudsen/msre-nojpnb-server:0.0.9
RUN pip install --no-cache-dir requests jupyterlab
ARG NB_UID=1000
#check if uid 1000 is already set, if not set it.
USER root
RUN if ! id -u ${NB_UID}; then adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER};\
    fi
RUN NB_USER=`id -nu ${NB_UID}`

COPY . ${HOME}
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}
