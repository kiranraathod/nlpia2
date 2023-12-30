FROM pytorch/pytorch:2.1.1-cuda12.1-cudnn8-runtime
# FROM jupyter/base-notebook

# condaforge/miniforge3

ENV TRANSFORMERS_CACHE=/tmp/.cache
ENV TOKENIZERS_PARALLELISM=true
ENV PYTHONUNBUFFERED 1

# USER $NB_USER
USER ${NB_UID}

WORKDIR "${HOME}/nlpia2"

COPY environment.yml .
COPY requirements.txt .

# Add RUN statements to install packages as the $NB_USER defined in the base images.

# Add a "USER root" statement followed by RUN statements to install system packages using apt-get,
# change file permissions, etc.

# If you do switch to root, always be sure to add a "USER $NB_USER" command at the end of the
# file to ensure the image runs as a unprivileged user by default.

# USER root

# RUN conda env update --file ./environment.yml

RUN python3 -m pip install --no-cache-dir --upgrade pip && \
    python3 -m pip install --no-cache-dir -r requirements.txt
        # jupyter
        # tensorflow-cpu \
        # torch \ 
        # torchvision \
        # torchaudio \
        # jax \
        # jaxlib \
        # optax

# RUN python3 -m pip install --no-cache-dir \
#     transformers \
#     datasets\
#     nltk \
#     pytorch_lightning \
#     gradio \
#     sentencepiece \
#     seqeval

# RUN python3 -m spacy download en_core_web_sm

# RUN python3 -m spacy download en_core_web_md

# RUN python3 -m spacy download en_core_web_lg


# COPY requirements.txt .

# RUN pip install --upgrade pip --root-user-action=ignore && \
#     pip install -r requirements.txt --root-user-action=ignore --no-cache

# RUN python -m spacy download en_core_web_md && \
#     python -c 'from sentence_transformers import SentenceTransformer; sbert = SentenceTransformer("paraphrase-MiniLM-L6-v2"); print(sbert)'


# CMD ["${HOME}/nlpia2/scripts/entrypoint.sh"]



CMD ["jupyter", "notebook", "--ip", "0.0.0.0"]