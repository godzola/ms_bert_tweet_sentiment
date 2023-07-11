FROM python:3.8

WORKDIR /code

#
# When we run the model we get an error you can see in the README.md something to the effect:
#   Xformers is not installed correctly. If you want to use memory_efficient_attention to accelerate training ... etc...
#
# I think it's because this isn't a GPU docker, but it was suggested in some google groups that you can
#  get the message to go away if you install from the source git. So for us... that would mean taking xformers out of
#  the requirements.txt file and adding this line:
#
# RUN pip install git+https://github.com/facebookresearch/xformers.git@main#egg=xformers 
#
# I didn't try it yet, but's out there.

COPY ./requirements.txt /code/requirements.txt
COPY ./main.py /code/
# COPY ./model/  /code/model/
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8080"]
